---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient
title: Class NetworkFirewallPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:07.169738+00:00
---

# Class NetworkFirewallPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkFirewallPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/NetworkFirewallPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The NetworkFirewallPolicies API.

This client uses NetworkFirewallPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response = networkFirewallPoliciesClient.get(project, firewallPolicy);
     }
     

Note: close() needs to be called on the NetworkFirewallPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddAssociation |  Inserts an association for the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAssociationAsync(AddAssociationNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAssociationAsync(String project, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAssociationOperationCallable() 
  * addAssociationCallable() 

  
AddPacketMirroringRule |  Inserts a packet mirroring rule into a firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addPacketMirroringRuleOperationCallable() 
  * addPacketMirroringRuleCallable() 

  
AddRule |  Inserts a rule into a firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addRuleAsync(AddRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addRuleOperationCallable() 
  * addRuleCallable() 

  
AggregatedList |  Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListNetworkFirewallPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
CloneRules |  Copies rules to the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cloneRulesAsync(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cloneRulesOperationCallable() 
  * cloneRulesCallable() 

  
Delete |  Deletes the specified policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetAssociation |  Gets an association with the specified name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAssociation(GetAssociationNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAssociation(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAssociationCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetPacketMirroringRule |  Gets a packet mirroring rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPacketMirroringRule(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPacketMirroringRuleCallable() 

  
GetRule |  Gets a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRule(GetRuleNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRule(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleCallable() 

  
Insert |  Creates a new policy in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists all the policies that have been configured for the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListNetworkFirewallPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified policy with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String firewallPolicy, FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchPacketMirroringRule |  Patches a packet mirroring rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchPacketMirroringRuleOperationCallable() 
  * patchPacketMirroringRuleCallable() 

  
PatchRule |  Patches a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchRuleAsync(PatchRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchRuleOperationCallable() 
  * patchRuleCallable() 

  
RemoveAssociation |  Removes an association for the specified firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeAssociationAsync(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAssociationOperationCallable() 
  * removeAssociationCallable() 

  
RemovePacketMirroringRule |  Deletes a packet mirroring rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removePacketMirroringRuleAsync(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removePacketMirroringRuleOperationCallable() 
  * removePacketMirroringRuleCallable() 

  
RemoveRule |  Deletes a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeRuleAsync(RemoveRuleNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeRuleAsync(String project, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeRuleOperationCallable() 
  * removeRuleCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworkFirewallPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkFirewallPoliciesSettings networkFirewallPoliciesSettings =
         NetworkFirewallPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create(networkFirewallPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkFirewallPoliciesSettings networkFirewallPoliciesSettings =
         NetworkFirewallPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create(networkFirewallPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkFirewallPoliciesClient

## Static Methods 

### create()
    
    
    public static final NetworkFirewallPoliciesClient create()

Constructs an instance of NetworkFirewallPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkFirewallPoliciesSettings settings)
    
    
    public static final NetworkFirewallPoliciesClient create(NetworkFirewallPoliciesSettings settings)

Constructs an instance of NetworkFirewallPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkFirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkFirewallPoliciesStub stub)
    
    
    public static final NetworkFirewallPoliciesClient create(NetworkFirewallPoliciesStub stub)

Constructs an instance of NetworkFirewallPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkFirewallPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkFirewallPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient)` |   
  
## Constructors 

### NetworkFirewallPoliciesClient(NetworkFirewallPoliciesSettings settings)
    
    
    protected NetworkFirewallPoliciesClient(NetworkFirewallPoliciesSettings settings)

Constructs an instance of NetworkFirewallPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkFirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesSettings)`  
  
  
### NetworkFirewallPoliciesClient(NetworkFirewallPoliciesStub stub)
    
    
    protected NetworkFirewallPoliciesClient(NetworkFirewallPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkFirewallPoliciesStub)`  
  
  
## Methods 

### addAssociationAsync(AddAssociationNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(AddAssociationNetworkFirewallPolicyRequest request)

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddAssociationNetworkFirewallPolicyRequest request =
           AddAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.addAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationAsync(String project, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(String project, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation firewallPolicyAssociationResource =
           FirewallPolicyAssociation.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .addAssociationAsync(project, firewallPolicy, firewallPolicyAssociationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyAssociationResource` | `[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationCallable()
    
    
    public final UnaryCallable<AddAssociationNetworkFirewallPolicyRequest,Operation> addAssociationCallable()

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddAssociationNetworkFirewallPolicyRequest request =
           AddAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.addAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationOperationCallable()
    
    
    public final OperationCallable<AddAssociationNetworkFirewallPolicyRequest,Operation,Operation> addAssociationOperationCallable()

Inserts an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddAssociationNetworkFirewallPolicyRequest request =
           AddAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.addAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addPacketMirroringRuleAsync(AddPacketMirroringRuleNetworkFirewallPolicyRequest request)

Inserts a packet mirroring rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddPacketMirroringRuleNetworkFirewallPolicyRequest request =
           AddPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.addPacketMirroringRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> addPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Inserts a packet mirroring rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .addPacketMirroringRuleAsync(project, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPacketMirroringRuleCallable()
    
    
    public final UnaryCallable<AddPacketMirroringRuleNetworkFirewallPolicyRequest,Operation> addPacketMirroringRuleCallable()

Inserts a packet mirroring rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddPacketMirroringRuleNetworkFirewallPolicyRequest request =
           AddPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.addPacketMirroringRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addPacketMirroringRuleOperationCallable()
    
    
    public final OperationCallable<AddPacketMirroringRuleNetworkFirewallPolicyRequest,Operation,Operation> addPacketMirroringRuleOperationCallable()

Inserts a packet mirroring rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddPacketMirroringRuleNetworkFirewallPolicyRequest request =
           AddPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient
               .addPacketMirroringRuleOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddPacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(AddRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(AddRuleNetworkFirewallPolicyRequest request)

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddRuleNetworkFirewallPolicyRequest request =
           AddRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.addRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .addRuleAsync(project, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleCallable()
    
    
    public final UnaryCallable<AddRuleNetworkFirewallPolicyRequest,Operation> addRuleCallable()

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddRuleNetworkFirewallPolicyRequest request =
           AddRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.addRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleOperationCallable()
    
    
    public final OperationCallable<AddRuleNetworkFirewallPolicyRequest,Operation,Operation> addRuleOperationCallable()

Inserts a rule into a firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AddRuleNetworkFirewallPolicyRequest request =
           AddRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.addRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListNetworkFirewallPoliciesRequest request)
    
    
    public final NetworkFirewallPoliciesClient.AggregatedListPagedResponse aggregatedList(AggregatedListNetworkFirewallPoliciesRequest request)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AggregatedListNetworkFirewallPoliciesRequest request =
           AggregatedListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, FirewallPoliciesScopedList> element :
           networkFirewallPoliciesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkFirewallPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final NetworkFirewallPoliciesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, FirewallPoliciesScopedList> element :
           networkFirewallPoliciesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkFirewallPoliciesRequest,NetworkFirewallPolicyAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AggregatedListNetworkFirewallPoliciesRequest request =
           AggregatedListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         NetworkFirewallPolicyAggregatedList response =
             networkFirewallPoliciesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, FirewallPoliciesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkFirewallPoliciesRequest),[NetworkFirewallPolicyAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPolicyAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkFirewallPoliciesRequest,NetworkFirewallPoliciesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of network firewall policies, listing network firewall policies from all applicable scopes (global and regional) and grouping the results per scope.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       AggregatedListNetworkFirewallPoliciesRequest request =
           AggregatedListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, FirewallPoliciesScopedList>> future =
           networkFirewallPoliciesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, FirewallPoliciesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkFirewallPoliciesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.AggregatedListPagedResponse)>` |   
  
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
  
### cloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(CloneRulesNetworkFirewallPolicyRequest request)

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       CloneRulesNetworkFirewallPolicyRequest request =
           CloneRulesNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       Operation response = networkFirewallPoliciesClient.cloneRulesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesAsync(String project, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(String project, String firewallPolicy)

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           networkFirewallPoliciesClient.cloneRulesAsync(project, firewallPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesCallable()
    
    
    public final UnaryCallable<CloneRulesNetworkFirewallPolicyRequest,Operation> cloneRulesCallable()

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       CloneRulesNetworkFirewallPolicyRequest request =
           CloneRulesNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.cloneRulesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesOperationCallable()
    
    
    public final OperationCallable<CloneRulesNetworkFirewallPolicyRequest,Operation,Operation> cloneRulesOperationCallable()

Copies rules to the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       CloneRulesNetworkFirewallPolicyRequest request =
           CloneRulesNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.cloneRulesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CloneRulesNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteNetworkFirewallPolicyRequest request)

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       DeleteNetworkFirewallPolicyRequest request =
           DeleteNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String firewallPolicy)

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response = networkFirewallPoliciesClient.deleteAsync(project, firewallPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteNetworkFirewallPolicyRequest,Operation> deleteCallable()

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       DeleteNetworkFirewallPolicyRequest request =
           DeleteNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkFirewallPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       DeleteNetworkFirewallPolicyRequest request =
           DeleteNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicy get(GetNetworkFirewallPolicyRequest request)

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetNetworkFirewallPolicyRequest request =
           GetNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .build();
       FirewallPolicy response = networkFirewallPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### get(String project, String firewallPolicy)
    
    
    public final FirewallPolicy get(String project, String firewallPolicy)

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response = networkFirewallPoliciesClient.get(project, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to get.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### getAssociation(GetAssociationNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicyAssociation getAssociation(GetAssociationNetworkFirewallPolicyRequest request)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetAssociationNetworkFirewallPolicyRequest request =
           GetAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .build();
       FirewallPolicyAssociation response = networkFirewallPoliciesClient.getAssociation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociation(String project, String firewallPolicy)
    
    
    public final FirewallPolicyAssociation getAssociation(String project, String firewallPolicy)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation response =
           networkFirewallPoliciesClient.getAssociation(project, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried association belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociationCallable()
    
    
    public final UnaryCallable<GetAssociationNetworkFirewallPolicyRequest,FirewallPolicyAssociation> getAssociationCallable()

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetAssociationNetworkFirewallPolicyRequest request =
           GetAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .build();
       ApiFuture<FirewallPolicyAssociation> future =
           networkFirewallPoliciesClient.getAssociationCallable().futureCall(request);
       // Do something.
       FirewallPolicyAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationNetworkFirewallPolicyRequest),[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)>` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetNetworkFirewallPolicyRequest,FirewallPolicy> getCallable()

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetNetworkFirewallPolicyRequest request =
           GetNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .build();
       ApiFuture<FirewallPolicy> future =
           networkFirewallPoliciesClient.getCallable().futureCall(request);
       // Do something.
       FirewallPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)>` |   
  
### getIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyNetworkFirewallPolicyRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetIamPolicyNetworkFirewallPolicyRequest request =
           GetIamPolicyNetworkFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = networkFirewallPoliciesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = networkFirewallPoliciesClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyNetworkFirewallPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetIamPolicyNetworkFirewallPolicyRequest request =
           GetIamPolicyNetworkFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           networkFirewallPoliciesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyNetworkFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicyRule getPacketMirroringRule(GetPacketMirroringRuleNetworkFirewallPolicyRequest request)

Gets a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetPacketMirroringRuleNetworkFirewallPolicyRequest request =
           GetPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .build();
       FirewallPolicyRule response = networkFirewallPoliciesClient.getPacketMirroringRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getPacketMirroringRule(String project, String firewallPolicy)
    
    
    public final FirewallPolicyRule getPacketMirroringRule(String project, String firewallPolicy)

Gets a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule response =
           networkFirewallPoliciesClient.getPacketMirroringRule(project, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getPacketMirroringRuleCallable()
    
    
    public final UnaryCallable<GetPacketMirroringRuleNetworkFirewallPolicyRequest,FirewallPolicyRule> getPacketMirroringRuleCallable()

Gets a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetPacketMirroringRuleNetworkFirewallPolicyRequest request =
           GetPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .build();
       ApiFuture<FirewallPolicyRule> future =
           networkFirewallPoliciesClient.getPacketMirroringRuleCallable().futureCall(request);
       // Do something.
       FirewallPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetPacketMirroringRuleNetworkFirewallPolicyRequest),[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)>` |   
  
### getRule(GetRuleNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicyRule getRule(GetRuleNetworkFirewallPolicyRequest request)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetRuleNetworkFirewallPolicyRequest request =
           GetRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .build();
       FirewallPolicyRule response = networkFirewallPoliciesClient.getRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRule(String project, String firewallPolicy)
    
    
    public final FirewallPolicyRule getRule(String project, String firewallPolicy)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule response = networkFirewallPoliciesClient.getRule(project, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRuleCallable()
    
    
    public final UnaryCallable<GetRuleNetworkFirewallPolicyRequest,FirewallPolicyRule> getRuleCallable()

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       GetRuleNetworkFirewallPolicyRequest request =
           GetRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .build();
       ApiFuture<FirewallPolicyRule> future =
           networkFirewallPoliciesClient.getRuleCallable().futureCall(request);
       // Do something.
       FirewallPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleNetworkFirewallPolicyRequest),[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkFirewallPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.NetworkFirewallPoliciesSettings` |   
  
### getStub()
    
    
    public NetworkFirewallPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkFirewallPoliciesStub)` |   
  
### insertAsync(InsertNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertNetworkFirewallPolicyRequest request)

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       InsertNetworkFirewallPolicyRequest request =
           InsertNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, FirewallPolicy firewallPolicyResource)

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient.insertAsync(project, firewallPolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertNetworkFirewallPolicyRequest,Operation> insertCallable()

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       InsertNetworkFirewallPolicyRequest request =
           InsertNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertNetworkFirewallPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new policy in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       InsertNetworkFirewallPolicyRequest request =
           InsertNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListNetworkFirewallPoliciesRequest request)
    
    
    public final NetworkFirewallPoliciesClient.ListPagedResponse list(ListNetworkFirewallPoliciesRequest request)

Lists all the policies that have been configured for the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       ListNetworkFirewallPoliciesRequest request =
           ListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (FirewallPolicy element : networkFirewallPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkFirewallPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final NetworkFirewallPoliciesClient.ListPagedResponse list(String project)

Lists all the policies that have been configured for the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       for (FirewallPolicy element : networkFirewallPoliciesClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkFirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListNetworkFirewallPoliciesRequest,FirewallPolicyList> listCallable()

Lists all the policies that have been configured for the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       ListNetworkFirewallPoliciesRequest request =
           ListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         FirewallPolicyList response = networkFirewallPoliciesClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkFirewallPoliciesRequest),[FirewallPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListNetworkFirewallPoliciesRequest,NetworkFirewallPoliciesClient.ListPagedResponse> listPagedCallable()

Lists all the policies that have been configured for the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       ListNetworkFirewallPoliciesRequest request =
           ListNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<FirewallPolicy> future =
           networkFirewallPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (FirewallPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkFirewallPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkFirewallPoliciesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchNetworkFirewallPolicyRequest request)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchNetworkFirewallPolicyRequest request =
           PatchNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String firewallPolicy, FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String firewallPolicy, FirewallPolicy firewallPolicyResource)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .patchAsync(project, firewallPolicy, firewallPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchNetworkFirewallPolicyRequest,Operation> patchCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchNetworkFirewallPolicyRequest request =
           PatchNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchNetworkFirewallPolicyRequest,Operation,Operation> patchOperationCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchNetworkFirewallPolicyRequest request =
           PatchNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchPacketMirroringRuleAsync(PatchPacketMirroringRuleNetworkFirewallPolicyRequest request)

Patches a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchPacketMirroringRuleNetworkFirewallPolicyRequest request =
           PatchPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           networkFirewallPoliciesClient.patchPacketMirroringRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchPacketMirroringRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Patches a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .patchPacketMirroringRuleAsync(project, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPacketMirroringRuleCallable()
    
    
    public final UnaryCallable<PatchPacketMirroringRuleNetworkFirewallPolicyRequest,Operation> patchPacketMirroringRuleCallable()

Patches a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchPacketMirroringRuleNetworkFirewallPolicyRequest request =
           PatchPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.patchPacketMirroringRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchPacketMirroringRuleOperationCallable()
    
    
    public final OperationCallable<PatchPacketMirroringRuleNetworkFirewallPolicyRequest,Operation,Operation> patchPacketMirroringRuleOperationCallable()

Patches a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchPacketMirroringRuleNetworkFirewallPolicyRequest request =
           PatchPacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient
               .patchPacketMirroringRuleOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchPacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchPacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(PatchRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(PatchRuleNetworkFirewallPolicyRequest request)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchRuleNetworkFirewallPolicyRequest request =
           PatchRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.patchRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(String project, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           networkFirewallPoliciesClient
               .patchRuleAsync(project, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleCallable()
    
    
    public final UnaryCallable<PatchRuleNetworkFirewallPolicyRequest,Operation> patchRuleCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchRuleNetworkFirewallPolicyRequest request =
           PatchRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.patchRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleOperationCallable()
    
    
    public final OperationCallable<PatchRuleNetworkFirewallPolicyRequest,Operation,Operation> patchRuleOperationCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       PatchRuleNetworkFirewallPolicyRequest request =
           PatchRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.patchRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(RemoveAssociationNetworkFirewallPolicyRequest request)

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveAssociationNetworkFirewallPolicyRequest request =
           RemoveAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.removeAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(String project, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(String project, String firewallPolicy)

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           networkFirewallPoliciesClient.removeAssociationAsync(project, firewallPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationCallable()
    
    
    public final UnaryCallable<RemoveAssociationNetworkFirewallPolicyRequest,Operation> removeAssociationCallable()

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveAssociationNetworkFirewallPolicyRequest request =
           RemoveAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.removeAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationOperationCallable()
    
    
    public final OperationCallable<RemoveAssociationNetworkFirewallPolicyRequest,Operation,Operation> removeAssociationOperationCallable()

Removes an association for the specified firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveAssociationNetworkFirewallPolicyRequest request =
           RemoveAssociationNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.removeAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAssociationNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removePacketMirroringRuleAsync(RemovePacketMirroringRuleNetworkFirewallPolicyRequest request)

Deletes a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemovePacketMirroringRuleNetworkFirewallPolicyRequest request =
           RemovePacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           networkFirewallPoliciesClient.removePacketMirroringRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePacketMirroringRuleAsync(String project, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removePacketMirroringRuleAsync(String project, String firewallPolicy)

Deletes a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           networkFirewallPoliciesClient
               .removePacketMirroringRuleAsync(project, firewallPolicy)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePacketMirroringRuleCallable()
    
    
    public final UnaryCallable<RemovePacketMirroringRuleNetworkFirewallPolicyRequest,Operation> removePacketMirroringRuleCallable()

Deletes a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemovePacketMirroringRuleNetworkFirewallPolicyRequest request =
           RemovePacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.removePacketMirroringRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removePacketMirroringRuleOperationCallable()
    
    
    public final OperationCallable<RemovePacketMirroringRuleNetworkFirewallPolicyRequest,Operation,Operation> removePacketMirroringRuleOperationCallable()

Deletes a packet mirroring rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemovePacketMirroringRuleNetworkFirewallPolicyRequest request =
           RemovePacketMirroringRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient
               .removePacketMirroringRuleOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemovePacketMirroringRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemovePacketMirroringRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(RemoveRuleNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(RemoveRuleNetworkFirewallPolicyRequest request)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveRuleNetworkFirewallPolicyRequest request =
           RemoveRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkFirewallPoliciesClient.removeRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(String project, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(String project, String firewallPolicy)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           networkFirewallPoliciesClient.removeRuleAsync(project, firewallPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleCallable()
    
    
    public final UnaryCallable<RemoveRuleNetworkFirewallPolicyRequest,Operation> removeRuleCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveRuleNetworkFirewallPolicyRequest request =
           RemoveRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkFirewallPoliciesClient.removeRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleOperationCallable()
    
    
    public final OperationCallable<RemoveRuleNetworkFirewallPolicyRequest,Operation,Operation> removeRuleOperationCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       RemoveRuleNetworkFirewallPolicyRequest request =
           RemoveRuleNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkFirewallPoliciesClient.removeRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveRuleNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyNetworkFirewallPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       SetIamPolicyNetworkFirewallPolicyRequest request =
           SetIamPolicyNetworkFirewallPolicyRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = networkFirewallPoliciesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           networkFirewallPoliciesClient.setIamPolicy(
               project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyNetworkFirewallPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       SetIamPolicyNetworkFirewallPolicyRequest request =
           SetIamPolicyNetworkFirewallPolicyRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           networkFirewallPoliciesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyNetworkFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsNetworkFirewallPolicyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       TestIamPermissionsNetworkFirewallPolicyRequest request =
           TestIamPermissionsNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = networkFirewallPoliciesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           networkFirewallPoliciesClient.testIamPermissions(
               project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsNetworkFirewallPolicyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkFirewallPoliciesClient networkFirewallPoliciesClient =
         NetworkFirewallPoliciesClient.create()) {
       TestIamPermissionsNetworkFirewallPolicyRequest request =
           TestIamPermissionsNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           networkFirewallPoliciesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNetworkFirewallPolicyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
