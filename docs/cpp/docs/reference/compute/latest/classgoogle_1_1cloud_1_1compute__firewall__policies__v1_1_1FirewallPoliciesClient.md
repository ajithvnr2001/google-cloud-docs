---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__firewall__policies__v1_1_1FirewallPoliciesClient/
title: Class FirewallPoliciesClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:00.372160+00:00
---

# Class FirewallPoliciesClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__firewall__policies__v1_1_1FirewallPoliciesClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class FirewallPoliciesClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

Service for the firewallPolicies resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies>

This client uses FirewallPolicies version 2026-09-01.

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### FirewallPoliciesClient(FirewallPoliciesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `FirewallPoliciesClient const &`   
  
  
### FirewallPoliciesClient(FirewallPoliciesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `FirewallPoliciesClient &&`   
  
  
### FirewallPoliciesClient(std::shared_ptr< FirewallPoliciesConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< FirewallPoliciesConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(FirewallPoliciesClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `FirewallPoliciesClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`FirewallPoliciesClient &` |   
  
### operator=(FirewallPoliciesClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `FirewallPoliciesClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`FirewallPoliciesClient &` |   
  
## Functions 

### AddAssociation(std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyAssociation const &, Options)

Inserts an association for the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addAssociation>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`firewall_policy_association_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyAssociation const &`   
The FirewallPolicyAssociation for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AddAssociation(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyAssociation const &, Options)

Inserts an association for the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`firewall_policy_association_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyAssociation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AddAssociation(google::cloud::cpp::compute::firewall_policies::v1::AddAssociationRequest const &, Options)

Inserts an association for the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addAssociation>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::AddAssociationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.AddAssociationRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L253). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AddAssociation(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::AddAssociationRequest const &, Options)

Inserts an association for the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::AddAssociationRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AddAssociation(google::cloud::cpp::compute::v1::Operation const &, Options)

Inserts an association for the specified firewall policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### AddRule(std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyRule const &, Options)

Inserts a rule into a firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addRule>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`firewall_policy_rule_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyRule const &`   
The FirewallPolicyRule for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AddRule(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyRule const &, Options)

Inserts a rule into a firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`firewall_policy_rule_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyRule const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AddRule(google::cloud::cpp::compute::firewall_policies::v1::AddRuleRequest const &, Options)

Inserts a rule into a firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addRule>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::AddRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.AddRuleRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L286). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### AddRule(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::AddRuleRequest const &, Options)

Inserts a rule into a firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::AddRuleRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### AddRule(google::cloud::cpp::compute::v1::Operation const &, Options)

Inserts a rule into a firewall policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### CloneRules(std::string const &, Options)

Copies rules to the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/cloneRules>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CloneRules(NoAwaitTag, std::string const &, Options)

Copies rules to the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### CloneRules(google::cloud::cpp::compute::firewall_policies::v1::CloneRulesRequest const &, Options)

Copies rules to the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/cloneRules>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::CloneRulesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.CloneRulesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L312). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### CloneRules(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::CloneRulesRequest const &, Options)

Copies rules to the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::CloneRulesRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### CloneRules(google::cloud::cpp::compute::v1::Operation const &, Options)

Copies rules to the specified firewall policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### DeleteFirewallPolicy(std::string const &, Options)

Deletes the specified policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/delete>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to delete.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteFirewallPolicy(NoAwaitTag, std::string const &, Options)

Deletes the specified policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteFirewallPolicy(google::cloud::cpp::compute::firewall_policies::v1::DeleteFirewallPolicyRequest const &, Options)

Deletes the specified policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/delete>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::DeleteFirewallPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.DeleteFirewallPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L338). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### DeleteFirewallPolicy(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::DeleteFirewallPolicyRequest const &, Options)

Deletes the specified policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::DeleteFirewallPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### DeleteFirewallPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes the specified policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### GetFirewallPolicy(std::string const &, Options)

Returns the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/get>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to get.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_048.proto#L27)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetFirewallPolicy(google::cloud::cpp::compute::firewall_policies::v1::GetFirewallPolicyRequest const &, Options)

Returns the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/get>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::GetFirewallPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.GetFirewallPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L370). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_048.proto#L27)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetAssociation(std::string const &, Options)

Gets an association with the specified name. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getAssociation>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to which the queried rule belongs.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicyAssociation >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicyAssociation](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_048.proto#L132)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetAssociation(google::cloud::cpp::compute::firewall_policies::v1::GetAssociationRequest const &, Options)

Gets an association with the specified name. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getAssociation>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::GetAssociationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.GetAssociationRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L360). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicyAssociation >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicyAssociation](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_048.proto#L132)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(std::string const &, Options)

Gets the access control policy for a resource. 

May be empty if no such policy or resource exists. <https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetIamPolicy(google::cloud::cpp::compute::firewall_policies::v1::GetIamPolicyRequest const &, Options)

Gets the access control policy for a resource. 

May be empty if no such policy or resource exists. <https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::GetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.GetIamPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L377). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetRule(std::string const &, Options)

Gets a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getRule>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to which the queried rule belongs.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicyRule >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicyRule](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_049.proto#L26)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### GetRule(google::cloud::cpp::compute::firewall_policies::v1::GetRuleRequest const &, Options)

Gets a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/getRule>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::GetRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.GetRuleRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L388). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPolicyRule >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPolicyRule](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_049.proto#L26)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### InsertFirewallPolicy(google::cloud::cpp::compute::firewall_policies::v1::InsertFirewallPolicyRequest const &, Options)

Creates a new policy in the specified project using the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/insert>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::InsertFirewallPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.InsertFirewallPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L398). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### InsertFirewallPolicy(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::InsertFirewallPolicyRequest const &, Options)

Creates a new policy in the specified project using the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::InsertFirewallPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### InsertFirewallPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Creates a new policy in the specified project using the data included in the request. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### ListFirewallPolicies(google::cloud::cpp::compute::firewall_policies::v1::ListFirewallPoliciesRequest, Options)

Lists all the policies that have been configured for the specified folder or organization. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/list>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::ListFirewallPoliciesRequest`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.ListFirewallPoliciesRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L438). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::FirewallPolicy >` | a [StreamRange](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StreamRange.html) to iterate of the results. See the documentation of this type for details. In brief, this class has `begin()` and `end()` member functions returning a iterator class meeting the [input iterator requirements](https://en.cppreference.com/w/cpp/named_req/InputIterator). The value type for this iterator is a [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) as the iteration may fail even after some values are retrieved successfully, for example, if there is a network disconnect. An empty set of results does not indicate an error, it indicates that there are no resources meeting the request criteria. On a successful iteration the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains elements of type [google.cloud.cpp.compute.v1.FirewallPolicy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_048.proto#L27), or rather, the C++ class generated by Protobuf from that type. Please consult the Protobuf documentation for details on the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### ListAssociations(google::cloud::cpp::compute::firewall_policies::v1::ListAssociationsRequest const &, Options)

Lists associations of a specified target, i.e., organization or folder. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/listAssociations>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::ListAssociationsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.ListAssociationsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L425). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::FirewallPoliciesListAssociationsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.FirewallPoliciesListAssociationsResponse](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_046.proto#L27)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### Move(std::string const &, Options)

Moves the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/move>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### Move(NoAwaitTag, std::string const &, Options)

Moves the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### Move(google::cloud::cpp::compute::firewall_policies::v1::MoveRequest const &, Options)

Moves the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/move>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::MoveRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.MoveRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L533). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### Move(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::MoveRequest const &, Options)

Moves the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::MoveRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### Move(google::cloud::cpp::compute::v1::Operation const &, Options)

Moves the specified firewall policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### PatchFirewallPolicy(std::string const &, google::cloud::cpp::compute::v1::FirewallPolicy const &, Options)

Patches the specified policy with the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patch>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`firewall_policy_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicy const &`   
The FirewallPolicy for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchFirewallPolicy(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::FirewallPolicy const &, Options)

Patches the specified policy with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`firewall_policy_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicy const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchFirewallPolicy(google::cloud::cpp::compute::firewall_policies::v1::PatchFirewallPolicyRequest const &, Options)

Patches the specified policy with the data included in the request. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patch>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::PatchFirewallPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.PatchFirewallPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L560). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchFirewallPolicy(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::PatchFirewallPolicyRequest const &, Options)

Patches the specified policy with the data included in the request. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::PatchFirewallPolicyRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchFirewallPolicy(google::cloud::cpp::compute::v1::Operation const &, Options)

Patches the specified policy with the data included in the request. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### PatchRule(std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyRule const &, Options)

Patches a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patchRule>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`firewall_policy_rule_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyRule const &`   
The FirewallPolicyRule for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchRule(NoAwaitTag, std::string const &, google::cloud::cpp::compute::v1::FirewallPolicyRule const &, Options)

Patches a rule of the specified priority. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`firewall_policy_rule_resource` |  `google::cloud::cpp::compute::v1::FirewallPolicyRule const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchRule(google::cloud::cpp::compute::firewall_policies::v1::PatchRuleRequest const &, Options)

Patches a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patchRule>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::PatchRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.PatchRuleRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L586). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### PatchRule(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::PatchRuleRequest const &, Options)

Patches a rule of the specified priority. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::PatchRuleRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### PatchRule(google::cloud::cpp::compute::v1::Operation const &, Options)

Patches a rule of the specified priority. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### RemoveAssociation(std::string const &, Options)

Removes an association for the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/removeAssociation>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RemoveAssociation(NoAwaitTag, std::string const &, Options)

Removes an association for the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### RemoveAssociation(google::cloud::cpp::compute::firewall_policies::v1::RemoveAssociationRequest const &, Options)

Removes an association for the specified firewall policy. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/removeAssociation>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::RemoveAssociationRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.RemoveAssociationRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L615). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RemoveAssociation(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::RemoveAssociationRequest const &, Options)

Removes an association for the specified firewall policy. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::RemoveAssociationRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### RemoveAssociation(google::cloud::cpp::compute::v1::Operation const &, Options)

Removes an association for the specified firewall policy. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### RemoveRule(std::string const &, Options)

Deletes a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/removeRule>

**Parameters**  
---  
**Name** | **Description**  
`firewall_policy` |  `std::string const &`   
Name of the firewall policy to update.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RemoveRule(NoAwaitTag, std::string const &, Options)

Deletes a rule of the specified priority. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`firewall_policy` |  `std::string const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### RemoveRule(google::cloud::cpp::compute::firewall_policies::v1::RemoveRuleRequest const &, Options)

Deletes a rule of the specified priority. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/removeRule>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::RemoveRuleRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.RemoveRuleRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L640). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` | A [`future`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future.html) that becomes satisfied when the LRO ([Long Running Operation](http://cloud/compute/docs/api/how-tos/api-requests-responses#handling_api_responses)) completes or the polling policy in effect for this call is exhausted. The future is satisfied with an error if the LRO completes with an error or the polling policy is exhausted. In this case the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) returned by the future contains the error. If the LRO completes successfully the value of the future contains the LRO's result. For this RPC the result is a [google.cloud.cpp.compute.v1.Operation] proto message. The C++ class representing this message is created by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
  
### RemoveRule(NoAwaitTag, google::cloud::cpp::compute::firewall_policies::v1::RemoveRuleRequest const &, Options)

Deletes a rule of the specified priority. 

Specifying the [`NoAwaitTag`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1NoAwaitTag.html) immediately returns the [`google::cloud::cpp::compute::v1::Operation`] that corresponds to the Long Running Operation that has been started. No polling for operation status occurs. 

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::RemoveRuleRequest const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### RemoveRule(google::cloud::cpp::compute::v1::Operation const &, Options)

Deletes a rule of the specified priority. 

This method accepts a `google::cloud::cpp::compute::v1::Operation` that corresponds to a previously started Long Running Operation (LRO) and polls the status of the LRO in the background. 

**Parameters**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### SetIamPolicy(std::string const &, google::cloud::cpp::compute::v1::GlobalOrganizationSetPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy. <https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/setIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`global_organization_set_policy_request_resource` |  `google::cloud::cpp::compute::v1::GlobalOrganizationSetPolicyRequest const &`   
The GlobalOrganizationSetPolicyRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### SetIamPolicy(google::cloud::cpp::compute::firewall_policies::v1::SetIamPolicyRequest const &, Options)

Sets the access control policy on the specified resource. 

Replaces any existing policy. <https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/setIamPolicy>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::SetIamPolicyRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.SetIamPolicyRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L665). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Policy >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.Policy](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_010.proto#L317)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(std::string const &, google::cloud::cpp::compute::v1::TestPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`resource` |  `std::string const &`   
Name or id of the resource for this request.   
`test_permissions_request_resource` |  `google::cloud::cpp::compute::v1::TestPermissionsRequest const &`   
The TestPermissionsRequest for this request.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### TestIamPermissions(google::cloud::cpp::compute::firewall_policies::v1::TestIamPermissionsRequest const &, Options)

Returns permissions that a caller has on the specified resource. 

<https://cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/testIamPermissions>

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::firewall_policies::v1::TestIamPermissionsRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.cpp.compute.firewall_policies.v1.TestIamPermissionsRequest](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/firewall_policies/v1/firewall_policies.proto#L677). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::TestPermissionsResponse >` | the result of the RPC. The response message type ([google.cloud.cpp.compute.v1.TestPermissionsResponse](https://github.com/googleapis/google-cloud-cpp/blob/b304472d248b766fbd740dcccd83f2eef337b974/google/cloud/compute/v1/internal/common_177.proto#L30)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
