---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient
title: Class FirewallPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:12.150885+00:00
---

# Class FirewallPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FirewallPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/FirewallPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The FirewallPolicies API.

This client uses FirewallPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response = firewallPoliciesClient.get(firewallPolicy);
     }
     

Note: close() needs to be called on the FirewallPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddAssociation |  Inserts an association for the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAssociationAsync(AddAssociationFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAssociationAsync(String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAssociationOperationCallable() 
  * addAssociationCallable() 

  
AddRule |  Inserts a rule into a firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addRuleAsync(AddRuleFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addRuleOperationCallable() 
  * addRuleCallable() 

  
CloneRules |  Copies rules to the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cloneRulesAsync(CloneRulesFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cloneRulesAsync(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cloneRulesOperationCallable() 
  * cloneRulesCallable() 

  
Delete |  Deletes the specified policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetAssociation |  Gets an association with the specified name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAssociation(GetAssociationFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAssociation(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAssociationCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetRule |  Gets a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRule(GetRuleFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRule(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleCallable() 

  
Insert |  Creates a new policy in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists all the policies that have been configured for the specified folder or organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListFirewallPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListAssociations |  Lists associations of a specified target, i.e., organization or folder. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAssociations(ListAssociationsFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAssociations() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAssociationsCallable() 

  
Move |  Moves the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveAsync(MoveFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveAsync(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveOperationCallable() 
  * moveCallable() 

  
Patch |  Patches the specified policy with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String firewallPolicy, FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchRule |  Patches a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchRuleAsync(PatchRuleFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchRuleOperationCallable() 
  * patchRuleCallable() 

  
RemoveAssociation |  Removes an association for the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAssociationAsync(RemoveAssociationFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeAssociationAsync(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAssociationOperationCallable() 
  * removeAssociationCallable() 

  
RemoveRule |  Deletes a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeRuleAsync(RemoveRuleFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeRuleAsync(String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeRuleOperationCallable() 
  * removeRuleCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String resource, GlobalOrganizationSetPolicyRequest globalOrganizationSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FirewallPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirewallPoliciesSettings firewallPoliciesSettings =
         FirewallPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FirewallPoliciesClient firewallPoliciesClient =
         FirewallPoliciesClient.create(firewallPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirewallPoliciesSettings firewallPoliciesSettings =
         FirewallPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     FirewallPoliciesClient firewallPoliciesClient =
         FirewallPoliciesClient.create(firewallPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FirewallPoliciesClient

## Static Methods 

### create()
    
    
    public static final FirewallPoliciesClient create()

Constructs an instance of FirewallPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirewallPoliciesSettings settings)
    
    
    public static final FirewallPoliciesClient create(FirewallPoliciesSettings settings)

Constructs an instance of FirewallPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirewallPoliciesStub stub)
    
    
    public static final FirewallPoliciesClient create(FirewallPoliciesStub stub)

Constructs an instance of FirewallPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(FirewallPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FirewallPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient)` |   
  
## Constructors 

### FirewallPoliciesClient(FirewallPoliciesSettings settings)
    
    
    protected FirewallPoliciesClient(FirewallPoliciesSettings settings)

Constructs an instance of FirewallPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesSettings)`  
  
  
### FirewallPoliciesClient(FirewallPoliciesStub stub)
    
    
    protected FirewallPoliciesClient(FirewallPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FirewallPoliciesStub)`  
  
  
## Methods 

### addAssociationAsync(AddAssociationFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(AddAssociationFirewallPolicyRequest request)

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddAssociationFirewallPolicyRequest request =
           AddAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.addAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationAsync(String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation firewallPolicyAssociationResource =
           FirewallPolicyAssociation.newBuilder().build();
       Operation response =
           firewallPoliciesClient
               .addAssociationAsync(firewallPolicy, firewallPolicyAssociationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyAssociationResource` | `[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationCallable()
    
    
    public final UnaryCallable<AddAssociationFirewallPolicyRequest,Operation> addAssociationCallable()

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddAssociationFirewallPolicyRequest request =
           AddAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           firewallPoliciesClient.addAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationOperationCallable()
    
    
    public final OperationCallable<AddAssociationFirewallPolicyRequest,Operation,Operation> addAssociationOperationCallable()

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddAssociationFirewallPolicyRequest request =
           AddAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.addAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(AddRuleFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(AddRuleFirewallPolicyRequest request)

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddRuleFirewallPolicyRequest request =
           AddRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.addRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           firewallPoliciesClient.addRuleAsync(firewallPolicy, firewallPolicyRuleResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleCallable()
    
    
    public final UnaryCallable<AddRuleFirewallPolicyRequest,Operation> addRuleCallable()

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddRuleFirewallPolicyRequest request =
           AddRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.addRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleOperationCallable()
    
    
    public final OperationCallable<AddRuleFirewallPolicyRequest,Operation,Operation> addRuleOperationCallable()

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       AddRuleFirewallPolicyRequest request =
           AddRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.addRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### cloneRulesAsync(CloneRulesFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(CloneRulesFirewallPolicyRequest request)

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       CloneRulesFirewallPolicyRequest request =
           CloneRulesFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       Operation response = firewallPoliciesClient.cloneRulesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesAsync(String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(String firewallPolicy)

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = firewallPoliciesClient.cloneRulesAsync(firewallPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesCallable()
    
    
    public final UnaryCallable<CloneRulesFirewallPolicyRequest,Operation> cloneRulesCallable()

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       CloneRulesFirewallPolicyRequest request =
           CloneRulesFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.cloneRulesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesOperationCallable()
    
    
    public final OperationCallable<CloneRulesFirewallPolicyRequest,Operation,Operation> cloneRulesOperationCallable()

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       CloneRulesFirewallPolicyRequest request =
           CloneRulesFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.cloneRulesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteFirewallPolicyRequest request)

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       DeleteFirewallPolicyRequest request =
           DeleteFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String firewallPolicy)

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = firewallPoliciesClient.deleteAsync(firewallPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteFirewallPolicyRequest,Operation> deleteCallable()

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       DeleteFirewallPolicyRequest request =
           DeleteFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteFirewallPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       DeleteFirewallPolicyRequest request =
           DeleteFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetFirewallPolicyRequest request)
    
    
    public final FirewallPolicy get(GetFirewallPolicyRequest request)

Returns the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetFirewallPolicyRequest request =
           GetFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .build();
       FirewallPolicy response = firewallPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### get(String firewallPolicy)
    
    
    public final FirewallPolicy get(String firewallPolicy)

Returns the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response = firewallPoliciesClient.get(firewallPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to get.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### getAssociation(GetAssociationFirewallPolicyRequest request)
    
    
    public final FirewallPolicyAssociation getAssociation(GetAssociationFirewallPolicyRequest request)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetAssociationFirewallPolicyRequest request =
           GetAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .build();
       FirewallPolicyAssociation response = firewallPoliciesClient.getAssociation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociation(String firewallPolicy)
    
    
    public final FirewallPolicyAssociation getAssociation(String firewallPolicy)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation response = firewallPoliciesClient.getAssociation(firewallPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociationCallable()
    
    
    public final UnaryCallable<GetAssociationFirewallPolicyRequest,FirewallPolicyAssociation> getAssociationCallable()

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetAssociationFirewallPolicyRequest request =
           GetAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .build();
       ApiFuture<FirewallPolicyAssociation> future =
           firewallPoliciesClient.getAssociationCallable().futureCall(request);
       // Do something.
       FirewallPolicyAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationFirewallPolicyRequest),[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)>` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetFirewallPolicyRequest,FirewallPolicy> getCallable()

Returns the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetFirewallPolicyRequest request =
           GetFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .build();
       ApiFuture<FirewallPolicy> future = firewallPoliciesClient.getCallable().futureCall(request);
       // Do something.
       FirewallPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)>` |   
  
### getIamPolicy(GetIamPolicyFirewallPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyFirewallPolicyRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetIamPolicyFirewallPolicyRequest request =
           GetIamPolicyFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setResource("resource-341064690")
               .build();
       Policy response = firewallPoliciesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String resource)
    
    
    public final Policy getIamPolicy(String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String resource = "resource-341064690";
       Policy response = firewallPoliciesClient.getIamPolicy(resource);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyFirewallPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetIamPolicyFirewallPolicyRequest request =
           GetIamPolicyFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = firewallPoliciesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getRule(GetRuleFirewallPolicyRequest request)
    
    
    public final FirewallPolicyRule getRule(GetRuleFirewallPolicyRequest request)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetRuleFirewallPolicyRequest request =
           GetRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .build();
       FirewallPolicyRule response = firewallPoliciesClient.getRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRule(String firewallPolicy)
    
    
    public final FirewallPolicyRule getRule(String firewallPolicy)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule response = firewallPoliciesClient.getRule(firewallPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRuleCallable()
    
    
    public final UnaryCallable<GetRuleFirewallPolicyRequest,FirewallPolicyRule> getRuleCallable()

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       GetRuleFirewallPolicyRequest request =
           GetRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .build();
       ApiFuture<FirewallPolicyRule> future =
           firewallPoliciesClient.getRuleCallable().futureCall(request);
       // Do something.
       FirewallPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleFirewallPolicyRequest),[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)>` |   
  
### getSettings()
    
    
    public final @Nullable FirewallPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.FirewallPoliciesSettings` |   
  
### getStub()
    
    
    public FirewallPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FirewallPoliciesStub)` |   
  
### insertAsync(FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(FirewallPolicy firewallPolicyResource)

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response = firewallPoliciesClient.insertAsync(firewallPolicyResource).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(InsertFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertFirewallPolicyRequest request)

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       InsertFirewallPolicyRequest request =
           InsertFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertFirewallPolicyRequest,Operation> insertCallable()

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       InsertFirewallPolicyRequest request =
           InsertFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertFirewallPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       InsertFirewallPolicyRequest request =
           InsertFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list()
    
    
    public final FirewallPoliciesClient.ListPagedResponse list()

Lists all the policies that have been configured for the specified folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       for (FirewallPolicy element : firewallPoliciesClient.list().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient.ListPagedResponse)` |   
  
### list(ListFirewallPoliciesRequest request)
    
    
    public final FirewallPoliciesClient.ListPagedResponse list(ListFirewallPoliciesRequest request)

Lists all the policies that have been configured for the specified folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       ListFirewallPoliciesRequest request =
           ListFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       for (FirewallPolicy element : firewallPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFirewallPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient.ListPagedResponse)` |   
  
### listAssociations()
    
    
    public final FirewallPoliciesListAssociationsResponse listAssociations()

Lists associations of a specified target, i.e., organization or folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       FirewallPoliciesListAssociationsResponse response = firewallPoliciesClient.listAssociations();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesListAssociationsResponse)` |   
  
### listAssociations(ListAssociationsFirewallPolicyRequest request)
    
    
    public final FirewallPoliciesListAssociationsResponse listAssociations(ListAssociationsFirewallPolicyRequest request)

Lists associations of a specified target, i.e., organization or folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       ListAssociationsFirewallPolicyRequest request =
           ListAssociationsFirewallPolicyRequest.newBuilder()
               .setIncludeInheritedPolicies(true)
               .setTargetResource("targetResource-1933150017")
               .build();
       FirewallPoliciesListAssociationsResponse response =
           firewallPoliciesClient.listAssociations(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAssociationsFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesListAssociationsResponse)` |   
  
### listAssociationsCallable()
    
    
    public final UnaryCallable<ListAssociationsFirewallPolicyRequest,FirewallPoliciesListAssociationsResponse> listAssociationsCallable()

Lists associations of a specified target, i.e., organization or folder.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       ListAssociationsFirewallPolicyRequest request =
           ListAssociationsFirewallPolicyRequest.newBuilder()
               .setIncludeInheritedPolicies(true)
               .setTargetResource("targetResource-1933150017")
               .build();
       ApiFuture<FirewallPoliciesListAssociationsResponse> future =
           firewallPoliciesClient.listAssociationsCallable().futureCall(request);
       // Do something.
       FirewallPoliciesListAssociationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAssociationsFirewallPolicyRequest),[FirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesListAssociationsResponse)>` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListFirewallPoliciesRequest,FirewallPolicyList> listCallable()

Lists all the policies that have been configured for the specified folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       ListFirewallPoliciesRequest request =
           ListFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       while (true) {
         FirewallPolicyList response = firewallPoliciesClient.listCallable().call(request);
         for (FirewallPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFirewallPoliciesRequest),[FirewallPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListFirewallPoliciesRequest,FirewallPoliciesClient.ListPagedResponse> listPagedCallable()

Lists all the policies that have been configured for the specified folder or organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       ListFirewallPoliciesRequest request =
           ListFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<FirewallPolicy> future =
           firewallPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (FirewallPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFirewallPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPoliciesClient.ListPagedResponse)>` |   
  
### moveAsync(MoveFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> moveAsync(MoveFirewallPolicyRequest request)

Moves the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       MoveFirewallPolicyRequest request =
           MoveFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.moveAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveAsync(String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> moveAsync(String firewallPolicy)

Moves the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = firewallPoliciesClient.moveAsync(firewallPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveCallable()
    
    
    public final UnaryCallable<MoveFirewallPolicyRequest,Operation> moveCallable()

Moves the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       MoveFirewallPolicyRequest request =
           MoveFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.moveCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveOperationCallable()
    
    
    public final OperationCallable<MoveFirewallPolicyRequest,Operation,Operation> moveOperationCallable()

Moves the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       MoveFirewallPolicyRequest request =
           MoveFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.moveOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(PatchFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchFirewallPolicyRequest request)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchFirewallPolicyRequest request =
           PatchFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String firewallPolicy, FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String firewallPolicy, FirewallPolicy firewallPolicyResource)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response =
           firewallPoliciesClient.patchAsync(firewallPolicy, firewallPolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchFirewallPolicyRequest,Operation> patchCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchFirewallPolicyRequest request =
           PatchFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchFirewallPolicyRequest,Operation,Operation> patchOperationCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchFirewallPolicyRequest request =
           PatchFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(PatchRuleFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(PatchRuleFirewallPolicyRequest request)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchRuleFirewallPolicyRequest request =
           PatchRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.patchRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           firewallPoliciesClient.patchRuleAsync(firewallPolicy, firewallPolicyRuleResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleCallable()
    
    
    public final UnaryCallable<PatchRuleFirewallPolicyRequest,Operation> patchRuleCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchRuleFirewallPolicyRequest request =
           PatchRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.patchRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleOperationCallable()
    
    
    public final OperationCallable<PatchRuleFirewallPolicyRequest,Operation,Operation> patchRuleOperationCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       PatchRuleFirewallPolicyRequest request =
           PatchRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.patchRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(RemoveAssociationFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(RemoveAssociationFirewallPolicyRequest request)

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveAssociationFirewallPolicyRequest request =
           RemoveAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.removeAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(String firewallPolicy)

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = firewallPoliciesClient.removeAssociationAsync(firewallPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationCallable()
    
    
    public final UnaryCallable<RemoveAssociationFirewallPolicyRequest,Operation> removeAssociationCallable()

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveAssociationFirewallPolicyRequest request =
           RemoveAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           firewallPoliciesClient.removeAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationOperationCallable()
    
    
    public final OperationCallable<RemoveAssociationFirewallPolicyRequest,Operation,Operation> removeAssociationOperationCallable()

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveAssociationFirewallPolicyRequest request =
           RemoveAssociationFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.removeAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(RemoveRuleFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(RemoveRuleFirewallPolicyRequest request)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveRuleFirewallPolicyRequest request =
           RemoveRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       Operation response = firewallPoliciesClient.removeRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(String firewallPolicy)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = firewallPoliciesClient.removeRuleAsync(firewallPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleCallable()
    
    
    public final UnaryCallable<RemoveRuleFirewallPolicyRequest,Operation> removeRuleCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveRuleFirewallPolicyRequest request =
           RemoveRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = firewallPoliciesClient.removeRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleOperationCallable()
    
    
    public final OperationCallable<RemoveRuleFirewallPolicyRequest,Operation,Operation> removeRuleOperationCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       RemoveRuleFirewallPolicyRequest request =
           RemoveRuleFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           firewallPoliciesClient.removeRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyFirewallPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyFirewallPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       SetIamPolicyFirewallPolicyRequest request =
           SetIamPolicyFirewallPolicyRequest.newBuilder()
               .setGlobalOrganizationSetPolicyRequestResource(
                   GlobalOrganizationSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = firewallPoliciesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String resource, GlobalOrganizationSetPolicyRequest globalOrganizationSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String resource, GlobalOrganizationSetPolicyRequest globalOrganizationSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String resource = "resource-341064690";
       GlobalOrganizationSetPolicyRequest globalOrganizationSetPolicyRequestResource =
           GlobalOrganizationSetPolicyRequest.newBuilder().build();
       Policy response =
           firewallPoliciesClient.setIamPolicy(resource, globalOrganizationSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalOrganizationSetPolicyRequestResource` | `[GlobalOrganizationSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOrganizationSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyFirewallPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       SetIamPolicyFirewallPolicyRequest request =
           SetIamPolicyFirewallPolicyRequest.newBuilder()
               .setGlobalOrganizationSetPolicyRequestResource(
                   GlobalOrganizationSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = firewallPoliciesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsFirewallPolicyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsFirewallPolicyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       TestIamPermissionsFirewallPolicyRequest request =
           TestIamPermissionsFirewallPolicyRequest.newBuilder()
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = firewallPoliciesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           firewallPoliciesClient.testIamPermissions(resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsFirewallPolicyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirewallPoliciesClient firewallPoliciesClient = FirewallPoliciesClient.create()) {
       TestIamPermissionsFirewallPolicyRequest request =
           TestIamPermissionsFirewallPolicyRequest.newBuilder()
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           firewallPoliciesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsFirewallPolicyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
