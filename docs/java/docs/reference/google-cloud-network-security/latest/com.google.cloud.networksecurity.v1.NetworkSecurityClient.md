---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient
title: Class NetworkSecurityClient (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:01.349200+00:00
---

# Class NetworkSecurityClient (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkSecurityClient (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-network-security/google-cloud-network-security/src/main/java/com/google/cloud/networksecurity/v1/NetworkSecurityClient.java)| [Product Reference](https://cloud.google.com/traffic-director/docs/reference/network-security/rest)  
---|---  
  
Service Description: Network Security API provides resources to configure authentication and authorization policies. Refer to per API resource documentation for more information.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthorizationPolicyName name =
           AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]");
       AuthorizationPolicy response = networkSecurityClient.getAuthorizationPolicy(name);
     }
     

Note: close() needs to be called on the NetworkSecurityClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAuthorizationPolicies |  Lists AuthorizationPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthorizationPolicies(ListAuthorizationPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthorizationPolicies(LocationName parent) 
  * listAuthorizationPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthorizationPoliciesPagedCallable() 
  * listAuthorizationPoliciesCallable() 

  
GetAuthorizationPolicy |  Gets details of a single AuthorizationPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthorizationPolicy(GetAuthorizationPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthorizationPolicy(AuthorizationPolicyName name) 
  * getAuthorizationPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthorizationPolicyCallable() 

  
CreateAuthorizationPolicy |  Creates a new AuthorizationPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAuthorizationPolicyAsync(LocationName parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId) 
  * createAuthorizationPolicyAsync(String parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAuthorizationPolicyOperationCallable() 
  * createAuthorizationPolicyCallable() 

  
UpdateAuthorizationPolicy |  Updates the parameters of a single AuthorizationPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAuthorizationPolicyAsync(AuthorizationPolicy authorizationPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAuthorizationPolicyOperationCallable() 
  * updateAuthorizationPolicyCallable() 

  
DeleteAuthorizationPolicy |  Deletes a single AuthorizationPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAuthorizationPolicyAsync(AuthorizationPolicyName name) 
  * deleteAuthorizationPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthorizationPolicyOperationCallable() 
  * deleteAuthorizationPolicyCallable() 

  
ListBackendAuthenticationConfigs |  Lists BackendAuthenticationConfigs in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackendAuthenticationConfigs(LocationName parent) 
  * listBackendAuthenticationConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackendAuthenticationConfigsPagedCallable() 
  * listBackendAuthenticationConfigsCallable() 

  
GetBackendAuthenticationConfig |  Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackendAuthenticationConfig(BackendAuthenticationConfigName name) 
  * getBackendAuthenticationConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackendAuthenticationConfigCallable() 

  
CreateBackendAuthenticationConfig |  Creates a new BackendAuthenticationConfig in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBackendAuthenticationConfigAsync(LocationName parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId) 
  * createBackendAuthenticationConfigAsync(String parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackendAuthenticationConfigOperationCallable() 
  * createBackendAuthenticationConfigCallable() 

  
UpdateBackendAuthenticationConfig |  Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateBackendAuthenticationConfigAsync(BackendAuthenticationConfig backendAuthenticationConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackendAuthenticationConfigOperationCallable() 
  * updateBackendAuthenticationConfigCallable() 

  
DeleteBackendAuthenticationConfig |  Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackendAuthenticationConfigAsync(BackendAuthenticationConfigName name) 
  * deleteBackendAuthenticationConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackendAuthenticationConfigOperationCallable() 
  * deleteBackendAuthenticationConfigCallable() 

  
ListServerTlsPolicies |  Lists ServerTlsPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServerTlsPolicies(ListServerTlsPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServerTlsPolicies(LocationName parent) 
  * listServerTlsPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServerTlsPoliciesPagedCallable() 
  * listServerTlsPoliciesCallable() 

  
GetServerTlsPolicy |  Gets details of a single ServerTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServerTlsPolicy(GetServerTlsPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServerTlsPolicy(ServerTlsPolicyName name) 
  * getServerTlsPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServerTlsPolicyCallable() 

  
CreateServerTlsPolicy |  Creates a new ServerTlsPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServerTlsPolicyAsync(CreateServerTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServerTlsPolicyAsync(LocationName parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId) 
  * createServerTlsPolicyAsync(String parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServerTlsPolicyOperationCallable() 
  * createServerTlsPolicyCallable() 

  
UpdateServerTlsPolicy |  Updates the parameters of a single ServerTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServerTlsPolicyAsync(ServerTlsPolicy serverTlsPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServerTlsPolicyOperationCallable() 
  * updateServerTlsPolicyCallable() 

  
DeleteServerTlsPolicy |  Deletes a single ServerTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServerTlsPolicyAsync(ServerTlsPolicyName name) 
  * deleteServerTlsPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServerTlsPolicyOperationCallable() 
  * deleteServerTlsPolicyCallable() 

  
ListClientTlsPolicies |  Lists ClientTlsPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listClientTlsPolicies(ListClientTlsPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listClientTlsPolicies(LocationName parent) 
  * listClientTlsPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listClientTlsPoliciesPagedCallable() 
  * listClientTlsPoliciesCallable() 

  
GetClientTlsPolicy |  Gets details of a single ClientTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getClientTlsPolicy(GetClientTlsPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getClientTlsPolicy(ClientTlsPolicyName name) 
  * getClientTlsPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getClientTlsPolicyCallable() 

  
CreateClientTlsPolicy |  Creates a new ClientTlsPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createClientTlsPolicyAsync(CreateClientTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createClientTlsPolicyAsync(LocationName parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId) 
  * createClientTlsPolicyAsync(String parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createClientTlsPolicyOperationCallable() 
  * createClientTlsPolicyCallable() 

  
UpdateClientTlsPolicy |  Updates the parameters of a single ClientTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateClientTlsPolicyAsync(ClientTlsPolicy clientTlsPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateClientTlsPolicyOperationCallable() 
  * updateClientTlsPolicyCallable() 

  
DeleteClientTlsPolicy |  Deletes a single ClientTlsPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteClientTlsPolicyAsync(ClientTlsPolicyName name) 
  * deleteClientTlsPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteClientTlsPolicyOperationCallable() 
  * deleteClientTlsPolicyCallable() 

  
ListGatewaySecurityPolicies |  Lists GatewaySecurityPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGatewaySecurityPolicies(LocationName parent) 
  * listGatewaySecurityPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGatewaySecurityPoliciesPagedCallable() 
  * listGatewaySecurityPoliciesCallable() 

  
GetGatewaySecurityPolicy |  Gets details of a single GatewaySecurityPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGatewaySecurityPolicy(GatewaySecurityPolicyName name) 
  * getGatewaySecurityPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGatewaySecurityPolicyCallable() 

  
CreateGatewaySecurityPolicy |  Creates a new GatewaySecurityPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGatewaySecurityPolicyAsync(LocationName parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId) 
  * createGatewaySecurityPolicyAsync(String parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGatewaySecurityPolicyOperationCallable() 
  * createGatewaySecurityPolicyCallable() 

  
UpdateGatewaySecurityPolicy |  Updates the parameters of a single GatewaySecurityPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateGatewaySecurityPolicyAsync(GatewaySecurityPolicy gatewaySecurityPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGatewaySecurityPolicyOperationCallable() 
  * updateGatewaySecurityPolicyCallable() 

  
DeleteGatewaySecurityPolicy |  Deletes a single GatewaySecurityPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGatewaySecurityPolicyAsync(GatewaySecurityPolicyName name) 
  * deleteGatewaySecurityPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGatewaySecurityPolicyOperationCallable() 
  * deleteGatewaySecurityPolicyCallable() 

  
ListGatewaySecurityPolicyRules |  Lists GatewaySecurityPolicyRules in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listGatewaySecurityPolicyRules(GatewaySecurityPolicyName parent) 
  * listGatewaySecurityPolicyRules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listGatewaySecurityPolicyRulesPagedCallable() 
  * listGatewaySecurityPolicyRulesCallable() 

  
GetGatewaySecurityPolicyRule |  Gets details of a single GatewaySecurityPolicyRule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getGatewaySecurityPolicyRule(GatewaySecurityPolicyRuleName name) 
  * getGatewaySecurityPolicyRule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getGatewaySecurityPolicyRuleCallable() 

  
CreateGatewaySecurityPolicyRule |  Creates a new GatewaySecurityPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createGatewaySecurityPolicyRuleAsync(GatewaySecurityPolicyName parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId) 
  * createGatewaySecurityPolicyRuleAsync(String parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createGatewaySecurityPolicyRuleOperationCallable() 
  * createGatewaySecurityPolicyRuleCallable() 

  
UpdateGatewaySecurityPolicyRule |  Updates the parameters of a single GatewaySecurityPolicyRule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateGatewaySecurityPolicyRuleAsync(GatewaySecurityPolicyRule gatewaySecurityPolicyRule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateGatewaySecurityPolicyRuleOperationCallable() 
  * updateGatewaySecurityPolicyRuleCallable() 

  
DeleteGatewaySecurityPolicyRule |  Deletes a single GatewaySecurityPolicyRule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteGatewaySecurityPolicyRuleAsync(GatewaySecurityPolicyRuleName name) 
  * deleteGatewaySecurityPolicyRuleAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteGatewaySecurityPolicyRuleOperationCallable() 
  * deleteGatewaySecurityPolicyRuleCallable() 

  
ListUrlLists |  Lists UrlLists in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUrlLists(ListUrlListsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUrlLists(LocationName parent) 
  * listUrlLists(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUrlListsPagedCallable() 
  * listUrlListsCallable() 

  
GetUrlList |  Gets details of a single UrlList. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUrlList(GetUrlListRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUrlList(UrlListName name) 
  * getUrlList(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUrlListCallable() 

  
CreateUrlList |  Creates a new UrlList in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUrlListAsync(CreateUrlListRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createUrlListAsync(LocationName parent, UrlList urlList, String urlListId) 
  * createUrlListAsync(String parent, UrlList urlList, String urlListId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUrlListOperationCallable() 
  * createUrlListCallable() 

  
UpdateUrlList |  Updates the parameters of a single UrlList. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateUrlListAsync(UpdateUrlListRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateUrlListAsync(UrlList urlList, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateUrlListOperationCallable() 
  * updateUrlListCallable() 

  
DeleteUrlList |  Deletes a single UrlList. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUrlListAsync(DeleteUrlListRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteUrlListAsync(UrlListName name) 
  * deleteUrlListAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUrlListOperationCallable() 
  * deleteUrlListCallable() 

  
ListTlsInspectionPolicies |  Lists TlsInspectionPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTlsInspectionPolicies(ListTlsInspectionPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTlsInspectionPolicies(LocationName parent) 
  * listTlsInspectionPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTlsInspectionPoliciesPagedCallable() 
  * listTlsInspectionPoliciesCallable() 

  
GetTlsInspectionPolicy |  Gets details of a single TlsInspectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTlsInspectionPolicy(GetTlsInspectionPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTlsInspectionPolicy(TlsInspectionPolicyName name) 
  * getTlsInspectionPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTlsInspectionPolicyCallable() 

  
CreateTlsInspectionPolicy |  Creates a new TlsInspectionPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTlsInspectionPolicyAsync(LocationName parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId) 
  * createTlsInspectionPolicyAsync(String parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTlsInspectionPolicyOperationCallable() 
  * createTlsInspectionPolicyCallable() 

  
UpdateTlsInspectionPolicy |  Updates the parameters of a single TlsInspectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTlsInspectionPolicyAsync(TlsInspectionPolicy tlsInspectionPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTlsInspectionPolicyOperationCallable() 
  * updateTlsInspectionPolicyCallable() 

  
DeleteTlsInspectionPolicy |  Deletes a single TlsInspectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTlsInspectionPolicyAsync(TlsInspectionPolicyName name) 
  * deleteTlsInspectionPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTlsInspectionPolicyOperationCallable() 
  * deleteTlsInspectionPolicyCallable() 

  
ListAuthzPolicies |  Lists AuthzPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthzPolicies(ListAuthzPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthzPolicies(LocationName parent) 
  * listAuthzPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthzPoliciesPagedCallable() 
  * listAuthzPoliciesCallable() 

  
GetAuthzPolicy |  Gets details of a single AuthzPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthzPolicy(GetAuthzPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthzPolicy(AuthzPolicyName name) 
  * getAuthzPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthzPolicyCallable() 

  
CreateAuthzPolicy |  Creates a new AuthzPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAuthzPolicyAsync(CreateAuthzPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAuthzPolicyAsync(LocationName parent, AuthzPolicy authzPolicy, String authzPolicyId) 
  * createAuthzPolicyAsync(String parent, AuthzPolicy authzPolicy, String authzPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAuthzPolicyOperationCallable() 
  * createAuthzPolicyCallable() 

  
UpdateAuthzPolicy |  Updates the parameters of a single AuthzPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAuthzPolicyAsync(UpdateAuthzPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAuthzPolicyAsync(AuthzPolicy authzPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAuthzPolicyOperationCallable() 
  * updateAuthzPolicyCallable() 

  
DeleteAuthzPolicy |  Deletes a single AuthzPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthzPolicyAsync(DeleteAuthzPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAuthzPolicyAsync(AuthzPolicyName name) 
  * deleteAuthzPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthzPolicyOperationCallable() 
  * deleteAuthzPolicyCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworkSecuritySettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkSecuritySettings networkSecuritySettings =
         NetworkSecuritySettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkSecurityClient networkSecurityClient =
         NetworkSecurityClient.create(networkSecuritySettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkSecuritySettings networkSecuritySettings =
         NetworkSecuritySettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkSecurityClient networkSecurityClient =
         NetworkSecurityClient.create(networkSecuritySettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkSecurityClient

## Static Methods 

### create()
    
    
    public static final NetworkSecurityClient create()

Constructs an instance of NetworkSecurityClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkSecuritySettings settings)
    
    
    public static final NetworkSecurityClient create(NetworkSecuritySettings settings)

Constructs an instance of NetworkSecurityClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkSecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecuritySettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkSecurityStub stub)
    
    
    public static final NetworkSecurityClient create(NetworkSecurityStub stub)

Constructs an instance of NetworkSecurityClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkSecuritySettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkSecurityStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.stub.NetworkSecurityStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient)` |   
  
## Constructors 

### NetworkSecurityClient(NetworkSecuritySettings settings)
    
    
    protected NetworkSecurityClient(NetworkSecuritySettings settings)

Constructs an instance of NetworkSecurityClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkSecuritySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecuritySettings)`  
  
  
### NetworkSecurityClient(NetworkSecurityStub stub)
    
    
    protected NetworkSecurityClient(NetworkSecurityStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkSecurityStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.stub.NetworkSecurityStub)`  
  
  
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

### createAuthorizationPolicyAsync(@Nullable LocationName parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId)
    
    
    public final OperationFuture<AuthorizationPolicy,OperationMetadata> createAuthorizationPolicyAsync(@Nullable LocationName parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId)

Creates a new AuthorizationPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AuthorizationPolicy authorizationPolicy = AuthorizationPolicy.newBuilder().build();
       String authorizationPolicyId = "authorizationPolicyId1314252166";
       AuthorizationPolicy response =
           networkSecurityClient
               .createAuthorizationPolicyAsync(parent, authorizationPolicy, authorizationPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the AuthorizationPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`authorizationPolicy` | `[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)`  
Required. AuthorizationPolicy resource to be created.  
`authorizationPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the AuthorizationPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "authz_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest request)
    
    
    public final OperationFuture<AuthorizationPolicy,OperationMetadata> createAuthorizationPolicyAsync(CreateAuthorizationPolicyRequest request)

Creates a new AuthorizationPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthorizationPolicyRequest request =
           CreateAuthorizationPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthorizationPolicyId("authorizationPolicyId1314252166")
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       AuthorizationPolicy response =
           networkSecurityClient.createAuthorizationPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthorizationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthorizationPolicyAsync(String parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId)
    
    
    public final OperationFuture<AuthorizationPolicy,OperationMetadata> createAuthorizationPolicyAsync(String parent, AuthorizationPolicy authorizationPolicy, String authorizationPolicyId)

Creates a new AuthorizationPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AuthorizationPolicy authorizationPolicy = AuthorizationPolicy.newBuilder().build();
       String authorizationPolicyId = "authorizationPolicyId1314252166";
       AuthorizationPolicy response =
           networkSecurityClient
               .createAuthorizationPolicyAsync(parent, authorizationPolicy, authorizationPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the AuthorizationPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`authorizationPolicy` | `[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)`  
Required. AuthorizationPolicy resource to be created.  
`authorizationPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the AuthorizationPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "authz_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthorizationPolicyCallable()
    
    
    public final UnaryCallable<CreateAuthorizationPolicyRequest,Operation> createAuthorizationPolicyCallable()

Creates a new AuthorizationPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthorizationPolicyRequest request =
           CreateAuthorizationPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthorizationPolicyId("authorizationPolicyId1314252166")
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createAuthorizationPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAuthorizationPolicyOperationCallable()
    
    
    public final OperationCallable<CreateAuthorizationPolicyRequest,AuthorizationPolicy,OperationMetadata> createAuthorizationPolicyOperationCallable()

Creates a new AuthorizationPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthorizationPolicyRequest request =
           CreateAuthorizationPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthorizationPolicyId("authorizationPolicyId1314252166")
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       OperationFuture<AuthorizationPolicy, OperationMetadata> future =
           networkSecurityClient.createAuthorizationPolicyOperationCallable().futureCall(request);
       // Do something.
       AuthorizationPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthorizationPolicyRequest),[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthzPolicyAsync(@Nullable LocationName parent, AuthzPolicy authzPolicy, String authzPolicyId)
    
    
    public final OperationFuture<AuthzPolicy,OperationMetadata> createAuthzPolicyAsync(@Nullable LocationName parent, AuthzPolicy authzPolicy, String authzPolicyId)

Creates a new AuthzPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AuthzPolicy authzPolicy = AuthzPolicy.newBuilder().build();
       String authzPolicyId = "authzPolicyId1717400543";
       AuthzPolicy response =
           networkSecurityClient.createAuthzPolicyAsync(parent, authzPolicy, authzPolicyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the `AuthzPolicy` resource. Must be in the format `projects/{project}/locations/{location}`.  
`authzPolicy` | `[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)`  
Required. `AuthzPolicy` resource to be created.  
`authzPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `AuthzPolicy` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthzPolicyAsync(CreateAuthzPolicyRequest request)
    
    
    public final OperationFuture<AuthzPolicy,OperationMetadata> createAuthzPolicyAsync(CreateAuthzPolicyRequest request)

Creates a new AuthzPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthzPolicyRequest request =
           CreateAuthzPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzPolicyId("authzPolicyId1717400543")
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthzPolicy response = networkSecurityClient.createAuthzPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthzPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthzPolicyAsync(String parent, AuthzPolicy authzPolicy, String authzPolicyId)
    
    
    public final OperationFuture<AuthzPolicy,OperationMetadata> createAuthzPolicyAsync(String parent, AuthzPolicy authzPolicy, String authzPolicyId)

Creates a new AuthzPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AuthzPolicy authzPolicy = AuthzPolicy.newBuilder().build();
       String authzPolicyId = "authzPolicyId1717400543";
       AuthzPolicy response =
           networkSecurityClient.createAuthzPolicyAsync(parent, authzPolicy, authzPolicyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `AuthzPolicy` resource. Must be in the format `projects/{project}/locations/{location}`.  
`authzPolicy` | `[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)`  
Required. `AuthzPolicy` resource to be created.  
`authzPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `AuthzPolicy` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createAuthzPolicyCallable()
    
    
    public final UnaryCallable<CreateAuthzPolicyRequest,Operation> createAuthzPolicyCallable()

Creates a new AuthzPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthzPolicyRequest request =
           CreateAuthzPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzPolicyId("authzPolicyId1717400543")
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createAuthzPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthzPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAuthzPolicyOperationCallable()
    
    
    public final OperationCallable<CreateAuthzPolicyRequest,AuthzPolicy,OperationMetadata> createAuthzPolicyOperationCallable()

Creates a new AuthzPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateAuthzPolicyRequest request =
           CreateAuthzPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzPolicyId("authzPolicyId1717400543")
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AuthzPolicy, OperationMetadata> future =
           networkSecurityClient.createAuthzPolicyOperationCallable().futureCall(request);
       // Do something.
       AuthzPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateAuthzPolicyRequest),[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createBackendAuthenticationConfigAsync(@Nullable LocationName parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId)
    
    
    public final OperationFuture<BackendAuthenticationConfig,OperationMetadata> createBackendAuthenticationConfigAsync(@Nullable LocationName parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId)

Creates a new BackendAuthenticationConfig in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BackendAuthenticationConfig backendAuthenticationConfig =
           BackendAuthenticationConfig.newBuilder().build();
       String backendAuthenticationConfigId = "backendAuthenticationConfigId-396698039";
       BackendAuthenticationConfig response =
           networkSecurityClient
               .createBackendAuthenticationConfigAsync(
                   parent, backendAuthenticationConfig, backendAuthenticationConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the BackendAuthenticationConfig. Must be in the format `projects/*/locations/{location}`.  
`backendAuthenticationConfig` | `[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)`  
Required. BackendAuthenticationConfig resource to be created.  
`backendAuthenticationConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the BackendAuthenticationConfig resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "backend-auth-config".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest request)
    
    
    public final OperationFuture<BackendAuthenticationConfig,OperationMetadata> createBackendAuthenticationConfigAsync(CreateBackendAuthenticationConfigRequest request)

Creates a new BackendAuthenticationConfig in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateBackendAuthenticationConfigRequest request =
           CreateBackendAuthenticationConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackendAuthenticationConfigId("backendAuthenticationConfigId-396698039")
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       BackendAuthenticationConfig response =
           networkSecurityClient.createBackendAuthenticationConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateBackendAuthenticationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createBackendAuthenticationConfigAsync(String parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId)
    
    
    public final OperationFuture<BackendAuthenticationConfig,OperationMetadata> createBackendAuthenticationConfigAsync(String parent, BackendAuthenticationConfig backendAuthenticationConfig, String backendAuthenticationConfigId)

Creates a new BackendAuthenticationConfig in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BackendAuthenticationConfig backendAuthenticationConfig =
           BackendAuthenticationConfig.newBuilder().build();
       String backendAuthenticationConfigId = "backendAuthenticationConfigId-396698039";
       BackendAuthenticationConfig response =
           networkSecurityClient
               .createBackendAuthenticationConfigAsync(
                   parent, backendAuthenticationConfig, backendAuthenticationConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the BackendAuthenticationConfig. Must be in the format `projects/*/locations/{location}`.  
`backendAuthenticationConfig` | `[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)`  
Required. BackendAuthenticationConfig resource to be created.  
`backendAuthenticationConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the BackendAuthenticationConfig resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "backend-auth-config".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createBackendAuthenticationConfigCallable()
    
    
    public final UnaryCallable<CreateBackendAuthenticationConfigRequest,Operation> createBackendAuthenticationConfigCallable()

Creates a new BackendAuthenticationConfig in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateBackendAuthenticationConfigRequest request =
           CreateBackendAuthenticationConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackendAuthenticationConfigId("backendAuthenticationConfigId-396698039")
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createBackendAuthenticationConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateBackendAuthenticationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackendAuthenticationConfigOperationCallable()
    
    
    public final OperationCallable<CreateBackendAuthenticationConfigRequest,BackendAuthenticationConfig,OperationMetadata> createBackendAuthenticationConfigOperationCallable()

Creates a new BackendAuthenticationConfig in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateBackendAuthenticationConfigRequest request =
           CreateBackendAuthenticationConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBackendAuthenticationConfigId("backendAuthenticationConfigId-396698039")
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       OperationFuture<BackendAuthenticationConfig, OperationMetadata> future =
           networkSecurityClient
               .createBackendAuthenticationConfigOperationCallable()
               .futureCall(request);
       // Do something.
       BackendAuthenticationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateBackendAuthenticationConfigRequest),[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createClientTlsPolicyAsync(@Nullable LocationName parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId)
    
    
    public final OperationFuture<ClientTlsPolicy,OperationMetadata> createClientTlsPolicyAsync(@Nullable LocationName parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId)

Creates a new ClientTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ClientTlsPolicy clientTlsPolicy = ClientTlsPolicy.newBuilder().build();
       String clientTlsPolicyId = "clientTlsPolicyId-188933315";
       ClientTlsPolicy response =
           networkSecurityClient
               .createClientTlsPolicyAsync(parent, clientTlsPolicy, clientTlsPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the ClientTlsPolicy. Must be in the format `projects/*/locations/{location}`.  
`clientTlsPolicy` | `[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)`  
Required. ClientTlsPolicy resource to be created.  
`clientTlsPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ClientTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "client_mtls_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createClientTlsPolicyAsync(CreateClientTlsPolicyRequest request)
    
    
    public final OperationFuture<ClientTlsPolicy,OperationMetadata> createClientTlsPolicyAsync(CreateClientTlsPolicyRequest request)

Creates a new ClientTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateClientTlsPolicyRequest request =
           CreateClientTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientTlsPolicyId("clientTlsPolicyId-188933315")
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       ClientTlsPolicy response = networkSecurityClient.createClientTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateClientTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createClientTlsPolicyAsync(String parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId)
    
    
    public final OperationFuture<ClientTlsPolicy,OperationMetadata> createClientTlsPolicyAsync(String parent, ClientTlsPolicy clientTlsPolicy, String clientTlsPolicyId)

Creates a new ClientTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ClientTlsPolicy clientTlsPolicy = ClientTlsPolicy.newBuilder().build();
       String clientTlsPolicyId = "clientTlsPolicyId-188933315";
       ClientTlsPolicy response =
           networkSecurityClient
               .createClientTlsPolicyAsync(parent, clientTlsPolicy, clientTlsPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the ClientTlsPolicy. Must be in the format `projects/*/locations/{location}`.  
`clientTlsPolicy` | `[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)`  
Required. ClientTlsPolicy resource to be created.  
`clientTlsPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ClientTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "client_mtls_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createClientTlsPolicyCallable()
    
    
    public final UnaryCallable<CreateClientTlsPolicyRequest,Operation> createClientTlsPolicyCallable()

Creates a new ClientTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateClientTlsPolicyRequest request =
           CreateClientTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientTlsPolicyId("clientTlsPolicyId-188933315")
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createClientTlsPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClientTlsPolicyOperationCallable()
    
    
    public final OperationCallable<CreateClientTlsPolicyRequest,ClientTlsPolicy,OperationMetadata> createClientTlsPolicyOperationCallable()

Creates a new ClientTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateClientTlsPolicyRequest request =
           CreateClientTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setClientTlsPolicyId("clientTlsPolicyId-188933315")
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       OperationFuture<ClientTlsPolicy, OperationMetadata> future =
           networkSecurityClient.createClientTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       ClientTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateClientTlsPolicyRequest),[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyAsync(@Nullable LocationName parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId)
    
    
    public final OperationFuture<GatewaySecurityPolicy,OperationMetadata> createGatewaySecurityPolicyAsync(@Nullable LocationName parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       GatewaySecurityPolicy gatewaySecurityPolicy = GatewaySecurityPolicy.newBuilder().build();
       String gatewaySecurityPolicyId = "gatewaySecurityPolicyId2047625137";
       GatewaySecurityPolicy response =
           networkSecurityClient
               .createGatewaySecurityPolicyAsync(
                   parent, gatewaySecurityPolicy, gatewaySecurityPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the GatewaySecurityPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`gatewaySecurityPolicy` | `[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)`  
Required. GatewaySecurityPolicy resource to be created.  
`gatewaySecurityPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the GatewaySecurityPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "gateway_security_policy1".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest request)
    
    
    public final OperationFuture<GatewaySecurityPolicy,OperationMetadata> createGatewaySecurityPolicyAsync(CreateGatewaySecurityPolicyRequest request)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRequest request =
           CreateGatewaySecurityPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewaySecurityPolicyId("gatewaySecurityPolicyId2047625137")
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       GatewaySecurityPolicy response =
           networkSecurityClient.createGatewaySecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyAsync(String parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId)
    
    
    public final OperationFuture<GatewaySecurityPolicy,OperationMetadata> createGatewaySecurityPolicyAsync(String parent, GatewaySecurityPolicy gatewaySecurityPolicy, String gatewaySecurityPolicyId)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       GatewaySecurityPolicy gatewaySecurityPolicy = GatewaySecurityPolicy.newBuilder().build();
       String gatewaySecurityPolicyId = "gatewaySecurityPolicyId2047625137";
       GatewaySecurityPolicy response =
           networkSecurityClient
               .createGatewaySecurityPolicyAsync(
                   parent, gatewaySecurityPolicy, gatewaySecurityPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the GatewaySecurityPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`gatewaySecurityPolicy` | `[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)`  
Required. GatewaySecurityPolicy resource to be created.  
`gatewaySecurityPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the GatewaySecurityPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "gateway_security_policy1".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyCallable()
    
    
    public final UnaryCallable<CreateGatewaySecurityPolicyRequest,Operation> createGatewaySecurityPolicyCallable()

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRequest request =
           CreateGatewaySecurityPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewaySecurityPolicyId("gatewaySecurityPolicyId2047625137")
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createGatewaySecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGatewaySecurityPolicyOperationCallable()
    
    
    public final OperationCallable<CreateGatewaySecurityPolicyRequest,GatewaySecurityPolicy,OperationMetadata> createGatewaySecurityPolicyOperationCallable()

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRequest request =
           CreateGatewaySecurityPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setGatewaySecurityPolicyId("gatewaySecurityPolicyId2047625137")
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       OperationFuture<GatewaySecurityPolicy, OperationMetadata> future =
           networkSecurityClient.createGatewaySecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       GatewaySecurityPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRequest),[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyRuleAsync(@Nullable GatewaySecurityPolicyName parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId)
    
    
    public final OperationFuture<GatewaySecurityPolicyRule,OperationMetadata> createGatewaySecurityPolicyRuleAsync(@Nullable GatewaySecurityPolicyName parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyName parent =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]");
       GatewaySecurityPolicyRule gatewaySecurityPolicyRule =
           GatewaySecurityPolicyRule.newBuilder().build();
       String gatewaySecurityPolicyRuleId = "gatewaySecurityPolicyRuleId-1764962099";
       GatewaySecurityPolicyRule response =
           networkSecurityClient
               .createGatewaySecurityPolicyRuleAsync(
                   parent, gatewaySecurityPolicyRule, gatewaySecurityPolicyRuleId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyName`  
Required. The parent where this rule will be created. Format : projects/{project}/location/{location}/gatewaySecurityPolicies/*  
`gatewaySecurityPolicyRule` | `[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)`  
Required. The rule to be created.  
`gatewaySecurityPolicyRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the rule, which will become the final component of the rule's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest request)
    
    
    public final OperationFuture<GatewaySecurityPolicyRule,OperationMetadata> createGatewaySecurityPolicyRuleAsync(CreateGatewaySecurityPolicyRuleRequest request)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRuleRequest request =
           CreateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .setGatewaySecurityPolicyRuleId("gatewaySecurityPolicyRuleId-1764962099")
               .build();
       GatewaySecurityPolicyRule response =
           networkSecurityClient.createGatewaySecurityPolicyRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyRuleAsync(String parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId)
    
    
    public final OperationFuture<GatewaySecurityPolicyRule,OperationMetadata> createGatewaySecurityPolicyRuleAsync(String parent, GatewaySecurityPolicyRule gatewaySecurityPolicyRule, String gatewaySecurityPolicyRuleId)

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
               .toString();
       GatewaySecurityPolicyRule gatewaySecurityPolicyRule =
           GatewaySecurityPolicyRule.newBuilder().build();
       String gatewaySecurityPolicyRuleId = "gatewaySecurityPolicyRuleId-1764962099";
       GatewaySecurityPolicyRule response =
           networkSecurityClient
               .createGatewaySecurityPolicyRuleAsync(
                   parent, gatewaySecurityPolicyRule, gatewaySecurityPolicyRuleId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent where this rule will be created. Format : projects/{project}/location/{location}/gatewaySecurityPolicies/*  
`gatewaySecurityPolicyRule` | `[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)`  
Required. The rule to be created.  
`gatewaySecurityPolicyRuleId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the rule, which will become the final component of the rule's resource name. This value should be 4-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createGatewaySecurityPolicyRuleCallable()
    
    
    public final UnaryCallable<CreateGatewaySecurityPolicyRuleRequest,Operation> createGatewaySecurityPolicyRuleCallable()

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRuleRequest request =
           CreateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .setGatewaySecurityPolicyRuleId("gatewaySecurityPolicyRuleId-1764962099")
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createGatewaySecurityPolicyRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGatewaySecurityPolicyRuleOperationCallable()
    
    
    public final OperationCallable<CreateGatewaySecurityPolicyRuleRequest,GatewaySecurityPolicyRule,OperationMetadata> createGatewaySecurityPolicyRuleOperationCallable()

Creates a new GatewaySecurityPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateGatewaySecurityPolicyRuleRequest request =
           CreateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .setGatewaySecurityPolicyRuleId("gatewaySecurityPolicyRuleId-1764962099")
               .build();
       OperationFuture<GatewaySecurityPolicyRule, OperationMetadata> future =
           networkSecurityClient
               .createGatewaySecurityPolicyRuleOperationCallable()
               .futureCall(request);
       // Do something.
       GatewaySecurityPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateGatewaySecurityPolicyRuleRequest),[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createServerTlsPolicyAsync(@Nullable LocationName parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId)
    
    
    public final OperationFuture<ServerTlsPolicy,OperationMetadata> createServerTlsPolicyAsync(@Nullable LocationName parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId)

Creates a new ServerTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServerTlsPolicy serverTlsPolicy = ServerTlsPolicy.newBuilder().build();
       String serverTlsPolicyId = "serverTlsPolicyId-1966046011";
       ServerTlsPolicy response =
           networkSecurityClient
               .createServerTlsPolicyAsync(parent, serverTlsPolicy, serverTlsPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the ServerTlsPolicy. Must be in the format `projects/*/locations/{location}`.  
`serverTlsPolicy` | `[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)`  
Required. ServerTlsPolicy resource to be created.  
`serverTlsPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServerTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "server_mtls_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createServerTlsPolicyAsync(CreateServerTlsPolicyRequest request)
    
    
    public final OperationFuture<ServerTlsPolicy,OperationMetadata> createServerTlsPolicyAsync(CreateServerTlsPolicyRequest request)

Creates a new ServerTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateServerTlsPolicyRequest request =
           CreateServerTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServerTlsPolicyId("serverTlsPolicyId-1966046011")
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       ServerTlsPolicy response = networkSecurityClient.createServerTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateServerTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createServerTlsPolicyAsync(String parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId)
    
    
    public final OperationFuture<ServerTlsPolicy,OperationMetadata> createServerTlsPolicyAsync(String parent, ServerTlsPolicy serverTlsPolicy, String serverTlsPolicyId)

Creates a new ServerTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServerTlsPolicy serverTlsPolicy = ServerTlsPolicy.newBuilder().build();
       String serverTlsPolicyId = "serverTlsPolicyId-1966046011";
       ServerTlsPolicy response =
           networkSecurityClient
               .createServerTlsPolicyAsync(parent, serverTlsPolicy, serverTlsPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the ServerTlsPolicy. Must be in the format `projects/*/locations/{location}`.  
`serverTlsPolicy` | `[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)`  
Required. ServerTlsPolicy resource to be created.  
`serverTlsPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the ServerTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "server_mtls_policy".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createServerTlsPolicyCallable()
    
    
    public final UnaryCallable<CreateServerTlsPolicyRequest,Operation> createServerTlsPolicyCallable()

Creates a new ServerTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateServerTlsPolicyRequest request =
           CreateServerTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServerTlsPolicyId("serverTlsPolicyId-1966046011")
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createServerTlsPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServerTlsPolicyOperationCallable()
    
    
    public final OperationCallable<CreateServerTlsPolicyRequest,ServerTlsPolicy,OperationMetadata> createServerTlsPolicyOperationCallable()

Creates a new ServerTlsPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateServerTlsPolicyRequest request =
           CreateServerTlsPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServerTlsPolicyId("serverTlsPolicyId-1966046011")
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       OperationFuture<ServerTlsPolicy, OperationMetadata> future =
           networkSecurityClient.createServerTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       ServerTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateServerTlsPolicyRequest),[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createTlsInspectionPolicyAsync(@Nullable LocationName parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId)
    
    
    public final OperationFuture<TlsInspectionPolicy,OperationMetadata> createTlsInspectionPolicyAsync(@Nullable LocationName parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId)

Creates a new TlsInspectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TlsInspectionPolicy tlsInspectionPolicy = TlsInspectionPolicy.newBuilder().build();
       String tlsInspectionPolicyId = "tlsInspectionPolicyId-647545892";
       TlsInspectionPolicy response =
           networkSecurityClient
               .createTlsInspectionPolicyAsync(parent, tlsInspectionPolicy, tlsInspectionPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the TlsInspectionPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`tlsInspectionPolicy` | `[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)`  
Required. TlsInspectionPolicy resource to be created.  
`tlsInspectionPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TlsInspectionPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "tls_inspection_policy1".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest request)
    
    
    public final OperationFuture<TlsInspectionPolicy,OperationMetadata> createTlsInspectionPolicyAsync(CreateTlsInspectionPolicyRequest request)

Creates a new TlsInspectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateTlsInspectionPolicyRequest request =
           CreateTlsInspectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsInspectionPolicyId("tlsInspectionPolicyId-647545892")
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       TlsInspectionPolicy response =
           networkSecurityClient.createTlsInspectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateTlsInspectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createTlsInspectionPolicyAsync(String parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId)
    
    
    public final OperationFuture<TlsInspectionPolicy,OperationMetadata> createTlsInspectionPolicyAsync(String parent, TlsInspectionPolicy tlsInspectionPolicy, String tlsInspectionPolicyId)

Creates a new TlsInspectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       TlsInspectionPolicy tlsInspectionPolicy = TlsInspectionPolicy.newBuilder().build();
       String tlsInspectionPolicyId = "tlsInspectionPolicyId-647545892";
       TlsInspectionPolicy response =
           networkSecurityClient
               .createTlsInspectionPolicyAsync(parent, tlsInspectionPolicy, tlsInspectionPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the TlsInspectionPolicy. Must be in the format `projects/{project}/locations/{location}`.  
`tlsInspectionPolicy` | `[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)`  
Required. TlsInspectionPolicy resource to be created.  
`tlsInspectionPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the TlsInspectionPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "tls_inspection_policy1".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createTlsInspectionPolicyCallable()
    
    
    public final UnaryCallable<CreateTlsInspectionPolicyRequest,Operation> createTlsInspectionPolicyCallable()

Creates a new TlsInspectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateTlsInspectionPolicyRequest request =
           CreateTlsInspectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsInspectionPolicyId("tlsInspectionPolicyId-647545892")
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createTlsInspectionPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateTlsInspectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTlsInspectionPolicyOperationCallable()
    
    
    public final OperationCallable<CreateTlsInspectionPolicyRequest,TlsInspectionPolicy,OperationMetadata> createTlsInspectionPolicyOperationCallable()

Creates a new TlsInspectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateTlsInspectionPolicyRequest request =
           CreateTlsInspectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTlsInspectionPolicyId("tlsInspectionPolicyId-647545892")
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       OperationFuture<TlsInspectionPolicy, OperationMetadata> future =
           networkSecurityClient.createTlsInspectionPolicyOperationCallable().futureCall(request);
       // Do something.
       TlsInspectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateTlsInspectionPolicyRequest),[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createUrlListAsync(@Nullable LocationName parent, UrlList urlList, String urlListId)
    
    
    public final OperationFuture<UrlList,OperationMetadata> createUrlListAsync(@Nullable LocationName parent, UrlList urlList, String urlListId)

Creates a new UrlList in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       UrlList urlList = UrlList.newBuilder().build();
       String urlListId = "urlListId-564417368";
       UrlList response = networkSecurityClient.createUrlListAsync(parent, urlList, urlListId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The parent resource of the UrlList. Must be in the format `projects/*/locations/{location}`.  
`urlList` | `[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)`  
Required. UrlList resource to be created.  
`urlListId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the UrlList resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "url_list".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createUrlListAsync(CreateUrlListRequest request)
    
    
    public final OperationFuture<UrlList,OperationMetadata> createUrlListAsync(CreateUrlListRequest request)

Creates a new UrlList in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateUrlListRequest request =
           CreateUrlListRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUrlListId("urlListId-564417368")
               .setUrlList(UrlList.newBuilder().build())
               .build();
       UrlList response = networkSecurityClient.createUrlListAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateUrlListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createUrlListAsync(String parent, UrlList urlList, String urlListId)
    
    
    public final OperationFuture<UrlList,OperationMetadata> createUrlListAsync(String parent, UrlList urlList, String urlListId)

Creates a new UrlList in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       UrlList urlList = UrlList.newBuilder().build();
       String urlListId = "urlListId-564417368";
       UrlList response = networkSecurityClient.createUrlListAsync(parent, urlList, urlListId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the UrlList. Must be in the format `projects/*/locations/{location}`.  
`urlList` | `[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)`  
Required. UrlList resource to be created.  
`urlListId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the UrlList resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "url_list".  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### createUrlListCallable()
    
    
    public final UnaryCallable<CreateUrlListRequest,Operation> createUrlListCallable()

Creates a new UrlList in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateUrlListRequest request =
           CreateUrlListRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUrlListId("urlListId-564417368")
               .setUrlList(UrlList.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.createUrlListCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateUrlListRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createUrlListOperationCallable()
    
    
    public final OperationCallable<CreateUrlListRequest,UrlList,OperationMetadata> createUrlListOperationCallable()

Creates a new UrlList in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       CreateUrlListRequest request =
           CreateUrlListRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setUrlListId("urlListId-564417368")
               .setUrlList(UrlList.newBuilder().build())
               .build();
       OperationFuture<UrlList, OperationMetadata> future =
           networkSecurityClient.createUrlListOperationCallable().futureCall(request);
       // Do something.
       UrlList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateUrlListRequest),[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthorizationPolicyAsync(@Nullable AuthorizationPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthorizationPolicyAsync(@Nullable AuthorizationPolicyName name)

Deletes a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthorizationPolicyName name =
           AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]");
       networkSecurityClient.deleteAuthorizationPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.AuthorizationPolicyName`  
Required. A name of the AuthorizationPolicy to delete. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthorizationPolicyAsync(DeleteAuthorizationPolicyRequest request)

Deletes a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthorizationPolicyRequest request =
           DeleteAuthorizationPolicyRequest.newBuilder()
               .setName(
                   AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
                       .toString())
               .build();
       networkSecurityClient.deleteAuthorizationPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthorizationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthorizationPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthorizationPolicyAsync(String name)

Deletes a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
               .toString();
       networkSecurityClient.deleteAuthorizationPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the AuthorizationPolicy to delete. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthorizationPolicyCallable()
    
    
    public final UnaryCallable<DeleteAuthorizationPolicyRequest,Operation> deleteAuthorizationPolicyCallable()

Deletes a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthorizationPolicyRequest request =
           DeleteAuthorizationPolicyRequest.newBuilder()
               .setName(
                   AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteAuthorizationPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAuthorizationPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteAuthorizationPolicyRequest,Empty,OperationMetadata> deleteAuthorizationPolicyOperationCallable()

Deletes a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthorizationPolicyRequest request =
           DeleteAuthorizationPolicyRequest.newBuilder()
               .setName(
                   AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteAuthorizationPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthorizationPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthzPolicyAsync(@Nullable AuthzPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzPolicyAsync(@Nullable AuthzPolicyName name)

Deletes a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthzPolicyName name = AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]");
       networkSecurityClient.deleteAuthzPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.AuthzPolicyName`  
Required. The name of the `AuthzPolicy` resource to delete. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthzPolicyAsync(DeleteAuthzPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzPolicyAsync(DeleteAuthzPolicyRequest request)

Deletes a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthzPolicyRequest request =
           DeleteAuthzPolicyRequest.newBuilder()
               .setName(AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       networkSecurityClient.deleteAuthzPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthzPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthzPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzPolicyAsync(String name)

Deletes a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name = AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString();
       networkSecurityClient.deleteAuthzPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `AuthzPolicy` resource to delete. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteAuthzPolicyCallable()
    
    
    public final UnaryCallable<DeleteAuthzPolicyRequest,Operation> deleteAuthzPolicyCallable()

Deletes a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthzPolicyRequest request =
           DeleteAuthzPolicyRequest.newBuilder()
               .setName(AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteAuthzPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthzPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAuthzPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteAuthzPolicyRequest,Empty,OperationMetadata> deleteAuthzPolicyOperationCallable()

Deletes a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteAuthzPolicyRequest request =
           DeleteAuthzPolicyRequest.newBuilder()
               .setName(AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteAuthzPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteAuthzPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteBackendAuthenticationConfigAsync(@Nullable BackendAuthenticationConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackendAuthenticationConfigAsync(@Nullable BackendAuthenticationConfigName name)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       BackendAuthenticationConfigName name =
           BackendAuthenticationConfigName.of(
               "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]");
       networkSecurityClient.deleteBackendAuthenticationConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.BackendAuthenticationConfigName`  
Required. A name of the BackendAuthenticationConfig to delete. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackendAuthenticationConfigAsync(DeleteBackendAuthenticationConfigRequest request)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteBackendAuthenticationConfigRequest request =
           DeleteBackendAuthenticationConfigRequest.newBuilder()
               .setName(
                   BackendAuthenticationConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       networkSecurityClient.deleteBackendAuthenticationConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteBackendAuthenticationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteBackendAuthenticationConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackendAuthenticationConfigAsync(String name)

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           BackendAuthenticationConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
               .toString();
       networkSecurityClient.deleteBackendAuthenticationConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the BackendAuthenticationConfig to delete. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteBackendAuthenticationConfigCallable()
    
    
    public final UnaryCallable<DeleteBackendAuthenticationConfigRequest,Operation> deleteBackendAuthenticationConfigCallable()

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteBackendAuthenticationConfigRequest request =
           DeleteBackendAuthenticationConfigRequest.newBuilder()
               .setName(
                   BackendAuthenticationConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteBackendAuthenticationConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteBackendAuthenticationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackendAuthenticationConfigOperationCallable()
    
    
    public final OperationCallable<DeleteBackendAuthenticationConfigRequest,Empty,OperationMetadata> deleteBackendAuthenticationConfigOperationCallable()

Deletes a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteBackendAuthenticationConfigRequest request =
           DeleteBackendAuthenticationConfigRequest.newBuilder()
               .setName(
                   BackendAuthenticationConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient
               .deleteBackendAuthenticationConfigOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteBackendAuthenticationConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteClientTlsPolicyAsync(@Nullable ClientTlsPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClientTlsPolicyAsync(@Nullable ClientTlsPolicyName name)

Deletes a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ClientTlsPolicyName name =
           ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]");
       networkSecurityClient.deleteClientTlsPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.ClientTlsPolicyName`  
Required. A name of the ClientTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClientTlsPolicyAsync(DeleteClientTlsPolicyRequest request)

Deletes a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteClientTlsPolicyRequest request =
           DeleteClientTlsPolicyRequest.newBuilder()
               .setName(
                   ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]")
                       .toString())
               .build();
       networkSecurityClient.deleteClientTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteClientTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteClientTlsPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteClientTlsPolicyAsync(String name)

Deletes a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]").toString();
       networkSecurityClient.deleteClientTlsPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ClientTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteClientTlsPolicyCallable()
    
    
    public final UnaryCallable<DeleteClientTlsPolicyRequest,Operation> deleteClientTlsPolicyCallable()

Deletes a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteClientTlsPolicyRequest request =
           DeleteClientTlsPolicyRequest.newBuilder()
               .setName(
                   ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteClientTlsPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClientTlsPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteClientTlsPolicyRequest,Empty,OperationMetadata> deleteClientTlsPolicyOperationCallable()

Deletes a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteClientTlsPolicyRequest request =
           DeleteClientTlsPolicyRequest.newBuilder()
               .setName(
                   ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteClientTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteClientTlsPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyAsync(@Nullable GatewaySecurityPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyAsync(@Nullable GatewaySecurityPolicyName name)

Deletes a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyName name =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]");
       networkSecurityClient.deleteGatewaySecurityPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyName`  
Required. A name of the GatewaySecurityPolicy to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyAsync(DeleteGatewaySecurityPolicyRequest request)

Deletes a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRequest request =
           DeleteGatewaySecurityPolicyRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .build();
       networkSecurityClient.deleteGatewaySecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyAsync(String name)

Deletes a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
               .toString();
       networkSecurityClient.deleteGatewaySecurityPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the GatewaySecurityPolicy to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyCallable()
    
    
    public final UnaryCallable<DeleteGatewaySecurityPolicyRequest,Operation> deleteGatewaySecurityPolicyCallable()

Deletes a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRequest request =
           DeleteGatewaySecurityPolicyRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteGatewaySecurityPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGatewaySecurityPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteGatewaySecurityPolicyRequest,Empty,OperationMetadata> deleteGatewaySecurityPolicyOperationCallable()

Deletes a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRequest request =
           DeleteGatewaySecurityPolicyRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteGatewaySecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyRuleAsync(@Nullable GatewaySecurityPolicyRuleName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyRuleAsync(@Nullable GatewaySecurityPolicyRuleName name)

Deletes a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyRuleName name =
           GatewaySecurityPolicyRuleName.of(
               "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]");
       networkSecurityClient.deleteGatewaySecurityPolicyRuleAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRuleName`  
Required. A name of the GatewaySecurityPolicyRule to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyRuleAsync(DeleteGatewaySecurityPolicyRuleRequest request)

Deletes a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRuleRequest request =
           DeleteGatewaySecurityPolicyRuleRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
                       .toString())
               .build();
       networkSecurityClient.deleteGatewaySecurityPolicyRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyRuleAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteGatewaySecurityPolicyRuleAsync(String name)

Deletes a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           GatewaySecurityPolicyRuleName.of(
                   "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
               .toString();
       networkSecurityClient.deleteGatewaySecurityPolicyRuleAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the GatewaySecurityPolicyRule to delete. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteGatewaySecurityPolicyRuleCallable()
    
    
    public final UnaryCallable<DeleteGatewaySecurityPolicyRuleRequest,Operation> deleteGatewaySecurityPolicyRuleCallable()

Deletes a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRuleRequest request =
           DeleteGatewaySecurityPolicyRuleRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteGatewaySecurityPolicyRuleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGatewaySecurityPolicyRuleOperationCallable()
    
    
    public final OperationCallable<DeleteGatewaySecurityPolicyRuleRequest,Empty,OperationMetadata> deleteGatewaySecurityPolicyRuleOperationCallable()

Deletes a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteGatewaySecurityPolicyRuleRequest request =
           DeleteGatewaySecurityPolicyRuleRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient
               .deleteGatewaySecurityPolicyRuleOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteGatewaySecurityPolicyRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteServerTlsPolicyAsync(@Nullable ServerTlsPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServerTlsPolicyAsync(@Nullable ServerTlsPolicyName name)

Deletes a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ServerTlsPolicyName name =
           ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]");
       networkSecurityClient.deleteServerTlsPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.ServerTlsPolicyName`  
Required. A name of the ServerTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServerTlsPolicyAsync(DeleteServerTlsPolicyRequest request)

Deletes a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteServerTlsPolicyRequest request =
           DeleteServerTlsPolicyRequest.newBuilder()
               .setName(
                   ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]")
                       .toString())
               .build();
       networkSecurityClient.deleteServerTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteServerTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteServerTlsPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServerTlsPolicyAsync(String name)

Deletes a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]").toString();
       networkSecurityClient.deleteServerTlsPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServerTlsPolicy to delete. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteServerTlsPolicyCallable()
    
    
    public final UnaryCallable<DeleteServerTlsPolicyRequest,Operation> deleteServerTlsPolicyCallable()

Deletes a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteServerTlsPolicyRequest request =
           DeleteServerTlsPolicyRequest.newBuilder()
               .setName(
                   ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteServerTlsPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServerTlsPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteServerTlsPolicyRequest,Empty,OperationMetadata> deleteServerTlsPolicyOperationCallable()

Deletes a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteServerTlsPolicyRequest request =
           DeleteServerTlsPolicyRequest.newBuilder()
               .setName(
                   ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteServerTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteServerTlsPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteTlsInspectionPolicyAsync(@Nullable TlsInspectionPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsInspectionPolicyAsync(@Nullable TlsInspectionPolicyName name)

Deletes a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       TlsInspectionPolicyName name =
           TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]");
       networkSecurityClient.deleteTlsInspectionPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.TlsInspectionPolicyName`  
Required. A name of the TlsInspectionPolicy to delete. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsInspectionPolicyAsync(DeleteTlsInspectionPolicyRequest request)

Deletes a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteTlsInspectionPolicyRequest request =
           DeleteTlsInspectionPolicyRequest.newBuilder()
               .setName(
                   TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
                       .toString())
               .setForce(true)
               .build();
       networkSecurityClient.deleteTlsInspectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteTlsInspectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteTlsInspectionPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTlsInspectionPolicyAsync(String name)

Deletes a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
               .toString();
       networkSecurityClient.deleteTlsInspectionPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TlsInspectionPolicy to delete. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteTlsInspectionPolicyCallable()
    
    
    public final UnaryCallable<DeleteTlsInspectionPolicyRequest,Operation> deleteTlsInspectionPolicyCallable()

Deletes a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteTlsInspectionPolicyRequest request =
           DeleteTlsInspectionPolicyRequest.newBuilder()
               .setName(
                   TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteTlsInspectionPolicyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteTlsInspectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTlsInspectionPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteTlsInspectionPolicyRequest,Empty,OperationMetadata> deleteTlsInspectionPolicyOperationCallable()

Deletes a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteTlsInspectionPolicyRequest request =
           DeleteTlsInspectionPolicyRequest.newBuilder()
               .setName(
                   TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
                       .toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteTlsInspectionPolicyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteTlsInspectionPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteUrlListAsync(@Nullable UrlListName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteUrlListAsync(@Nullable UrlListName name)

Deletes a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UrlListName name = UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]");
       networkSecurityClient.deleteUrlListAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.UrlListName`  
Required. A name of the UrlList to delete. Must be in the format `projects/*/locations/{location}/urlLists/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteUrlListAsync(DeleteUrlListRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteUrlListAsync(DeleteUrlListRequest request)

Deletes a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteUrlListRequest request =
           DeleteUrlListRequest.newBuilder()
               .setName(UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString())
               .build();
       networkSecurityClient.deleteUrlListAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteUrlListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteUrlListAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteUrlListAsync(String name)

Deletes a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name = UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString();
       networkSecurityClient.deleteUrlListAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the UrlList to delete. Must be in the format `projects/*/locations/{location}/urlLists/*`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### deleteUrlListCallable()
    
    
    public final UnaryCallable<DeleteUrlListRequest,Operation> deleteUrlListCallable()

Deletes a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteUrlListRequest request =
           DeleteUrlListRequest.newBuilder()
               .setName(UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.deleteUrlListCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteUrlListRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteUrlListOperationCallable()
    
    
    public final OperationCallable<DeleteUrlListRequest,Empty,OperationMetadata> deleteUrlListOperationCallable()

Deletes a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       DeleteUrlListRequest request =
           DeleteUrlListRequest.newBuilder()
               .setName(UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           networkSecurityClient.deleteUrlListOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteUrlListRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### getAuthorizationPolicy(@Nullable AuthorizationPolicyName name)
    
    
    public final AuthorizationPolicy getAuthorizationPolicy(@Nullable AuthorizationPolicyName name)

Gets details of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthorizationPolicyName name =
           AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]");
       AuthorizationPolicy response = networkSecurityClient.getAuthorizationPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.AuthorizationPolicyName`  
Required. A name of the AuthorizationPolicy to get. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)` |   
  
### getAuthorizationPolicy(GetAuthorizationPolicyRequest request)
    
    
    public final AuthorizationPolicy getAuthorizationPolicy(GetAuthorizationPolicyRequest request)

Gets details of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetAuthorizationPolicyRequest request =
           GetAuthorizationPolicyRequest.newBuilder()
               .setName(
                   AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
                       .toString())
               .build();
       AuthorizationPolicy response = networkSecurityClient.getAuthorizationPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetAuthorizationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)` |   
  
### getAuthorizationPolicy(String name)
    
    
    public final AuthorizationPolicy getAuthorizationPolicy(String name)

Gets details of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
               .toString();
       AuthorizationPolicy response = networkSecurityClient.getAuthorizationPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the AuthorizationPolicy to get. Must be in the format `projects/{project}/locations/{location}/authorizationPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)` |   
  
### getAuthorizationPolicyCallable()
    
    
    public final UnaryCallable<GetAuthorizationPolicyRequest,AuthorizationPolicy> getAuthorizationPolicyCallable()

Gets details of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetAuthorizationPolicyRequest request =
           GetAuthorizationPolicyRequest.newBuilder()
               .setName(
                   AuthorizationPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHORIZATION_POLICY]")
                       .toString())
               .build();
       ApiFuture<AuthorizationPolicy> future =
           networkSecurityClient.getAuthorizationPolicyCallable().futureCall(request);
       // Do something.
       AuthorizationPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetAuthorizationPolicyRequest),[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)>` |   
  
### getAuthzPolicy(@Nullable AuthzPolicyName name)
    
    
    public final AuthzPolicy getAuthzPolicy(@Nullable AuthzPolicyName name)

Gets details of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthzPolicyName name = AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]");
       AuthzPolicy response = networkSecurityClient.getAuthzPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.AuthzPolicyName`  
Required. A name of the `AuthzPolicy` resource to get. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)` |   
  
### getAuthzPolicy(GetAuthzPolicyRequest request)
    
    
    public final AuthzPolicy getAuthzPolicy(GetAuthzPolicyRequest request)

Gets details of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetAuthzPolicyRequest request =
           GetAuthzPolicyRequest.newBuilder()
               .setName(AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString())
               .build();
       AuthzPolicy response = networkSecurityClient.getAuthzPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetAuthzPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)` |   
  
### getAuthzPolicy(String name)
    
    
    public final AuthzPolicy getAuthzPolicy(String name)

Gets details of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name = AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString();
       AuthzPolicy response = networkSecurityClient.getAuthzPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `AuthzPolicy` resource to get. Must be in the format `projects/{project}/locations/{location}/authzPolicies/{authz_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)` |   
  
### getAuthzPolicyCallable()
    
    
    public final UnaryCallable<GetAuthzPolicyRequest,AuthzPolicy> getAuthzPolicyCallable()

Gets details of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetAuthzPolicyRequest request =
           GetAuthzPolicyRequest.newBuilder()
               .setName(AuthzPolicyName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_POLICY]").toString())
               .build();
       ApiFuture<AuthzPolicy> future =
           networkSecurityClient.getAuthzPolicyCallable().futureCall(request);
       // Do something.
       AuthzPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetAuthzPolicyRequest),[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)>` |   
  
### getBackendAuthenticationConfig(@Nullable BackendAuthenticationConfigName name)
    
    
    public final BackendAuthenticationConfig getBackendAuthenticationConfig(@Nullable BackendAuthenticationConfigName name)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       BackendAuthenticationConfigName name =
           BackendAuthenticationConfigName.of(
               "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]");
       BackendAuthenticationConfig response =
           networkSecurityClient.getBackendAuthenticationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.BackendAuthenticationConfigName`  
Required. A name of the BackendAuthenticationConfig to get. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)` |   
  
### getBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest request)
    
    
    public final BackendAuthenticationConfig getBackendAuthenticationConfig(GetBackendAuthenticationConfigRequest request)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetBackendAuthenticationConfigRequest request =
           GetBackendAuthenticationConfigRequest.newBuilder()
               .setName(
                   BackendAuthenticationConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
                       .toString())
               .build();
       BackendAuthenticationConfig response =
           networkSecurityClient.getBackendAuthenticationConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetBackendAuthenticationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)` |   
  
### getBackendAuthenticationConfig(String name)
    
    
    public final BackendAuthenticationConfig getBackendAuthenticationConfig(String name)

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           BackendAuthenticationConfigName.of(
                   "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
               .toString();
       BackendAuthenticationConfig response =
           networkSecurityClient.getBackendAuthenticationConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the BackendAuthenticationConfig to get. Must be in the format `projects/*/locations/{location}/backendAuthenticationConfigs/*`.  
**Returns**  
---  
**Type** | **Description**  
`[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)` |   
  
### getBackendAuthenticationConfigCallable()
    
    
    public final UnaryCallable<GetBackendAuthenticationConfigRequest,BackendAuthenticationConfig> getBackendAuthenticationConfigCallable()

Gets details of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetBackendAuthenticationConfigRequest request =
           GetBackendAuthenticationConfigRequest.newBuilder()
               .setName(
                   BackendAuthenticationConfigName.of(
                           "[PROJECT]", "[LOCATION]", "[BACKEND_AUTHENTICATION_CONFIG]")
                       .toString())
               .build();
       ApiFuture<BackendAuthenticationConfig> future =
           networkSecurityClient.getBackendAuthenticationConfigCallable().futureCall(request);
       // Do something.
       BackendAuthenticationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetBackendAuthenticationConfigRequest),[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)>` |   
  
### getClientTlsPolicy(@Nullable ClientTlsPolicyName name)
    
    
    public final ClientTlsPolicy getClientTlsPolicy(@Nullable ClientTlsPolicyName name)

Gets details of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ClientTlsPolicyName name =
           ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]");
       ClientTlsPolicy response = networkSecurityClient.getClientTlsPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.ClientTlsPolicyName`  
Required. A name of the ClientTlsPolicy to get. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)` |   
  
### getClientTlsPolicy(GetClientTlsPolicyRequest request)
    
    
    public final ClientTlsPolicy getClientTlsPolicy(GetClientTlsPolicyRequest request)

Gets details of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetClientTlsPolicyRequest request =
           GetClientTlsPolicyRequest.newBuilder()
               .setName(
                   ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]")
                       .toString())
               .build();
       ClientTlsPolicy response = networkSecurityClient.getClientTlsPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetClientTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)` |   
  
### getClientTlsPolicy(String name)
    
    
    public final ClientTlsPolicy getClientTlsPolicy(String name)

Gets details of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]").toString();
       ClientTlsPolicy response = networkSecurityClient.getClientTlsPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ClientTlsPolicy to get. Must be in the format `projects/*/locations/{location}/clientTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)` |   
  
### getClientTlsPolicyCallable()
    
    
    public final UnaryCallable<GetClientTlsPolicyRequest,ClientTlsPolicy> getClientTlsPolicyCallable()

Gets details of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetClientTlsPolicyRequest request =
           GetClientTlsPolicyRequest.newBuilder()
               .setName(
                   ClientTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[CLIENT_TLS_POLICY]")
                       .toString())
               .build();
       ApiFuture<ClientTlsPolicy> future =
           networkSecurityClient.getClientTlsPolicyCallable().futureCall(request);
       // Do something.
       ClientTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetClientTlsPolicyRequest),[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)>` |   
  
### getGatewaySecurityPolicy(@Nullable GatewaySecurityPolicyName name)
    
    
    public final GatewaySecurityPolicy getGatewaySecurityPolicy(@Nullable GatewaySecurityPolicyName name)

Gets details of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyName name =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]");
       GatewaySecurityPolicy response = networkSecurityClient.getGatewaySecurityPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyName`  
Required. A name of the GatewaySecurityPolicy to get. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)` |   
  
### getGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest request)
    
    
    public final GatewaySecurityPolicy getGatewaySecurityPolicy(GetGatewaySecurityPolicyRequest request)

Gets details of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetGatewaySecurityPolicyRequest request =
           GetGatewaySecurityPolicyRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .build();
       GatewaySecurityPolicy response = networkSecurityClient.getGatewaySecurityPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetGatewaySecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)` |   
  
### getGatewaySecurityPolicy(String name)
    
    
    public final GatewaySecurityPolicy getGatewaySecurityPolicy(String name)

Gets details of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
               .toString();
       GatewaySecurityPolicy response = networkSecurityClient.getGatewaySecurityPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the GatewaySecurityPolicy to get. Must be in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)` |   
  
### getGatewaySecurityPolicyCallable()
    
    
    public final UnaryCallable<GetGatewaySecurityPolicyRequest,GatewaySecurityPolicy> getGatewaySecurityPolicyCallable()

Gets details of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetGatewaySecurityPolicyRequest request =
           GetGatewaySecurityPolicyRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .build();
       ApiFuture<GatewaySecurityPolicy> future =
           networkSecurityClient.getGatewaySecurityPolicyCallable().futureCall(request);
       // Do something.
       GatewaySecurityPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetGatewaySecurityPolicyRequest),[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)>` |   
  
### getGatewaySecurityPolicyRule(@Nullable GatewaySecurityPolicyRuleName name)
    
    
    public final GatewaySecurityPolicyRule getGatewaySecurityPolicyRule(@Nullable GatewaySecurityPolicyRuleName name)

Gets details of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyRuleName name =
           GatewaySecurityPolicyRuleName.of(
               "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]");
       GatewaySecurityPolicyRule response = networkSecurityClient.getGatewaySecurityPolicyRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRuleName`  
Required. The name of the GatewaySecurityPolicyRule to retrieve. Format: projects/{project}/location/{location}/gatewaySecurityPolicies/*/rules/*  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)` |   
  
### getGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest request)
    
    
    public final GatewaySecurityPolicyRule getGatewaySecurityPolicyRule(GetGatewaySecurityPolicyRuleRequest request)

Gets details of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetGatewaySecurityPolicyRuleRequest request =
           GetGatewaySecurityPolicyRuleRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
                       .toString())
               .build();
       GatewaySecurityPolicyRule response =
           networkSecurityClient.getGatewaySecurityPolicyRule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetGatewaySecurityPolicyRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)` |   
  
### getGatewaySecurityPolicyRule(String name)
    
    
    public final GatewaySecurityPolicyRule getGatewaySecurityPolicyRule(String name)

Gets details of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           GatewaySecurityPolicyRuleName.of(
                   "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
               .toString();
       GatewaySecurityPolicyRule response = networkSecurityClient.getGatewaySecurityPolicyRule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the GatewaySecurityPolicyRule to retrieve. Format: projects/{project}/location/{location}/gatewaySecurityPolicies/*/rules/*  
**Returns**  
---  
**Type** | **Description**  
`[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)` |   
  
### getGatewaySecurityPolicyRuleCallable()
    
    
    public final UnaryCallable<GetGatewaySecurityPolicyRuleRequest,GatewaySecurityPolicyRule> getGatewaySecurityPolicyRuleCallable()

Gets details of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetGatewaySecurityPolicyRuleRequest request =
           GetGatewaySecurityPolicyRuleRequest.newBuilder()
               .setName(
                   GatewaySecurityPolicyRuleName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]", "[RULE]")
                       .toString())
               .build();
       ApiFuture<GatewaySecurityPolicyRule> future =
           networkSecurityClient.getGatewaySecurityPolicyRuleCallable().futureCall(request);
       // Do something.
       GatewaySecurityPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetGatewaySecurityPolicyRuleRequest),[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = networkSecurityClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = networkSecurityClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = networkSecurityClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = networkSecurityClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getServerTlsPolicy(@Nullable ServerTlsPolicyName name)
    
    
    public final ServerTlsPolicy getServerTlsPolicy(@Nullable ServerTlsPolicyName name)

Gets details of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ServerTlsPolicyName name =
           ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]");
       ServerTlsPolicy response = networkSecurityClient.getServerTlsPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.ServerTlsPolicyName`  
Required. A name of the ServerTlsPolicy to get. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)` |   
  
### getServerTlsPolicy(GetServerTlsPolicyRequest request)
    
    
    public final ServerTlsPolicy getServerTlsPolicy(GetServerTlsPolicyRequest request)

Gets details of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetServerTlsPolicyRequest request =
           GetServerTlsPolicyRequest.newBuilder()
               .setName(
                   ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]")
                       .toString())
               .build();
       ServerTlsPolicy response = networkSecurityClient.getServerTlsPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetServerTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)` |   
  
### getServerTlsPolicy(String name)
    
    
    public final ServerTlsPolicy getServerTlsPolicy(String name)

Gets details of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]").toString();
       ServerTlsPolicy response = networkSecurityClient.getServerTlsPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the ServerTlsPolicy to get. Must be in the format `projects/*/locations/{location}/serverTlsPolicies/*`.  
**Returns**  
---  
**Type** | **Description**  
`[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)` |   
  
### getServerTlsPolicyCallable()
    
    
    public final UnaryCallable<GetServerTlsPolicyRequest,ServerTlsPolicy> getServerTlsPolicyCallable()

Gets details of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetServerTlsPolicyRequest request =
           GetServerTlsPolicyRequest.newBuilder()
               .setName(
                   ServerTlsPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVER_TLS_POLICY]")
                       .toString())
               .build();
       ApiFuture<ServerTlsPolicy> future =
           networkSecurityClient.getServerTlsPolicyCallable().futureCall(request);
       // Do something.
       ServerTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetServerTlsPolicyRequest),[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkSecuritySettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.NetworkSecuritySettings` |   
  
### getStub()
    
    
    public NetworkSecurityStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.stub.NetworkSecurityStub)` |   
  
### getTlsInspectionPolicy(@Nullable TlsInspectionPolicyName name)
    
    
    public final TlsInspectionPolicy getTlsInspectionPolicy(@Nullable TlsInspectionPolicyName name)

Gets details of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       TlsInspectionPolicyName name =
           TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]");
       TlsInspectionPolicy response = networkSecurityClient.getTlsInspectionPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.TlsInspectionPolicyName`  
Required. A name of the TlsInspectionPolicy to get. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)` |   
  
### getTlsInspectionPolicy(GetTlsInspectionPolicyRequest request)
    
    
    public final TlsInspectionPolicy getTlsInspectionPolicy(GetTlsInspectionPolicyRequest request)

Gets details of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetTlsInspectionPolicyRequest request =
           GetTlsInspectionPolicyRequest.newBuilder()
               .setName(
                   TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
                       .toString())
               .build();
       TlsInspectionPolicy response = networkSecurityClient.getTlsInspectionPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetTlsInspectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)` |   
  
### getTlsInspectionPolicy(String name)
    
    
    public final TlsInspectionPolicy getTlsInspectionPolicy(String name)

Gets details of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name =
           TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
               .toString();
       TlsInspectionPolicy response = networkSecurityClient.getTlsInspectionPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the TlsInspectionPolicy to get. Must be in the format `projects/{project}/locations/{location}/tlsInspectionPolicies/{tls_inspection_policy}`.  
**Returns**  
---  
**Type** | **Description**  
`[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)` |   
  
### getTlsInspectionPolicyCallable()
    
    
    public final UnaryCallable<GetTlsInspectionPolicyRequest,TlsInspectionPolicy> getTlsInspectionPolicyCallable()

Gets details of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetTlsInspectionPolicyRequest request =
           GetTlsInspectionPolicyRequest.newBuilder()
               .setName(
                   TlsInspectionPolicyName.of("[PROJECT]", "[LOCATION]", "[TLS_INSPECTION_POLICY]")
                       .toString())
               .build();
       ApiFuture<TlsInspectionPolicy> future =
           networkSecurityClient.getTlsInspectionPolicyCallable().futureCall(request);
       // Do something.
       TlsInspectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetTlsInspectionPolicyRequest),[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)>` |   
  
### getUrlList(@Nullable UrlListName name)
    
    
    public final UrlList getUrlList(@Nullable UrlListName name)

Gets details of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UrlListName name = UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]");
       UrlList response = networkSecurityClient.getUrlList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.UrlListName`  
Required. A name of the UrlList to get. Must be in the format `projects/*/locations/{location}/urlLists/*`.  
**Returns**  
---  
**Type** | **Description**  
`[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)` |   
  
### getUrlList(GetUrlListRequest request)
    
    
    public final UrlList getUrlList(GetUrlListRequest request)

Gets details of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetUrlListRequest request =
           GetUrlListRequest.newBuilder()
               .setName(UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString())
               .build();
       UrlList response = networkSecurityClient.getUrlList(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetUrlListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)` |   
  
### getUrlList(String name)
    
    
    public final UrlList getUrlList(String name)

Gets details of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String name = UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString();
       UrlList response = networkSecurityClient.getUrlList(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the UrlList to get. Must be in the format `projects/*/locations/{location}/urlLists/*`.  
**Returns**  
---  
**Type** | **Description**  
`[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)` |   
  
### getUrlListCallable()
    
    
    public final UnaryCallable<GetUrlListRequest,UrlList> getUrlListCallable()

Gets details of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GetUrlListRequest request =
           GetUrlListRequest.newBuilder()
               .setName(UrlListName.of("[PROJECT]", "[LOCATION]", "[URL_LIST]").toString())
               .build();
       ApiFuture<UrlList> future = networkSecurityClient.getUrlListCallable().futureCall(request);
       // Do something.
       UrlList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetUrlListRequest),[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)>` |   
  
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
  
### listAuthorizationPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse listAuthorizationPolicies(@Nullable LocationName parent)

Lists AuthorizationPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AuthorizationPolicy element :
           networkSecurityClient.listAuthorizationPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the AuthorizationPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse)` |   
  
### listAuthorizationPolicies(ListAuthorizationPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse listAuthorizationPolicies(ListAuthorizationPoliciesRequest request)

Lists AuthorizationPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthorizationPoliciesRequest request =
           ListAuthorizationPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (AuthorizationPolicy element :
           networkSecurityClient.listAuthorizationPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthorizationPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse)` |   
  
### listAuthorizationPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse listAuthorizationPolicies(String parent)

Lists AuthorizationPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AuthorizationPolicy element :
           networkSecurityClient.listAuthorizationPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the AuthorizationPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse)` |   
  
### listAuthorizationPoliciesCallable()
    
    
    public final UnaryCallable<ListAuthorizationPoliciesRequest,ListAuthorizationPoliciesResponse> listAuthorizationPoliciesCallable()

Lists AuthorizationPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthorizationPoliciesRequest request =
           ListAuthorizationPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListAuthorizationPoliciesResponse response =
             networkSecurityClient.listAuthorizationPoliciesCallable().call(request);
         for (AuthorizationPolicy element : response.getAuthorizationPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthorizationPoliciesRequest),[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthorizationPoliciesResponse)>` |   
  
### listAuthorizationPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListAuthorizationPoliciesRequest,NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse> listAuthorizationPoliciesPagedCallable()

Lists AuthorizationPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthorizationPoliciesRequest request =
           ListAuthorizationPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<AuthorizationPolicy> future =
           networkSecurityClient.listAuthorizationPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (AuthorizationPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthorizationPoliciesRequest),[ListAuthorizationPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthorizationPoliciesPagedResponse)>` |   
  
### listAuthzPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListAuthzPoliciesPagedResponse listAuthzPolicies(@Nullable LocationName parent)

Lists AuthzPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AuthzPolicy element : networkSecurityClient.listAuthzPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the `AuthzPolicy` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthzPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthzPoliciesPagedResponse)` |   
  
### listAuthzPolicies(ListAuthzPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListAuthzPoliciesPagedResponse listAuthzPolicies(ListAuthzPoliciesRequest request)

Lists AuthzPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthzPoliciesRequest request =
           ListAuthzPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AuthzPolicy element : networkSecurityClient.listAuthzPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthzPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthzPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthzPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthzPoliciesPagedResponse)` |   
  
### listAuthzPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListAuthzPoliciesPagedResponse listAuthzPolicies(String parent)

Lists AuthzPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AuthzPolicy element : networkSecurityClient.listAuthzPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `AuthzPolicy` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListAuthzPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthzPoliciesPagedResponse)` |   
  
### listAuthzPoliciesCallable()
    
    
    public final UnaryCallable<ListAuthzPoliciesRequest,ListAuthzPoliciesResponse> listAuthzPoliciesCallable()

Lists AuthzPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthzPoliciesRequest request =
           ListAuthzPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAuthzPoliciesResponse response =
             networkSecurityClient.listAuthzPoliciesCallable().call(request);
         for (AuthzPolicy element : response.getAuthzPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthzPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthzPoliciesRequest),[ListAuthzPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthzPoliciesResponse)>` |   
  
### listAuthzPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListAuthzPoliciesRequest,NetworkSecurityClient.ListAuthzPoliciesPagedResponse> listAuthzPoliciesPagedCallable()

Lists AuthzPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListAuthzPoliciesRequest request =
           ListAuthzPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AuthzPolicy> future =
           networkSecurityClient.listAuthzPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (AuthzPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthzPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListAuthzPoliciesRequest),[ListAuthzPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListAuthzPoliciesPagedResponse)>` |   
  
### listBackendAuthenticationConfigs(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse listBackendAuthenticationConfigs(@Nullable LocationName parent)

Lists BackendAuthenticationConfigs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackendAuthenticationConfig element :
           networkSecurityClient.listBackendAuthenticationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the BackendAuthenticationConfigs should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse)` |   
  
### listBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest request)
    
    
    public final NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse listBackendAuthenticationConfigs(ListBackendAuthenticationConfigsRequest request)

Lists BackendAuthenticationConfigs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListBackendAuthenticationConfigsRequest request =
           ListBackendAuthenticationConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BackendAuthenticationConfig element :
           networkSecurityClient.listBackendAuthenticationConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListBackendAuthenticationConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse)` |   
  
### listBackendAuthenticationConfigs(String parent)
    
    
    public final NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse listBackendAuthenticationConfigs(String parent)

Lists BackendAuthenticationConfigs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackendAuthenticationConfig element :
           networkSecurityClient.listBackendAuthenticationConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the BackendAuthenticationConfigs should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse)` |   
  
### listBackendAuthenticationConfigsCallable()
    
    
    public final UnaryCallable<ListBackendAuthenticationConfigsRequest,ListBackendAuthenticationConfigsResponse> listBackendAuthenticationConfigsCallable()

Lists BackendAuthenticationConfigs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListBackendAuthenticationConfigsRequest request =
           ListBackendAuthenticationConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBackendAuthenticationConfigsResponse response =
             networkSecurityClient.listBackendAuthenticationConfigsCallable().call(request);
         for (BackendAuthenticationConfig element : response.getBackendAuthenticationConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListBackendAuthenticationConfigsRequest),[ListBackendAuthenticationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListBackendAuthenticationConfigsResponse)>` |   
  
### listBackendAuthenticationConfigsPagedCallable()
    
    
    public final UnaryCallable<ListBackendAuthenticationConfigsRequest,NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse> listBackendAuthenticationConfigsPagedCallable()

Lists BackendAuthenticationConfigs in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListBackendAuthenticationConfigsRequest request =
           ListBackendAuthenticationConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BackendAuthenticationConfig> future =
           networkSecurityClient.listBackendAuthenticationConfigsPagedCallable().futureCall(request);
       // Do something.
       for (BackendAuthenticationConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendAuthenticationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListBackendAuthenticationConfigsRequest),[ListBackendAuthenticationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListBackendAuthenticationConfigsPagedResponse)>` |   
  
### listClientTlsPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListClientTlsPoliciesPagedResponse listClientTlsPolicies(@Nullable LocationName parent)

Lists ClientTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ClientTlsPolicy element :
           networkSecurityClient.listClientTlsPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the ClientTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListClientTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListClientTlsPoliciesPagedResponse)` |   
  
### listClientTlsPolicies(ListClientTlsPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListClientTlsPoliciesPagedResponse listClientTlsPolicies(ListClientTlsPoliciesRequest request)

Lists ClientTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListClientTlsPoliciesRequest request =
           ListClientTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ClientTlsPolicy element :
           networkSecurityClient.listClientTlsPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListClientTlsPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListClientTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListClientTlsPoliciesPagedResponse)` |   
  
### listClientTlsPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListClientTlsPoliciesPagedResponse listClientTlsPolicies(String parent)

Lists ClientTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ClientTlsPolicy element :
           networkSecurityClient.listClientTlsPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the ClientTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListClientTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListClientTlsPoliciesPagedResponse)` |   
  
### listClientTlsPoliciesCallable()
    
    
    public final UnaryCallable<ListClientTlsPoliciesRequest,ListClientTlsPoliciesResponse> listClientTlsPoliciesCallable()

Lists ClientTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListClientTlsPoliciesRequest request =
           ListClientTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListClientTlsPoliciesResponse response =
             networkSecurityClient.listClientTlsPoliciesCallable().call(request);
         for (ClientTlsPolicy element : response.getClientTlsPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListClientTlsPoliciesRequest),[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListClientTlsPoliciesResponse)>` |   
  
### listClientTlsPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListClientTlsPoliciesRequest,NetworkSecurityClient.ListClientTlsPoliciesPagedResponse> listClientTlsPoliciesPagedCallable()

Lists ClientTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListClientTlsPoliciesRequest request =
           ListClientTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ClientTlsPolicy> future =
           networkSecurityClient.listClientTlsPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (ClientTlsPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListClientTlsPoliciesRequest),[ListClientTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListClientTlsPoliciesPagedResponse)>` |   
  
### listGatewaySecurityPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse listGatewaySecurityPolicies(@Nullable LocationName parent)

Lists GatewaySecurityPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (GatewaySecurityPolicy element :
           networkSecurityClient.listGatewaySecurityPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the GatewaySecurityPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse)` |   
  
### listGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse listGatewaySecurityPolicies(ListGatewaySecurityPoliciesRequest request)

Lists GatewaySecurityPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPoliciesRequest request =
           ListGatewaySecurityPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (GatewaySecurityPolicy element :
           networkSecurityClient.listGatewaySecurityPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse)` |   
  
### listGatewaySecurityPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse listGatewaySecurityPolicies(String parent)

Lists GatewaySecurityPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (GatewaySecurityPolicy element :
           networkSecurityClient.listGatewaySecurityPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the GatewaySecurityPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse)` |   
  
### listGatewaySecurityPoliciesCallable()
    
    
    public final UnaryCallable<ListGatewaySecurityPoliciesRequest,ListGatewaySecurityPoliciesResponse> listGatewaySecurityPoliciesCallable()

Lists GatewaySecurityPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPoliciesRequest request =
           ListGatewaySecurityPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGatewaySecurityPoliciesResponse response =
             networkSecurityClient.listGatewaySecurityPoliciesCallable().call(request);
         for (GatewaySecurityPolicy element : response.getGatewaySecurityPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPoliciesRequest),[ListGatewaySecurityPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPoliciesResponse)>` |   
  
### listGatewaySecurityPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListGatewaySecurityPoliciesRequest,NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse> listGatewaySecurityPoliciesPagedCallable()

Lists GatewaySecurityPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPoliciesRequest request =
           ListGatewaySecurityPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<GatewaySecurityPolicy> future =
           networkSecurityClient.listGatewaySecurityPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (GatewaySecurityPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaySecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPoliciesRequest),[ListGatewaySecurityPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPoliciesPagedResponse)>` |   
  
### listGatewaySecurityPolicyRules(@Nullable GatewaySecurityPolicyName parent)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse listGatewaySecurityPolicyRules(@Nullable GatewaySecurityPolicyName parent)

Lists GatewaySecurityPolicyRules in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyName parent =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]");
       for (GatewaySecurityPolicyRule element :
           networkSecurityClient.listGatewaySecurityPolicyRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.GatewaySecurityPolicyName`  
Required. The project, location and GatewaySecurityPolicy from which the GatewaySecurityPolicyRules should be listed, specified in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse)` |   
  
### listGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest request)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse listGatewaySecurityPolicyRules(ListGatewaySecurityPolicyRulesRequest request)

Lists GatewaySecurityPolicyRules in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPolicyRulesRequest request =
           ListGatewaySecurityPolicyRulesRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (GatewaySecurityPolicyRule element :
           networkSecurityClient.listGatewaySecurityPolicyRules(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPolicyRulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse)` |   
  
### listGatewaySecurityPolicyRules(String parent)
    
    
    public final NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse listGatewaySecurityPolicyRules(String parent)

Lists GatewaySecurityPolicyRules in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent =
           GatewaySecurityPolicyName.of("[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
               .toString();
       for (GatewaySecurityPolicyRule element :
           networkSecurityClient.listGatewaySecurityPolicyRules(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project, location and GatewaySecurityPolicy from which the GatewaySecurityPolicyRules should be listed, specified in the format `projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse)` |   
  
### listGatewaySecurityPolicyRulesCallable()
    
    
    public final UnaryCallable<ListGatewaySecurityPolicyRulesRequest,ListGatewaySecurityPolicyRulesResponse> listGatewaySecurityPolicyRulesCallable()

Lists GatewaySecurityPolicyRules in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPolicyRulesRequest request =
           ListGatewaySecurityPolicyRulesRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListGatewaySecurityPolicyRulesResponse response =
             networkSecurityClient.listGatewaySecurityPolicyRulesCallable().call(request);
         for (GatewaySecurityPolicyRule element : response.getGatewaySecurityPolicyRulesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPolicyRulesRequest),[ListGatewaySecurityPolicyRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPolicyRulesResponse)>` |   
  
### listGatewaySecurityPolicyRulesPagedCallable()
    
    
    public final UnaryCallable<ListGatewaySecurityPolicyRulesRequest,NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse> listGatewaySecurityPolicyRulesPagedCallable()

Lists GatewaySecurityPolicyRules in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListGatewaySecurityPolicyRulesRequest request =
           ListGatewaySecurityPolicyRulesRequest.newBuilder()
               .setParent(
                   GatewaySecurityPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[GATEWAY_SECURITY_POLICY]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<GatewaySecurityPolicyRule> future =
           networkSecurityClient.listGatewaySecurityPolicyRulesPagedCallable().futureCall(request);
       // Do something.
       for (GatewaySecurityPolicyRule element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGatewaySecurityPolicyRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListGatewaySecurityPolicyRulesRequest),[ListGatewaySecurityPolicyRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListGatewaySecurityPolicyRulesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final NetworkSecurityClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : networkSecurityClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             networkSecurityClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,NetworkSecurityClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           networkSecurityClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListLocationsPagedResponse)>` |   
  
### listServerTlsPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListServerTlsPoliciesPagedResponse listServerTlsPolicies(@Nullable LocationName parent)

Lists ServerTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServerTlsPolicy element :
           networkSecurityClient.listServerTlsPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the ServerTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListServerTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListServerTlsPoliciesPagedResponse)` |   
  
### listServerTlsPolicies(ListServerTlsPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListServerTlsPoliciesPagedResponse listServerTlsPolicies(ListServerTlsPoliciesRequest request)

Lists ServerTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListServerTlsPoliciesRequest request =
           ListServerTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       for (ServerTlsPolicy element :
           networkSecurityClient.listServerTlsPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListServerTlsPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListServerTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListServerTlsPoliciesPagedResponse)` |   
  
### listServerTlsPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListServerTlsPoliciesPagedResponse listServerTlsPolicies(String parent)

Lists ServerTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServerTlsPolicy element :
           networkSecurityClient.listServerTlsPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the ServerTlsPolicies should be listed, specified in the format `projects/*/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListServerTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListServerTlsPoliciesPagedResponse)` |   
  
### listServerTlsPoliciesCallable()
    
    
    public final UnaryCallable<ListServerTlsPoliciesRequest,ListServerTlsPoliciesResponse> listServerTlsPoliciesCallable()

Lists ServerTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListServerTlsPoliciesRequest request =
           ListServerTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       while (true) {
         ListServerTlsPoliciesResponse response =
             networkSecurityClient.listServerTlsPoliciesCallable().call(request);
         for (ServerTlsPolicy element : response.getServerTlsPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListServerTlsPoliciesRequest),[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListServerTlsPoliciesResponse)>` |   
  
### listServerTlsPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListServerTlsPoliciesRequest,NetworkSecurityClient.ListServerTlsPoliciesPagedResponse> listServerTlsPoliciesPagedCallable()

Lists ServerTlsPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListServerTlsPoliciesRequest request =
           ListServerTlsPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReturnPartialSuccess(true)
               .build();
       ApiFuture<ServerTlsPolicy> future =
           networkSecurityClient.listServerTlsPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (ServerTlsPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListServerTlsPoliciesRequest),[ListServerTlsPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListServerTlsPoliciesPagedResponse)>` |   
  
### listTlsInspectionPolicies(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse listTlsInspectionPolicies(@Nullable LocationName parent)

Lists TlsInspectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (TlsInspectionPolicy element :
           networkSecurityClient.listTlsInspectionPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the TlsInspectionPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse)` |   
  
### listTlsInspectionPolicies(ListTlsInspectionPoliciesRequest request)
    
    
    public final NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse listTlsInspectionPolicies(ListTlsInspectionPoliciesRequest request)

Lists TlsInspectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListTlsInspectionPoliciesRequest request =
           ListTlsInspectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (TlsInspectionPolicy element :
           networkSecurityClient.listTlsInspectionPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListTlsInspectionPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse)` |   
  
### listTlsInspectionPolicies(String parent)
    
    
    public final NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse listTlsInspectionPolicies(String parent)

Lists TlsInspectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (TlsInspectionPolicy element :
           networkSecurityClient.listTlsInspectionPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the TlsInspectionPolicies should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse)` |   
  
### listTlsInspectionPoliciesCallable()
    
    
    public final UnaryCallable<ListTlsInspectionPoliciesRequest,ListTlsInspectionPoliciesResponse> listTlsInspectionPoliciesCallable()

Lists TlsInspectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListTlsInspectionPoliciesRequest request =
           ListTlsInspectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTlsInspectionPoliciesResponse response =
             networkSecurityClient.listTlsInspectionPoliciesCallable().call(request);
         for (TlsInspectionPolicy element : response.getTlsInspectionPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListTlsInspectionPoliciesRequest),[ListTlsInspectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListTlsInspectionPoliciesResponse)>` |   
  
### listTlsInspectionPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListTlsInspectionPoliciesRequest,NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse> listTlsInspectionPoliciesPagedCallable()

Lists TlsInspectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListTlsInspectionPoliciesRequest request =
           ListTlsInspectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<TlsInspectionPolicy> future =
           networkSecurityClient.listTlsInspectionPoliciesPagedCallable().futureCall(request);
       // Do something.
       for (TlsInspectionPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTlsInspectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListTlsInspectionPoliciesRequest),[ListTlsInspectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListTlsInspectionPoliciesPagedResponse)>` |   
  
### listUrlLists(@Nullable LocationName parent)
    
    
    public final NetworkSecurityClient.ListUrlListsPagedResponse listUrlLists(@Nullable LocationName parent)

Lists UrlLists in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (UrlList element : networkSecurityClient.listUrlLists(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networksecurity.v1.LocationName`  
Required. The project and location from which the UrlLists should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListUrlListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListUrlListsPagedResponse)` |   
  
### listUrlLists(ListUrlListsRequest request)
    
    
    public final NetworkSecurityClient.ListUrlListsPagedResponse listUrlLists(ListUrlListsRequest request)

Lists UrlLists in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListUrlListsRequest request =
           ListUrlListsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (UrlList element : networkSecurityClient.listUrlLists(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUrlListsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListUrlListsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListUrlListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListUrlListsPagedResponse)` |   
  
### listUrlLists(String parent)
    
    
    public final NetworkSecurityClient.ListUrlListsPagedResponse listUrlLists(String parent)

Lists UrlLists in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (UrlList element : networkSecurityClient.listUrlLists(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the UrlLists should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityClient.ListUrlListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListUrlListsPagedResponse)` |   
  
### listUrlListsCallable()
    
    
    public final UnaryCallable<ListUrlListsRequest,ListUrlListsResponse> listUrlListsCallable()

Lists UrlLists in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListUrlListsRequest request =
           ListUrlListsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListUrlListsResponse response = networkSecurityClient.listUrlListsCallable().call(request);
         for (UrlList element : response.getUrlListsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUrlListsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListUrlListsRequest),[ListUrlListsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListUrlListsResponse)>` |   
  
### listUrlListsPagedCallable()
    
    
    public final UnaryCallable<ListUrlListsRequest,NetworkSecurityClient.ListUrlListsPagedResponse> listUrlListsPagedCallable()

Lists UrlLists in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ListUrlListsRequest request =
           ListUrlListsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<UrlList> future =
           networkSecurityClient.listUrlListsPagedCallable().futureCall(request);
       // Do something.
       for (UrlList element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUrlListsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListUrlListsRequest),[ListUrlListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.NetworkSecurityClient.ListUrlListsPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = networkSecurityClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = networkSecurityClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = networkSecurityClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AddressGroupName.ofProjectLocationAddressGroupName(
                           "[PROJECT]", "[LOCATION]", "[ADDRESS_GROUP]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           networkSecurityClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAuthorizationPolicyAsync(AuthorizationPolicy authorizationPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<AuthorizationPolicy,OperationMetadata> updateAuthorizationPolicyAsync(AuthorizationPolicy authorizationPolicy, FieldMask updateMask)

Updates the parameters of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthorizationPolicy authorizationPolicy = AuthorizationPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AuthorizationPolicy response =
           networkSecurityClient
               .updateAuthorizationPolicyAsync(authorizationPolicy, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`authorizationPolicy` | `[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy)`  
Required. Updated AuthorizationPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the AuthorizationPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest request)
    
    
    public final OperationFuture<AuthorizationPolicy,OperationMetadata> updateAuthorizationPolicyAsync(UpdateAuthorizationPolicyRequest request)

Updates the parameters of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthorizationPolicyRequest request =
           UpdateAuthorizationPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       AuthorizationPolicy response =
           networkSecurityClient.updateAuthorizationPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthorizationPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateAuthorizationPolicyCallable()
    
    
    public final UnaryCallable<UpdateAuthorizationPolicyRequest,Operation> updateAuthorizationPolicyCallable()

Updates the parameters of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthorizationPolicyRequest request =
           UpdateAuthorizationPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateAuthorizationPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAuthorizationPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateAuthorizationPolicyRequest,AuthorizationPolicy,OperationMetadata> updateAuthorizationPolicyOperationCallable()

Updates the parameters of a single AuthorizationPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthorizationPolicyRequest request =
           UpdateAuthorizationPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthorizationPolicy(AuthorizationPolicy.newBuilder().build())
               .build();
       OperationFuture<AuthorizationPolicy, OperationMetadata> future =
           networkSecurityClient.updateAuthorizationPolicyOperationCallable().futureCall(request);
       // Do something.
       AuthorizationPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthorizationPolicyRequest),[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthorizationPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateAuthzPolicyAsync(AuthzPolicy authzPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<AuthzPolicy,OperationMetadata> updateAuthzPolicyAsync(AuthzPolicy authzPolicy, FieldMask updateMask)

Updates the parameters of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       AuthzPolicy authzPolicy = AuthzPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AuthzPolicy response =
           networkSecurityClient.updateAuthzPolicyAsync(authzPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`authzPolicy` | `[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy)`  
Required. `AuthzPolicy` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Used to specify the fields to be overwritten in the `AuthzPolicy` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateAuthzPolicyAsync(UpdateAuthzPolicyRequest request)
    
    
    public final OperationFuture<AuthzPolicy,OperationMetadata> updateAuthzPolicyAsync(UpdateAuthzPolicyRequest request)

Updates the parameters of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthzPolicyRequest request =
           UpdateAuthzPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthzPolicy response = networkSecurityClient.updateAuthzPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthzPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateAuthzPolicyCallable()
    
    
    public final UnaryCallable<UpdateAuthzPolicyRequest,Operation> updateAuthzPolicyCallable()

Updates the parameters of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthzPolicyRequest request =
           UpdateAuthzPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateAuthzPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthzPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAuthzPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateAuthzPolicyRequest,AuthzPolicy,OperationMetadata> updateAuthzPolicyOperationCallable()

Updates the parameters of a single AuthzPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateAuthzPolicyRequest request =
           UpdateAuthzPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzPolicy(AuthzPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AuthzPolicy, OperationMetadata> future =
           networkSecurityClient.updateAuthzPolicyOperationCallable().futureCall(request);
       // Do something.
       AuthzPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAuthzPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateAuthzPolicyRequest),[AuthzPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.AuthzPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateBackendAuthenticationConfigAsync(BackendAuthenticationConfig backendAuthenticationConfig, FieldMask updateMask)
    
    
    public final OperationFuture<BackendAuthenticationConfig,OperationMetadata> updateBackendAuthenticationConfigAsync(BackendAuthenticationConfig backendAuthenticationConfig, FieldMask updateMask)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       BackendAuthenticationConfig backendAuthenticationConfig =
           BackendAuthenticationConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BackendAuthenticationConfig response =
           networkSecurityClient
               .updateBackendAuthenticationConfigAsync(backendAuthenticationConfig, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backendAuthenticationConfig` | `[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig)`  
Required. Updated BackendAuthenticationConfig resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the BackendAuthenticationConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest request)
    
    
    public final OperationFuture<BackendAuthenticationConfig,OperationMetadata> updateBackendAuthenticationConfigAsync(UpdateBackendAuthenticationConfigRequest request)

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateBackendAuthenticationConfigRequest request =
           UpdateBackendAuthenticationConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       BackendAuthenticationConfig response =
           networkSecurityClient.updateBackendAuthenticationConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateBackendAuthenticationConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateBackendAuthenticationConfigCallable()
    
    
    public final UnaryCallable<UpdateBackendAuthenticationConfigRequest,Operation> updateBackendAuthenticationConfigCallable()

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateBackendAuthenticationConfigRequest request =
           UpdateBackendAuthenticationConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateBackendAuthenticationConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateBackendAuthenticationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackendAuthenticationConfigOperationCallable()
    
    
    public final OperationCallable<UpdateBackendAuthenticationConfigRequest,BackendAuthenticationConfig,OperationMetadata> updateBackendAuthenticationConfigOperationCallable()

Updates the parameters of a single BackendAuthenticationConfig to BackendAuthenticationConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateBackendAuthenticationConfigRequest request =
           UpdateBackendAuthenticationConfigRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setBackendAuthenticationConfig(BackendAuthenticationConfig.newBuilder().build())
               .build();
       OperationFuture<BackendAuthenticationConfig, OperationMetadata> future =
           networkSecurityClient
               .updateBackendAuthenticationConfigOperationCallable()
               .futureCall(request);
       // Do something.
       BackendAuthenticationConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackendAuthenticationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateBackendAuthenticationConfigRequest),[BackendAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.BackendAuthenticationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateClientTlsPolicyAsync(ClientTlsPolicy clientTlsPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<ClientTlsPolicy,OperationMetadata> updateClientTlsPolicyAsync(ClientTlsPolicy clientTlsPolicy, FieldMask updateMask)

Updates the parameters of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ClientTlsPolicy clientTlsPolicy = ClientTlsPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ClientTlsPolicy response =
           networkSecurityClient.updateClientTlsPolicyAsync(clientTlsPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`clientTlsPolicy` | `[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy)`  
Required. Updated ClientTlsPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ClientTlsPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest request)
    
    
    public final OperationFuture<ClientTlsPolicy,OperationMetadata> updateClientTlsPolicyAsync(UpdateClientTlsPolicyRequest request)

Updates the parameters of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateClientTlsPolicyRequest request =
           UpdateClientTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       ClientTlsPolicy response = networkSecurityClient.updateClientTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateClientTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateClientTlsPolicyCallable()
    
    
    public final UnaryCallable<UpdateClientTlsPolicyRequest,Operation> updateClientTlsPolicyCallable()

Updates the parameters of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateClientTlsPolicyRequest request =
           UpdateClientTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateClientTlsPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClientTlsPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateClientTlsPolicyRequest,ClientTlsPolicy,OperationMetadata> updateClientTlsPolicyOperationCallable()

Updates the parameters of a single ClientTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateClientTlsPolicyRequest request =
           UpdateClientTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setClientTlsPolicy(ClientTlsPolicy.newBuilder().build())
               .build();
       OperationFuture<ClientTlsPolicy, OperationMetadata> future =
           networkSecurityClient.updateClientTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       ClientTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateClientTlsPolicyRequest),[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ClientTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyAsync(GatewaySecurityPolicy gatewaySecurityPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<GatewaySecurityPolicy,OperationMetadata> updateGatewaySecurityPolicyAsync(GatewaySecurityPolicy gatewaySecurityPolicy, FieldMask updateMask)

Updates the parameters of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicy gatewaySecurityPolicy = GatewaySecurityPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GatewaySecurityPolicy response =
           networkSecurityClient
               .updateGatewaySecurityPolicyAsync(gatewaySecurityPolicy, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`gatewaySecurityPolicy` | `[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy)`  
Required. Updated GatewaySecurityPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the GatewaySecurityPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest request)
    
    
    public final OperationFuture<GatewaySecurityPolicy,OperationMetadata> updateGatewaySecurityPolicyAsync(UpdateGatewaySecurityPolicyRequest request)

Updates the parameters of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRequest request =
           UpdateGatewaySecurityPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       GatewaySecurityPolicy response =
           networkSecurityClient.updateGatewaySecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyCallable()
    
    
    public final UnaryCallable<UpdateGatewaySecurityPolicyRequest,Operation> updateGatewaySecurityPolicyCallable()

Updates the parameters of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRequest request =
           UpdateGatewaySecurityPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateGatewaySecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGatewaySecurityPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateGatewaySecurityPolicyRequest,GatewaySecurityPolicy,OperationMetadata> updateGatewaySecurityPolicyOperationCallable()

Updates the parameters of a single GatewaySecurityPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRequest request =
           UpdateGatewaySecurityPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicy(GatewaySecurityPolicy.newBuilder().build())
               .build();
       OperationFuture<GatewaySecurityPolicy, OperationMetadata> future =
           networkSecurityClient.updateGatewaySecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       GatewaySecurityPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGatewaySecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRequest),[GatewaySecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyRuleAsync(GatewaySecurityPolicyRule gatewaySecurityPolicyRule, FieldMask updateMask)
    
    
    public final OperationFuture<GatewaySecurityPolicyRule,OperationMetadata> updateGatewaySecurityPolicyRuleAsync(GatewaySecurityPolicyRule gatewaySecurityPolicyRule, FieldMask updateMask)

Updates the parameters of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       GatewaySecurityPolicyRule gatewaySecurityPolicyRule =
           GatewaySecurityPolicyRule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       GatewaySecurityPolicyRule response =
           networkSecurityClient
               .updateGatewaySecurityPolicyRuleAsync(gatewaySecurityPolicyRule, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyRule` | `[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule)`  
Required. Updated GatewaySecurityPolicyRule resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the GatewaySecurityPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest request)
    
    
    public final OperationFuture<GatewaySecurityPolicyRule,OperationMetadata> updateGatewaySecurityPolicyRuleAsync(UpdateGatewaySecurityPolicyRuleRequest request)

Updates the parameters of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRuleRequest request =
           UpdateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .build();
       GatewaySecurityPolicyRule response =
           networkSecurityClient.updateGatewaySecurityPolicyRuleAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRuleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateGatewaySecurityPolicyRuleCallable()
    
    
    public final UnaryCallable<UpdateGatewaySecurityPolicyRuleRequest,Operation> updateGatewaySecurityPolicyRuleCallable()

Updates the parameters of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRuleRequest request =
           UpdateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateGatewaySecurityPolicyRuleCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGatewaySecurityPolicyRuleOperationCallable()
    
    
    public final OperationCallable<UpdateGatewaySecurityPolicyRuleRequest,GatewaySecurityPolicyRule,OperationMetadata> updateGatewaySecurityPolicyRuleOperationCallable()

Updates the parameters of a single GatewaySecurityPolicyRule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateGatewaySecurityPolicyRuleRequest request =
           UpdateGatewaySecurityPolicyRuleRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setGatewaySecurityPolicyRule(GatewaySecurityPolicyRule.newBuilder().build())
               .build();
       OperationFuture<GatewaySecurityPolicyRule, OperationMetadata> future =
           networkSecurityClient
               .updateGatewaySecurityPolicyRuleOperationCallable()
               .futureCall(request);
       // Do something.
       GatewaySecurityPolicyRule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateGatewaySecurityPolicyRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateGatewaySecurityPolicyRuleRequest),[GatewaySecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GatewaySecurityPolicyRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateServerTlsPolicyAsync(ServerTlsPolicy serverTlsPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<ServerTlsPolicy,OperationMetadata> updateServerTlsPolicyAsync(ServerTlsPolicy serverTlsPolicy, FieldMask updateMask)

Updates the parameters of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       ServerTlsPolicy serverTlsPolicy = ServerTlsPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServerTlsPolicy response =
           networkSecurityClient.updateServerTlsPolicyAsync(serverTlsPolicy, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serverTlsPolicy` | `[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy)`  
Required. Updated ServerTlsPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServerTlsPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest request)
    
    
    public final OperationFuture<ServerTlsPolicy,OperationMetadata> updateServerTlsPolicyAsync(UpdateServerTlsPolicyRequest request)

Updates the parameters of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateServerTlsPolicyRequest request =
           UpdateServerTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       ServerTlsPolicy response = networkSecurityClient.updateServerTlsPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateServerTlsPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateServerTlsPolicyCallable()
    
    
    public final UnaryCallable<UpdateServerTlsPolicyRequest,Operation> updateServerTlsPolicyCallable()

Updates the parameters of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateServerTlsPolicyRequest request =
           UpdateServerTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateServerTlsPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServerTlsPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateServerTlsPolicyRequest,ServerTlsPolicy,OperationMetadata> updateServerTlsPolicyOperationCallable()

Updates the parameters of a single ServerTlsPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateServerTlsPolicyRequest request =
           UpdateServerTlsPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServerTlsPolicy(ServerTlsPolicy.newBuilder().build())
               .build();
       OperationFuture<ServerTlsPolicy, OperationMetadata> future =
           networkSecurityClient.updateServerTlsPolicyOperationCallable().futureCall(request);
       // Do something.
       ServerTlsPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateServerTlsPolicyRequest),[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ServerTlsPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateTlsInspectionPolicyAsync(TlsInspectionPolicy tlsInspectionPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<TlsInspectionPolicy,OperationMetadata> updateTlsInspectionPolicyAsync(TlsInspectionPolicy tlsInspectionPolicy, FieldMask updateMask)

Updates the parameters of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       TlsInspectionPolicy tlsInspectionPolicy = TlsInspectionPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TlsInspectionPolicy response =
           networkSecurityClient
               .updateTlsInspectionPolicyAsync(tlsInspectionPolicy, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tlsInspectionPolicy` | `[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy)`  
Required. Updated TlsInspectionPolicy resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the TlsInspectionPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest request)
    
    
    public final OperationFuture<TlsInspectionPolicy,OperationMetadata> updateTlsInspectionPolicyAsync(UpdateTlsInspectionPolicyRequest request)

Updates the parameters of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateTlsInspectionPolicyRequest request =
           UpdateTlsInspectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       TlsInspectionPolicy response =
           networkSecurityClient.updateTlsInspectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateTlsInspectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateTlsInspectionPolicyCallable()
    
    
    public final UnaryCallable<UpdateTlsInspectionPolicyRequest,Operation> updateTlsInspectionPolicyCallable()

Updates the parameters of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateTlsInspectionPolicyRequest request =
           UpdateTlsInspectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateTlsInspectionPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateTlsInspectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTlsInspectionPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateTlsInspectionPolicyRequest,TlsInspectionPolicy,OperationMetadata> updateTlsInspectionPolicyOperationCallable()

Updates the parameters of a single TlsInspectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateTlsInspectionPolicyRequest request =
           UpdateTlsInspectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTlsInspectionPolicy(TlsInspectionPolicy.newBuilder().build())
               .build();
       OperationFuture<TlsInspectionPolicy, OperationMetadata> future =
           networkSecurityClient.updateTlsInspectionPolicyOperationCallable().futureCall(request);
       // Do something.
       TlsInspectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTlsInspectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateTlsInspectionPolicyRequest),[TlsInspectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.TlsInspectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateUrlListAsync(UpdateUrlListRequest request)
    
    
    public final OperationFuture<UrlList,OperationMetadata> updateUrlListAsync(UpdateUrlListRequest request)

Updates the parameters of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateUrlListRequest request =
           UpdateUrlListRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUrlList(UrlList.newBuilder().build())
               .build();
       UrlList response = networkSecurityClient.updateUrlListAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateUrlListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateUrlListAsync(UrlList urlList, FieldMask updateMask)
    
    
    public final OperationFuture<UrlList,OperationMetadata> updateUrlListAsync(UrlList urlList, FieldMask updateMask)

Updates the parameters of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UrlList urlList = UrlList.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       UrlList response = networkSecurityClient.updateUrlListAsync(urlList, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`urlList` | `[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList)`  
Required. Updated UrlList resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the UrlList resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
### updateUrlListCallable()
    
    
    public final UnaryCallable<UpdateUrlListRequest,Operation> updateUrlListCallable()

Updates the parameters of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateUrlListRequest request =
           UpdateUrlListRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUrlList(UrlList.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           networkSecurityClient.updateUrlListCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateUrlListRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateUrlListOperationCallable()
    
    
    public final OperationCallable<UpdateUrlListRequest,UrlList,OperationMetadata> updateUrlListOperationCallable()

Updates the parameters of a single UrlList.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkSecurityClient networkSecurityClient = NetworkSecurityClient.create()) {
       UpdateUrlListRequest request =
           UpdateUrlListRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUrlList(UrlList.newBuilder().build())
               .build();
       OperationFuture<UrlList, OperationMetadata> future =
           networkSecurityClient.updateUrlListOperationCallable().futureCall(request);
       // Do something.
       UrlList response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateUrlListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateUrlListRequest),[UrlList](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UrlList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
