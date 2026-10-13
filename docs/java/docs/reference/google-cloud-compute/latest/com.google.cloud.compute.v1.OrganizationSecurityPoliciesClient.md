---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient
title: Class OrganizationSecurityPoliciesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:15.427372+00:00
---

# Class OrganizationSecurityPoliciesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrganizationSecurityPoliciesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/OrganizationSecurityPoliciesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The OrganizationSecurityPolicies API.

This client uses OrganizationSecurityPolicies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicy response = organizationSecurityPoliciesClient.get(securityPolicy);
     }
     

Note: close() needs to be called on the OrganizationSecurityPoliciesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddAssociation |  Inserts an association for the specified security policy.  This has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addAssociation instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAssociationAsync(AddAssociationOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAssociationAsync(String securityPolicy, SecurityPolicyAssociation securityPolicyAssociationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAssociationOperationCallable() 
  * addAssociationCallable() 

  
AddRule |  Inserts a rule into a security policy.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addRule instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addRuleAsync(AddRuleOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addRuleOperationCallable() 
  * addRuleCallable() 

  
CopyRules |  Copies rules to the specified security policy.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.cloneRules instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * copyRulesAsync(CopyRulesOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * copyRulesAsync(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * copyRulesOperationCallable() 
  * copyRulesCallable() 

  
Delete |  Deletes the specified policy.  Use this API to remove Cloud Armor policies. Previously, alpha and beta versions of this API were used to remove firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.delete instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  List all of the ordered rules present in a single specified policy.  Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.get instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetOrganizationSecurityPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetAssociation |  Gets an association with the specified name.  Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getAssociation instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAssociation(GetAssociationOrganizationSecurityPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAssociation(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAssociationCallable() 

  
GetRule |  Gets a rule at the specified priority.  Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getRule instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRule(GetRuleOrganizationSecurityPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRule(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRuleCallable() 

  
Insert |  Creates a new policy in the specified organization using the data included in the request.  Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(SecurityPolicy securityPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  List all the policies that have been configured for the specified organization.  Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.list instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListOrganizationSecurityPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListAssociations |  Lists associations of a specified target, i.e., organization or folder.  Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.listAssociations instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAssociations(ListAssociationsOrganizationSecurityPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAssociations() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAssociationsCallable() 

  
ListPreconfiguredExpressionSets |  Gets the current list of preconfigured Web Application Firewall (WAF) expressions. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPreconfiguredExpressionSets(ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPreconfiguredExpressionSets() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPreconfiguredExpressionSetsCallable() 

  
Move |  Moves the specified security policy.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.move instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveAsync(MoveOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveAsync(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveOperationCallable() 
  * moveCallable() 

  
Patch |  Patches the specified policy with the data included in the request.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patch instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String securityPolicy, SecurityPolicy securityPolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchRule |  Patches a rule at the specified priority.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patchRule instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchRuleAsync(PatchRuleOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchRuleOperationCallable() 
  * patchRuleCallable() 

  
RemoveAssociation |  Removes an association for the specified security policy.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeAssociation instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeAssociationAsync(RemoveAssociationOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeAssociationAsync(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeAssociationOperationCallable() 
  * removeAssociationCallable() 

  
RemoveRule |  Deletes a rule at the specified priority.  Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeRule instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeRuleAsync(RemoveRuleOrganizationSecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeRuleAsync(String securityPolicy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeRuleOperationCallable() 
  * removeRuleCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of OrganizationSecurityPoliciesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationSecurityPoliciesSettings organizationSecurityPoliciesSettings =
         OrganizationSecurityPoliciesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create(organizationSecurityPoliciesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationSecurityPoliciesSettings organizationSecurityPoliciesSettings =
         OrganizationSecurityPoliciesSettings.newBuilder().setEndpoint(myEndpoint).build();
     OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create(organizationSecurityPoliciesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrganizationSecurityPoliciesClient

## Static Methods 

### create()
    
    
    public static final OrganizationSecurityPoliciesClient create()

Constructs an instance of OrganizationSecurityPoliciesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrganizationSecurityPoliciesSettings settings)
    
    
    public static final OrganizationSecurityPoliciesClient create(OrganizationSecurityPoliciesSettings settings)

Constructs an instance of OrganizationSecurityPoliciesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrganizationSecurityPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(OrganizationSecurityPoliciesStub stub)
    
    
    public static final OrganizationSecurityPoliciesClient create(OrganizationSecurityPoliciesStub stub)

Constructs an instance of OrganizationSecurityPoliciesClient, using the given stub for making calls. This is for advanced usage - prefer using create(OrganizationSecurityPoliciesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrganizationSecurityPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.OrganizationSecurityPoliciesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient)` |   
  
## Constructors 

### OrganizationSecurityPoliciesClient(OrganizationSecurityPoliciesSettings settings)
    
    
    protected OrganizationSecurityPoliciesClient(OrganizationSecurityPoliciesSettings settings)

Constructs an instance of OrganizationSecurityPoliciesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[OrganizationSecurityPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings)`  
  
  
### OrganizationSecurityPoliciesClient(OrganizationSecurityPoliciesStub stub)
    
    
    protected OrganizationSecurityPoliciesClient(OrganizationSecurityPoliciesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrganizationSecurityPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.OrganizationSecurityPoliciesStub)`  
  
  
## Methods 

### addAssociationAsync(AddAssociationOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(AddAssociationOrganizationSecurityPolicyRequest request)

Inserts an association for the specified security policy.

This has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddAssociationOrganizationSecurityPolicyRequest request =
           AddAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyAssociationResource(SecurityPolicyAssociation.newBuilder().build())
               .build();
       Operation response = organizationSecurityPoliciesClient.addAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationAsync(String securityPolicy, SecurityPolicyAssociation securityPolicyAssociationResource)
    
    
    public final OperationFuture<Operation,Operation> addAssociationAsync(String securityPolicy, SecurityPolicyAssociation securityPolicyAssociationResource)

Inserts an association for the specified security policy.

This has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicyAssociation securityPolicyAssociationResource =
           SecurityPolicyAssociation.newBuilder().build();
       Operation response =
           organizationSecurityPoliciesClient
               .addAssociationAsync(securityPolicy, securityPolicyAssociationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
`securityPolicyAssociationResource` | `[SecurityPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyAssociation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationCallable()
    
    
    public final UnaryCallable<AddAssociationOrganizationSecurityPolicyRequest,Operation> addAssociationCallable()

Inserts an association for the specified security policy.

This has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddAssociationOrganizationSecurityPolicyRequest request =
           AddAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyAssociationResource(SecurityPolicyAssociation.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.addAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationOperationCallable()
    
    
    public final OperationCallable<AddAssociationOrganizationSecurityPolicyRequest,Operation,Operation> addAssociationOperationCallable()

Inserts an association for the specified security policy.

This has billing implications. Projects in the hierarchy with effective hierarchical security policies will be automatically enrolled into Cloud Armor Enterprise if not already enrolled.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddAssociationOrganizationSecurityPolicyRequest request =
           AddAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setReplaceExistingAssociation(true)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyAssociationResource(SecurityPolicyAssociation.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.addAssociationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(AddRuleOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(AddRuleOrganizationSecurityPolicyRequest request)

Inserts a rule into a security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddRuleOrganizationSecurityPolicyRequest request =
           AddRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       Operation response = organizationSecurityPoliciesClient.addRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> addRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource)

Inserts a rule into a security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicyRule securityPolicyRuleResource = SecurityPolicyRule.newBuilder().build();
       Operation response =
           organizationSecurityPoliciesClient
               .addRuleAsync(securityPolicy, securityPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
`securityPolicyRuleResource` | `[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleCallable()
    
    
    public final UnaryCallable<AddRuleOrganizationSecurityPolicyRequest,Operation> addRuleCallable()

Inserts a rule into a security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddRuleOrganizationSecurityPolicyRequest request =
           AddRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.addRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleOperationCallable()
    
    
    public final OperationCallable<AddRuleOrganizationSecurityPolicyRequest,Operation,Operation> addRuleOperationCallable()

Inserts a rule into a security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.addRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       AddRuleOrganizationSecurityPolicyRequest request =
           AddRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.addRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### copyRulesAsync(CopyRulesOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> copyRulesAsync(CopyRulesOrganizationSecurityPolicyRequest request)

Copies rules to the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.cloneRules instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       CopyRulesOrganizationSecurityPolicyRequest request =
           CopyRulesOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSourceSecurityPolicy("sourceSecurityPolicy1092878733")
               .build();
       Operation response = organizationSecurityPoliciesClient.copyRulesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CopyRulesOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CopyRulesOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### copyRulesAsync(String securityPolicy)
    
    
    public final OperationFuture<Operation,Operation> copyRulesAsync(String securityPolicy)

Copies rules to the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.cloneRules instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       Operation response = organizationSecurityPoliciesClient.copyRulesAsync(securityPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### copyRulesCallable()
    
    
    public final UnaryCallable<CopyRulesOrganizationSecurityPolicyRequest,Operation> copyRulesCallable()

Copies rules to the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.cloneRules instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       CopyRulesOrganizationSecurityPolicyRequest request =
           CopyRulesOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSourceSecurityPolicy("sourceSecurityPolicy1092878733")
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.copyRulesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CopyRulesOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CopyRulesOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### copyRulesOperationCallable()
    
    
    public final OperationCallable<CopyRulesOrganizationSecurityPolicyRequest,Operation,Operation> copyRulesOperationCallable()

Copies rules to the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.cloneRules instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       CopyRulesOrganizationSecurityPolicyRequest request =
           CopyRulesOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSourceSecurityPolicy("sourceSecurityPolicy1092878733")
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.copyRulesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CopyRulesOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CopyRulesOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteOrganizationSecurityPolicyRequest request)

Deletes the specified policy.

Use this API to remove Cloud Armor policies. Previously, alpha and beta versions of this API were used to remove firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.delete instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       DeleteOrganizationSecurityPolicyRequest request =
           DeleteOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       Operation response = organizationSecurityPoliciesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String securityPolicy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String securityPolicy)

Deletes the specified policy.

Use this API to remove Cloud Armor policies. Previously, alpha and beta versions of this API were used to remove firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.delete instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       Operation response = organizationSecurityPoliciesClient.deleteAsync(securityPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteOrganizationSecurityPolicyRequest,Operation> deleteCallable()

Deletes the specified policy.

Use this API to remove Cloud Armor policies. Previously, alpha and beta versions of this API were used to remove firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.delete instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       DeleteOrganizationSecurityPolicyRequest request =
           DeleteOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteOrganizationSecurityPolicyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified policy.

Use this API to remove Cloud Armor policies. Previously, alpha and beta versions of this API were used to remove firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.delete instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       DeleteOrganizationSecurityPolicyRequest request =
           DeleteOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetOrganizationSecurityPolicyRequest request)
    
    
    public final SecurityPolicy get(GetOrganizationSecurityPolicyRequest request)

List all of the ordered rules present in a single specified policy.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.get instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetOrganizationSecurityPolicyRequest request =
           GetOrganizationSecurityPolicyRequest.newBuilder()
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       SecurityPolicy response = organizationSecurityPoliciesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)` |   
  
### get(String securityPolicy)
    
    
    public final SecurityPolicy get(String securityPolicy)

List all of the ordered rules present in a single specified policy.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.get instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicy response = organizationSecurityPoliciesClient.get(securityPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to get.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)` |   
  
### getAssociation(GetAssociationOrganizationSecurityPolicyRequest request)
    
    
    public final SecurityPolicyAssociation getAssociation(GetAssociationOrganizationSecurityPolicyRequest request)

Gets an association with the specified name.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetAssociationOrganizationSecurityPolicyRequest request =
           GetAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setName("name3373707")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       SecurityPolicyAssociation response =
           organizationSecurityPoliciesClient.getAssociation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyAssociation)` |   
  
### getAssociation(String securityPolicy)
    
    
    public final SecurityPolicyAssociation getAssociation(String securityPolicy)

Gets an association with the specified name.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicyAssociation response =
           organizationSecurityPoliciesClient.getAssociation(securityPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyAssociation)` |   
  
### getAssociationCallable()
    
    
    public final UnaryCallable<GetAssociationOrganizationSecurityPolicyRequest,SecurityPolicyAssociation> getAssociationCallable()

Gets an association with the specified name.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetAssociationOrganizationSecurityPolicyRequest request =
           GetAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setName("name3373707")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<SecurityPolicyAssociation> future =
           organizationSecurityPoliciesClient.getAssociationCallable().futureCall(request);
       // Do something.
       SecurityPolicyAssociation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationOrganizationSecurityPolicyRequest),[SecurityPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyAssociation)>` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetOrganizationSecurityPolicyRequest,SecurityPolicy> getCallable()

List all of the ordered rules present in a single specified policy.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.get instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetOrganizationSecurityPolicyRequest request =
           GetOrganizationSecurityPolicyRequest.newBuilder()
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<SecurityPolicy> future =
           organizationSecurityPoliciesClient.getCallable().futureCall(request);
       // Do something.
       SecurityPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOrganizationSecurityPolicyRequest),[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)>` |   
  
### getRule(GetRuleOrganizationSecurityPolicyRequest request)
    
    
    public final SecurityPolicyRule getRule(GetRuleOrganizationSecurityPolicyRequest request)

Gets a rule at the specified priority.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetRuleOrganizationSecurityPolicyRequest request =
           GetRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       SecurityPolicyRule response = organizationSecurityPoliciesClient.getRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)` |   
  
### getRule(String securityPolicy)
    
    
    public final SecurityPolicyRule getRule(String securityPolicy)

Gets a rule at the specified priority.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicyRule response = organizationSecurityPoliciesClient.getRule(securityPolicy);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to which the queried rule belongs.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)` |   
  
### getRuleCallable()
    
    
    public final UnaryCallable<GetRuleOrganizationSecurityPolicyRequest,SecurityPolicyRule> getRuleCallable()

Gets a rule at the specified priority.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.getRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       GetRuleOrganizationSecurityPolicyRequest request =
           GetRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<SecurityPolicyRule> future =
           organizationSecurityPoliciesClient.getRuleCallable().futureCall(request);
       // Do something.
       SecurityPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleOrganizationSecurityPolicyRequest),[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)>` |   
  
### getSettings()
    
    
    public final @Nullable OrganizationSecurityPoliciesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings` |   
  
### getStub()
    
    
    public OrganizationSecurityPoliciesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.OrganizationSecurityPoliciesStub)` |   
  
### insertAsync(InsertOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertOrganizationSecurityPolicyRequest request)

Creates a new policy in the specified organization using the data included in the request.

Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       InsertOrganizationSecurityPolicyRequest request =
           InsertOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       Operation response = organizationSecurityPoliciesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(SecurityPolicy securityPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(SecurityPolicy securityPolicyResource)

Creates a new policy in the specified organization using the data included in the request.

Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       SecurityPolicy securityPolicyResource = SecurityPolicy.newBuilder().build();
       Operation response =
           organizationSecurityPoliciesClient.insertAsync(securityPolicyResource).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicyResource` | `[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertOrganizationSecurityPolicyRequest,Operation> insertCallable()

Creates a new policy in the specified organization using the data included in the request.

Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       InsertOrganizationSecurityPolicyRequest request =
           InsertOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertOrganizationSecurityPolicyRequest,Operation,Operation> insertOperationCallable()

Creates a new policy in the specified organization using the data included in the request.

Use this API to add Cloud Armor policies. Previously, alpha and beta versions of this API were used to add firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.insert instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       InsertOrganizationSecurityPolicyRequest request =
           InsertOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
    
    
    public final OrganizationSecurityPoliciesClient.ListPagedResponse list()

List all the policies that have been configured for the specified organization.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.list instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       for (SecurityPolicy element : organizationSecurityPoliciesClient.list().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient.ListPagedResponse)` |   
  
### list(ListOrganizationSecurityPoliciesRequest request)
    
    
    public final OrganizationSecurityPoliciesClient.ListPagedResponse list(ListOrganizationSecurityPoliciesRequest request)

List all the policies that have been configured for the specified organization.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.list instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListOrganizationSecurityPoliciesRequest request =
           ListOrganizationSecurityPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       for (SecurityPolicy element : organizationSecurityPoliciesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListOrganizationSecurityPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient.ListPagedResponse)` |   
  
### listAssociations()
    
    
    public final OrganizationSecurityPoliciesListAssociationsResponse listAssociations()

Lists associations of a specified target, i.e., organization or folder.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.listAssociations instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       OrganizationSecurityPoliciesListAssociationsResponse response =
           organizationSecurityPoliciesClient.listAssociations();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesListAssociationsResponse)` |   
  
### listAssociations(ListAssociationsOrganizationSecurityPolicyRequest request)
    
    
    public final OrganizationSecurityPoliciesListAssociationsResponse listAssociations(ListAssociationsOrganizationSecurityPolicyRequest request)

Lists associations of a specified target, i.e., organization or folder.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.listAssociations instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListAssociationsOrganizationSecurityPolicyRequest request =
           ListAssociationsOrganizationSecurityPolicyRequest.newBuilder()
               .setTargetResource("targetResource-1933150017")
               .build();
       OrganizationSecurityPoliciesListAssociationsResponse response =
           organizationSecurityPoliciesClient.listAssociations(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssociationsOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAssociationsOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesListAssociationsResponse)` |   
  
### listAssociationsCallable()
    
    
    public final UnaryCallable<ListAssociationsOrganizationSecurityPolicyRequest,OrganizationSecurityPoliciesListAssociationsResponse> listAssociationsCallable()

Lists associations of a specified target, i.e., organization or folder.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.listAssociations instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListAssociationsOrganizationSecurityPolicyRequest request =
           ListAssociationsOrganizationSecurityPolicyRequest.newBuilder()
               .setTargetResource("targetResource-1933150017")
               .build();
       ApiFuture<OrganizationSecurityPoliciesListAssociationsResponse> future =
           organizationSecurityPoliciesClient.listAssociationsCallable().futureCall(request);
       // Do something.
       OrganizationSecurityPoliciesListAssociationsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssociationsOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAssociationsOrganizationSecurityPolicyRequest),[OrganizationSecurityPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesListAssociationsResponse)>` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListOrganizationSecurityPoliciesRequest,SecurityPolicyList> listCallable()

List all the policies that have been configured for the specified organization.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.list instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListOrganizationSecurityPoliciesRequest request =
           ListOrganizationSecurityPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       while (true) {
         SecurityPolicyList response =
             organizationSecurityPoliciesClient.listCallable().call(request);
         for (SecurityPolicy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListOrganizationSecurityPoliciesRequest),[SecurityPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListOrganizationSecurityPoliciesRequest,OrganizationSecurityPoliciesClient.ListPagedResponse> listPagedCallable()

List all the policies that have been configured for the specified organization.

Use this API to read Cloud Armor policies. Previously, alpha and beta versions of this API were used to read firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.list instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListOrganizationSecurityPoliciesRequest request =
           ListOrganizationSecurityPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<SecurityPolicy> future =
           organizationSecurityPoliciesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (SecurityPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListOrganizationSecurityPoliciesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient.ListPagedResponse)>` |   
  
### listPreconfiguredExpressionSets()
    
    
    public final SecurityPoliciesListPreconfiguredExpressionSetsResponse listPreconfiguredExpressionSets()

Gets the current list of preconfigured Web Application Firewall (WAF) expressions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       SecurityPoliciesListPreconfiguredExpressionSetsResponse response =
           organizationSecurityPoliciesClient.listPreconfiguredExpressionSets();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[SecurityPoliciesListPreconfiguredExpressionSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPoliciesListPreconfiguredExpressionSetsResponse)` |   
  
### listPreconfiguredExpressionSets(ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest request)
    
    
    public final SecurityPoliciesListPreconfiguredExpressionSetsResponse listPreconfiguredExpressionSets(ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest request)

Gets the current list of preconfigured Web Application Firewall (WAF) expressions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest request =
           ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       SecurityPoliciesListPreconfiguredExpressionSetsResponse response =
           organizationSecurityPoliciesClient.listPreconfiguredExpressionSets(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPoliciesListPreconfiguredExpressionSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPoliciesListPreconfiguredExpressionSetsResponse)` |   
  
### listPreconfiguredExpressionSetsCallable()
    
    
    public final UnaryCallable<ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,SecurityPoliciesListPreconfiguredExpressionSetsResponse> listPreconfiguredExpressionSetsCallable()

Gets the current list of preconfigured Web Application Firewall (WAF) expressions.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest request =
           ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentId("parentId1175162725")
               .build();
       ApiFuture<SecurityPoliciesListPreconfiguredExpressionSetsResponse> future =
           organizationSecurityPoliciesClient
               .listPreconfiguredExpressionSetsCallable()
               .futureCall(request);
       // Do something.
       SecurityPoliciesListPreconfiguredExpressionSetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest),[SecurityPoliciesListPreconfiguredExpressionSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPoliciesListPreconfiguredExpressionSetsResponse)>` |   
  
### moveAsync(MoveOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> moveAsync(MoveOrganizationSecurityPolicyRequest request)

Moves the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.move instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       MoveOrganizationSecurityPolicyRequest request =
           MoveOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       Operation response = organizationSecurityPoliciesClient.moveAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveAsync(String securityPolicy)
    
    
    public final OperationFuture<Operation,Operation> moveAsync(String securityPolicy)

Moves the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.move instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       Operation response = organizationSecurityPoliciesClient.moveAsync(securityPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveCallable()
    
    
    public final UnaryCallable<MoveOrganizationSecurityPolicyRequest,Operation> moveCallable()

Moves the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.move instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       MoveOrganizationSecurityPolicyRequest request =
           MoveOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.moveCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveOperationCallable()
    
    
    public final OperationCallable<MoveOrganizationSecurityPolicyRequest,Operation,Operation> moveOperationCallable()

Moves the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.move instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       MoveOrganizationSecurityPolicyRequest request =
           MoveOrganizationSecurityPolicyRequest.newBuilder()
               .setParentId("parentId1175162725")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.moveOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(PatchOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchOrganizationSecurityPolicyRequest request)

Patches the specified policy with the data included in the request.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patch instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchOrganizationSecurityPolicyRequest request =
           PatchOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       Operation response = organizationSecurityPoliciesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String securityPolicy, SecurityPolicy securityPolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String securityPolicy, SecurityPolicy securityPolicyResource)

Patches the specified policy with the data included in the request.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patch instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicy securityPolicyResource = SecurityPolicy.newBuilder().build();
       Operation response =
           organizationSecurityPoliciesClient
               .patchAsync(securityPolicy, securityPolicyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
`securityPolicyResource` | `[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchOrganizationSecurityPolicyRequest,Operation> patchCallable()

Patches the specified policy with the data included in the request.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patch instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchOrganizationSecurityPolicyRequest request =
           PatchOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchOrganizationSecurityPolicyRequest,Operation,Operation> patchOperationCallable()

Patches the specified policy with the data included in the request.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patch instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchOrganizationSecurityPolicyRequest request =
           PatchOrganizationSecurityPolicyRequest.newBuilder()
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyResource(SecurityPolicy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(PatchRuleOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(PatchRuleOrganizationSecurityPolicyRequest request)

Patches a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patchRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchRuleOrganizationSecurityPolicyRequest request =
           PatchRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       Operation response = organizationSecurityPoliciesClient.patchRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource)
    
    
    public final OperationFuture<Operation,Operation> patchRuleAsync(String securityPolicy, SecurityPolicyRule securityPolicyRuleResource)

Patches a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patchRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       SecurityPolicyRule securityPolicyRuleResource = SecurityPolicyRule.newBuilder().build();
       Operation response =
           organizationSecurityPoliciesClient
               .patchRuleAsync(securityPolicy, securityPolicyRuleResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
`securityPolicyRuleResource` | `[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleCallable()
    
    
    public final UnaryCallable<PatchRuleOrganizationSecurityPolicyRequest,Operation> patchRuleCallable()

Patches a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patchRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchRuleOrganizationSecurityPolicyRequest request =
           PatchRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.patchRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleOperationCallable()
    
    
    public final OperationCallable<PatchRuleOrganizationSecurityPolicyRequest,Operation,Operation> patchRuleOperationCallable()

Patches a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.patchRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       PatchRuleOrganizationSecurityPolicyRequest request =
           PatchRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .setSecurityPolicyRuleResource(SecurityPolicyRule.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.patchRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(RemoveAssociationOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(RemoveAssociationOrganizationSecurityPolicyRequest request)

Removes an association for the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveAssociationOrganizationSecurityPolicyRequest request =
           RemoveAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       Operation response = organizationSecurityPoliciesClient.removeAssociationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationAsync(String securityPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeAssociationAsync(String securityPolicy)

Removes an association for the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       Operation response =
           organizationSecurityPoliciesClient.removeAssociationAsync(securityPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationCallable()
    
    
    public final UnaryCallable<RemoveAssociationOrganizationSecurityPolicyRequest,Operation> removeAssociationCallable()

Removes an association for the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveAssociationOrganizationSecurityPolicyRequest request =
           RemoveAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.removeAssociationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationOperationCallable()
    
    
    public final OperationCallable<RemoveAssociationOrganizationSecurityPolicyRequest,Operation,Operation> removeAssociationOperationCallable()

Removes an association for the specified security policy.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeAssociation instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveAssociationOrganizationSecurityPolicyRequest request =
           RemoveAssociationOrganizationSecurityPolicyRequest.newBuilder()
               .setName("name3373707")
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient
               .removeAssociationOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(RemoveRuleOrganizationSecurityPolicyRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(RemoveRuleOrganizationSecurityPolicyRequest request)

Deletes a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveRuleOrganizationSecurityPolicyRequest request =
           RemoveRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       Operation response = organizationSecurityPoliciesClient.removeRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleOrganizationSecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleAsync(String securityPolicy)
    
    
    public final OperationFuture<Operation,Operation> removeRuleAsync(String securityPolicy)

Deletes a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       String securityPolicy = "securityPolicy-788621166";
       Operation response = organizationSecurityPoliciesClient.removeRuleAsync(securityPolicy).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`securityPolicy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the security policy to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleCallable()
    
    
    public final UnaryCallable<RemoveRuleOrganizationSecurityPolicyRequest,Operation> removeRuleCallable()

Deletes a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveRuleOrganizationSecurityPolicyRequest request =
           RemoveRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       ApiFuture<Operation> future =
           organizationSecurityPoliciesClient.removeRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleOperationCallable()
    
    
    public final OperationCallable<RemoveRuleOrganizationSecurityPolicyRequest,Operation,Operation> removeRuleOperationCallable()

Deletes a rule at the specified priority.

Use this API to modify Cloud Armor policies. Previously, alpha and beta versions of this API were used to modify firewall policies. This usage is now disabled for most organizations. Use firewallPolicies.removeRule instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (OrganizationSecurityPoliciesClient organizationSecurityPoliciesClient =
         OrganizationSecurityPoliciesClient.create()) {
       RemoveRuleOrganizationSecurityPolicyRequest request =
           RemoveRuleOrganizationSecurityPolicyRequest.newBuilder()
               .setPriority(-1165461084)
               .setRequestId("requestId693933066")
               .setSecurityPolicy("securityPolicy-788621166")
               .build();
       OperationFuture<Operation, Operation> future =
           organizationSecurityPoliciesClient.removeRuleOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
