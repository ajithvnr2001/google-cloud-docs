---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient
title: Class RegionNetworkFirewallPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:49.776579+00:00
---

# Class RegionNetworkFirewallPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionNetworkFirewallPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionNetworkFirewallPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionNetworkFirewallPolicies API.

This client uses RegionNetworkFirewallPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response =
           regionNetworkFirewallPoliciesClient.get(project, region, firewallPolicy);
     }
     

Note: close() needs to be called on the RegionNetworkFirewallPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddAssociation |  Inserts an association for the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAssociationAsync(AddAssociationRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAssociationOperationCallable() 
  * addAssociationCallable() 

  
AddRule |  Inserts a rule into a network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addRuleAsync(AddRuleRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addRuleOperationCallable() 
  * addRuleCallable() 

  
CloneRules |  Copies rules to the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cloneRulesAsync(CloneRulesRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cloneRulesAsync(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cloneRulesOperationCallable() 
  * cloneRulesCallable() 

  
Delete |  Deletes the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetAssociation |  Gets an association with the specified name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAssociation(GetAssociationRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAssociation(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAssociationCallable() 

  
GetEffectiveFirewalls |  Returns the effective firewalls on a given network. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveFirewalls(GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveFirewalls(String project, String region, String network) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveFirewallsCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String region, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetRule |  Gets a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRule(GetRuleRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRule(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleCallable() 

  
Insert |  Creates a new network firewall policy in the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists all the network firewall policies that have been configured for the specified project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionNetworkFirewallPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String firewallPolicy, FirewallPolicy firewallPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchAssociation |  Updates an association for the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAssociationAsync(PatchAssociationRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchAssociationOperationCallable() 
  * patchAssociationCallable() 

  
PatchRule |  Patches a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchRuleAsync(PatchRuleRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchRuleOperationCallable() 
  * patchRuleCallable() 

  
RemoveAssociation |  Removes an association for the specified network firewall policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAssociationAsync(RemoveAssociationRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeAssociationAsync(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAssociationOperationCallable() 
  * removeAssociationCallable() 

  
RemoveRule |  Deletes a rule of the specified priority. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeRuleAsync(RemoveRuleRegionNetworkFirewallPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeRuleAsync(String project, String region, String firewallPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeRuleOperationCallable() 
  * removeRuleCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionNetworkFirewallPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionNetworkFirewallPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionNetworkFirewallPoliciesSettings regionNetworkFirewallPoliciesSettings =
         RegionNetworkFirewallPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create(regionNetworkFirewallPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionNetworkFirewallPoliciesSettings regionNetworkFirewallPoliciesSettings =
         RegionNetworkFirewallPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create(regionNetworkFirewallPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionNetworkFirewallPoliciesClient

## Static Methods 

### create()
    
    
    public static final RegionNetworkFirewallPoliciesClient create()

Constructs an instance of RegionNetworkFirewallPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionNetworkFirewallPoliciesSettings settings)
    
    
    public static final RegionNetworkFirewallPoliciesClient create(RegionNetworkFirewallPoliciesSettings settings)

Constructs an instance of RegionNetworkFirewallPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionNetworkFirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionNetworkFirewallPoliciesStub stub)
    
    
    public static final RegionNetworkFirewallPoliciesClient create(RegionNetworkFirewallPoliciesStub stub)

Constructs an instance of RegionNetworkFirewallPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionNetworkFirewallPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionNetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkFirewallPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient)` |   
  
## Constructors 

### RegionNetworkFirewallPoliciesClient(RegionNetworkFirewallPoliciesSettings settings)
    
    
    protected RegionNetworkFirewallPoliciesClient(RegionNetworkFirewallPoliciesSettings settings)

Constructs an instance of RegionNetworkFirewallPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionNetworkFirewallPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesSettings)`  
  
  
### RegionNetworkFirewallPoliciesClient(RegionNetworkFirewallPoliciesStub stub)
    
    
    protected RegionNetworkFirewallPoliciesClient(RegionNetworkFirewallPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionNetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkFirewallPoliciesStub)`  
  
  
## Methods 

### addAssociationAsync(AddAssociationRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(AddAssociationRegionNetworkFirewallPolicyRequest request)

Inserts an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddAssociationRegionNetworkFirewallPolicyRequest request =
           AddAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setAssociatedPolicyToBeReplaced("associatedPolicyToBeReplaced1754581094")
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.addAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)

Inserts an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation firewallPolicyAssociationResource =
           FirewallPolicyAssociation.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .addAssociationAsync(
                   project, region, firewallPolicy, firewallPolicyAssociationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyAssociationResource` | `[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationCallable()
    
    
    public final UnaryCallable<AddAssociationRegionNetworkFirewallPolicyRequest,Operation> addAssociationCallable()

Inserts an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddAssociationRegionNetworkFirewallPolicyRequest request =
           AddAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setAssociatedPolicyToBeReplaced("associatedPolicyToBeReplaced1754581094")
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.addAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationOperationCallable()
    
    
    public final OperationCallable<AddAssociationRegionNetworkFirewallPolicyRequest,Operation,Operation> addAssociationOperationCallable()

Inserts an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddAssociationRegionNetworkFirewallPolicyRequest request =
           AddAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setAssociatedPolicyToBeReplaced("associatedPolicyToBeReplaced1754581094")
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.addAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(AddRuleRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(AddRuleRegionNetworkFirewallPolicyRequest request)

Inserts a rule into a network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddRuleRegionNetworkFirewallPolicyRequest request =
           AddRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.addRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Inserts a rule into a network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .addRuleAsync(project, region, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleCallable()
    
    
    public final UnaryCallable<AddRuleRegionNetworkFirewallPolicyRequest,Operation> addRuleCallable()

Inserts a rule into a network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddRuleRegionNetworkFirewallPolicyRequest request =
           AddRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.addRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleOperationCallable()
    
    
    public final OperationCallable<AddRuleRegionNetworkFirewallPolicyRequest,Operation,Operation> addRuleOperationCallable()

Inserts a rule into a network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       AddRuleRegionNetworkFirewallPolicyRequest request =
           AddRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setMaxPriority(-207235553)
               .setMinPriority(267190513)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.addRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### cloneRulesAsync(CloneRulesRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(CloneRulesRegionNetworkFirewallPolicyRequest request)

Copies rules to the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       CloneRulesRegionNetworkFirewallPolicyRequest request =
           CloneRulesRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.cloneRulesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesAsync(String project, String region, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> cloneRulesAsync(String project, String region, String firewallPolicy)

Copies rules to the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           regionNetworkFirewallPoliciesClient
               .cloneRulesAsync(project, region, firewallPolicy)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesCallable()
    
    
    public final UnaryCallable<CloneRulesRegionNetworkFirewallPolicyRequest,Operation> cloneRulesCallable()

Copies rules to the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       CloneRulesRegionNetworkFirewallPolicyRequest request =
           CloneRulesRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.cloneRulesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cloneRulesOperationCallable()
    
    
    public final OperationCallable<CloneRulesRegionNetworkFirewallPolicyRequest,Operation,Operation> cloneRulesOperationCallable()

Copies rules to the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       CloneRulesRegionNetworkFirewallPolicyRequest request =
           CloneRulesRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceFirewallPolicy("sourceFirewallPolicy-593774771")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.cloneRulesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CloneRulesRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionNetworkFirewallPolicyRequest request)

Deletes the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       DeleteRegionNetworkFirewallPolicyRequest request =
           DeleteRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String firewallPolicy)

Deletes the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           regionNetworkFirewallPoliciesClient.deleteAsync(project, region, firewallPolicy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionNetworkFirewallPolicyRequest,Operation> deleteCallable()

Deletes the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       DeleteRegionNetworkFirewallPolicyRequest request =
           DeleteRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionNetworkFirewallPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       DeleteRegionNetworkFirewallPolicyRequest request =
           DeleteRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicy get(GetRegionNetworkFirewallPolicyRequest request)

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetRegionNetworkFirewallPolicyRequest request =
           GetRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       FirewallPolicy response = regionNetworkFirewallPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### get(String project, String region, String firewallPolicy)
    
    
    public final FirewallPolicy get(String project, String region, String firewallPolicy)

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy response =
           regionNetworkFirewallPoliciesClient.get(project, region, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to get.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)` |   
  
### getAssociation(GetAssociationRegionNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicyAssociation getAssociation(GetAssociationRegionNetworkFirewallPolicyRequest request)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetAssociationRegionNetworkFirewallPolicyRequest request =
           GetAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       FirewallPolicyAssociation response =
           regionNetworkFirewallPoliciesClient.getAssociation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociation(String project, String region, String firewallPolicy)
    
    
    public final FirewallPolicyAssociation getAssociation(String project, String region, String firewallPolicy)

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation response =
           regionNetworkFirewallPoliciesClient.getAssociation(project, region, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried association belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)` |   
  
### getAssociationCallable()
    
    
    public final UnaryCallable<GetAssociationRegionNetworkFirewallPolicyRequest,FirewallPolicyAssociation> getAssociationCallable()

Gets an association with the specified name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetAssociationRegionNetworkFirewallPolicyRequest request =
           GetAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<FirewallPolicyAssociation> future =
           regionNetworkFirewallPoliciesClient.getAssociationCallable().futureCall(request);
       // Do something.
       FirewallPolicyAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationRegionNetworkFirewallPolicyRequest),[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)>` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionNetworkFirewallPolicyRequest,FirewallPolicy> getCallable()

Returns the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetRegionNetworkFirewallPolicyRequest request =
           GetRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<FirewallPolicy> future =
           regionNetworkFirewallPoliciesClient.getCallable().futureCall(request);
       // Do something.
       FirewallPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionNetworkFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)>` |   
  
### getEffectiveFirewalls(GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest request)
    
    
    public final RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse getEffectiveFirewalls(GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest request)

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest request =
           GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse response =
           regionNetworkFirewallPoliciesClient.getEffectiveFirewalls(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewalls(String project, String region, String network)
    
    
    public final RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse getEffectiveFirewalls(String project, String region, String network)

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String network = "network1843485230";
       RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse response =
           regionNetworkFirewallPoliciesClient.getEffectiveFirewalls(project, region, network);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`network` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Network reference  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse)` |   
  
### getEffectiveFirewallsCallable()
    
    
    public final UnaryCallable<GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest,RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse> getEffectiveFirewallsCallable()

Returns the effective firewalls on a given network.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest request =
           GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest.newBuilder()
               .setNetwork("network1843485230")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse> future =
           regionNetworkFirewallPoliciesClient.getEffectiveFirewallsCallable().futureCall(request);
       // Do something.
       RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsRegionNetworkFirewallPolicyRequest),[RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse)>` |   
  
### getIamPolicy(GetIamPolicyRegionNetworkFirewallPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRegionNetworkFirewallPolicyRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetIamPolicyRegionNetworkFirewallPolicyRequest request =
           GetIamPolicyRegionNetworkFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       Policy response = regionNetworkFirewallPoliciesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String region, String resource)
    
    
    public final Policy getIamPolicy(String project, String region, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       Policy response = regionNetworkFirewallPoliciesClient.getIamPolicy(project, region, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRegionNetworkFirewallPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetIamPolicyRegionNetworkFirewallPolicyRequest request =
           GetIamPolicyRegionNetworkFirewallPolicyRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           regionNetworkFirewallPoliciesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionNetworkFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getRule(GetRuleRegionNetworkFirewallPolicyRequest request)
    
    
    public final FirewallPolicyRule getRule(GetRuleRegionNetworkFirewallPolicyRequest request)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetRuleRegionNetworkFirewallPolicyRequest request =
           GetRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       FirewallPolicyRule response = regionNetworkFirewallPoliciesClient.getRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRule(String project, String region, String firewallPolicy)
    
    
    public final FirewallPolicyRule getRule(String project, String region, String firewallPolicy)

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule response =
           regionNetworkFirewallPoliciesClient.getRule(project, region, firewallPolicy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)` |   
  
### getRuleCallable()
    
    
    public final UnaryCallable<GetRuleRegionNetworkFirewallPolicyRequest,FirewallPolicyRule> getRuleCallable()

Gets a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       GetRuleRegionNetworkFirewallPolicyRequest request =
           GetRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<FirewallPolicyRule> future =
           regionNetworkFirewallPoliciesClient.getRuleCallable().futureCall(request);
       // Do something.
       FirewallPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleRegionNetworkFirewallPolicyRequest),[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionNetworkFirewallPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesSettings` |   
  
### getStub()
    
    
    public RegionNetworkFirewallPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkFirewallPoliciesStub)` |   
  
### insertAsync(InsertRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionNetworkFirewallPolicyRequest request)

Creates a new network firewall policy in the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       InsertRegionNetworkFirewallPolicyRequest request =
           InsertRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, FirewallPolicy firewallPolicyResource)

Creates a new network firewall policy in the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .insertAsync(project, region, firewallPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionNetworkFirewallPolicyRequest,Operation> insertCallable()

Creates a new network firewall policy in the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       InsertRegionNetworkFirewallPolicyRequest request =
           InsertRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionNetworkFirewallPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new network firewall policy in the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       InsertRegionNetworkFirewallPolicyRequest request =
           InsertRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionNetworkFirewallPoliciesRequest request)
    
    
    public final RegionNetworkFirewallPoliciesClient.ListPagedResponse list(ListRegionNetworkFirewallPoliciesRequest request)

Lists all the network firewall policies that have been configured for the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       ListRegionNetworkFirewallPoliciesRequest request =
           ListRegionNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (FirewallPolicy element :
           regionNetworkFirewallPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkFirewallPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionNetworkFirewallPoliciesClient.ListPagedResponse list(String project, String region)

Lists all the network firewall policies that have been configured for the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (FirewallPolicy element :
           regionNetworkFirewallPoliciesClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkFirewallPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionNetworkFirewallPoliciesRequest,FirewallPolicyList> listCallable()

Lists all the network firewall policies that have been configured for the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       ListRegionNetworkFirewallPoliciesRequest request =
           ListRegionNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         FirewallPolicyList response =
             regionNetworkFirewallPoliciesClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkFirewallPoliciesRequest),[FirewallPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionNetworkFirewallPoliciesRequest,RegionNetworkFirewallPoliciesClient.ListPagedResponse> listPagedCallable()

Lists all the network firewall policies that have been configured for the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       ListRegionNetworkFirewallPoliciesRequest request =
           ListRegionNetworkFirewallPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<FirewallPolicy> future =
           regionNetworkFirewallPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (FirewallPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkFirewallPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkFirewallPoliciesClient.ListPagedResponse)>` |   
  
### patchAssociationAsync(PatchAssociationRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAssociationAsync(PatchAssociationRegionNetworkFirewallPolicyRequest request)

Updates an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchAssociationRegionNetworkFirewallPolicyRequest request =
           PatchAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.patchAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAssociationRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)
    
    
    public final OperationFuture<Operation,Operation> patchAssociationAsync(String project, String region, String firewallPolicy, FirewallPolicyAssociation firewallPolicyAssociationResource)

Updates an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyAssociation firewallPolicyAssociationResource =
           FirewallPolicyAssociation.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .patchAssociationAsync(
                   project, region, firewallPolicy, firewallPolicyAssociationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyAssociationResource` | `[FirewallPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyAssociation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAssociationCallable()
    
    
    public final UnaryCallable<PatchAssociationRegionNetworkFirewallPolicyRequest,Operation> patchAssociationCallable()

Updates an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchAssociationRegionNetworkFirewallPolicyRequest request =
           PatchAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.patchAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAssociationOperationCallable()
    
    
    public final OperationCallable<PatchAssociationRegionNetworkFirewallPolicyRequest,Operation,Operation> patchAssociationOperationCallable()

Updates an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchAssociationRegionNetworkFirewallPolicyRequest request =
           PatchAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyAssociationResource(FirewallPolicyAssociation.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient
               .patchAssociationOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(PatchRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionNetworkFirewallPolicyRequest request)

Patches the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRegionNetworkFirewallPolicyRequest request =
           PatchRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String firewallPolicy, FirewallPolicy firewallPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String firewallPolicy, FirewallPolicy firewallPolicyResource)

Patches the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicy firewallPolicyResource = FirewallPolicy.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .patchAsync(project, region, firewallPolicy, firewallPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyResource` | `[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionNetworkFirewallPolicyRequest,Operation> patchCallable()

Patches the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRegionNetworkFirewallPolicyRequest request =
           PatchRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionNetworkFirewallPolicyRequest,Operation,Operation> patchOperationCallable()

Patches the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRegionNetworkFirewallPolicyRequest request =
           PatchRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyResource(FirewallPolicy.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(PatchRuleRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(PatchRuleRegionNetworkFirewallPolicyRequest request)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRuleRegionNetworkFirewallPolicyRequest request =
           PatchRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.patchRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(String project, String region, String firewallPolicy, FirewallPolicyRule firewallPolicyRuleResource)

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       FirewallPolicyRule firewallPolicyRuleResource = FirewallPolicyRule.newBuilder().build();
       Operation response =
           regionNetworkFirewallPoliciesClient
               .patchRuleAsync(project, region, firewallPolicy, firewallPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
`firewallPolicyRuleResource` | `[FirewallPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FirewallPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleCallable()
    
    
    public final UnaryCallable<PatchRuleRegionNetworkFirewallPolicyRequest,Operation> patchRuleCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRuleRegionNetworkFirewallPolicyRequest request =
           PatchRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.patchRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleOperationCallable()
    
    
    public final OperationCallable<PatchRuleRegionNetworkFirewallPolicyRequest,Operation,Operation> patchRuleOperationCallable()

Patches a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       PatchRuleRegionNetworkFirewallPolicyRequest request =
           PatchRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setFirewallPolicyRuleResource(FirewallPolicyRule.newBuilder().build())
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.patchRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(RemoveAssociationRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(RemoveAssociationRegionNetworkFirewallPolicyRequest request)

Removes an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveAssociationRegionNetworkFirewallPolicyRequest request =
           RemoveAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionNetworkFirewallPoliciesClient.removeAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(String project, String region, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(String project, String region, String firewallPolicy)

Removes an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           regionNetworkFirewallPoliciesClient
               .removeAssociationAsync(project, region, firewallPolicy)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationCallable()
    
    
    public final UnaryCallable<RemoveAssociationRegionNetworkFirewallPolicyRequest,Operation> removeAssociationCallable()

Removes an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveAssociationRegionNetworkFirewallPolicyRequest request =
           RemoveAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.removeAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationOperationCallable()
    
    
    public final OperationCallable<RemoveAssociationRegionNetworkFirewallPolicyRequest,Operation,Operation> removeAssociationOperationCallable()

Removes an association for the specified network firewall policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveAssociationRegionNetworkFirewallPolicyRequest request =
           RemoveAssociationRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setName("name3373707")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient
               .removeAssociationOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(RemoveRuleRegionNetworkFirewallPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(RemoveRuleRegionNetworkFirewallPolicyRequest request)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveRuleRegionNetworkFirewallPolicyRequest request =
           RemoveRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkFirewallPoliciesClient.removeRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(String project, String region, String firewallPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(String project, String region, String firewallPolicy)

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String firewallPolicy = "firewallPolicy1819692626";
       Operation response =
           regionNetworkFirewallPoliciesClient
               .removeRuleAsync(project, region, firewallPolicy)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`firewallPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the firewall policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleCallable()
    
    
    public final UnaryCallable<RemoveRuleRegionNetworkFirewallPolicyRequest,Operation> removeRuleCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveRuleRegionNetworkFirewallPolicyRequest request =
           RemoveRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkFirewallPoliciesClient.removeRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleOperationCallable()
    
    
    public final OperationCallable<RemoveRuleRegionNetworkFirewallPolicyRequest,Operation,Operation> removeRuleOperationCallable()

Deletes a rule of the specified priority.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       RemoveRuleRegionNetworkFirewallPolicyRequest request =
           RemoveRuleRegionNetworkFirewallPolicyRequest.newBuilder()
               .setFirewallPolicy("firewallPolicy1819692626")
               .setPriority(-1165461084)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkFirewallPoliciesClient.removeRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleRegionNetworkFirewallPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyRegionNetworkFirewallPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRegionNetworkFirewallPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       SetIamPolicyRegionNetworkFirewallPolicyRequest request =
           SetIamPolicyRegionNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = regionNetworkFirewallPoliciesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetPolicyRequest regionSetPolicyRequestResource =
           RegionSetPolicyRequest.newBuilder().build();
       Policy response =
           regionNetworkFirewallPoliciesClient.setIamPolicy(
               project, region, resource, regionSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRegionNetworkFirewallPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       SetIamPolicyRegionNetworkFirewallPolicyRequest request =
           SetIamPolicyRegionNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future =
           regionNetworkFirewallPoliciesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionNetworkFirewallPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionNetworkFirewallPolicyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionNetworkFirewallPolicyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       TestIamPermissionsRegionNetworkFirewallPolicyRequest request =
           TestIamPermissionsRegionNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response =
           regionNetworkFirewallPoliciesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionNetworkFirewallPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionNetworkFirewallPoliciesClient.testIamPermissions(
               project, region, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRegionNetworkFirewallPolicyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkFirewallPoliciesClient regionNetworkFirewallPoliciesClient =
         RegionNetworkFirewallPoliciesClient.create()) {
       TestIamPermissionsRegionNetworkFirewallPolicyRequest request =
           TestIamPermissionsRegionNetworkFirewallPolicyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionNetworkFirewallPoliciesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionNetworkFirewallPolicyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
