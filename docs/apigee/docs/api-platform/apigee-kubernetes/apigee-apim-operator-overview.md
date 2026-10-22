---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-overview/
title: Apigee Operator for Kubernetes overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:52.308337+00:00
---

# Apigee Operator for Kubernetes overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Operator for Kubernetes overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee Operator for Kubernetes allows you to perform API management tasks, such as defining [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#what-is-an-api-product) and [operations](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product#operations), using Kubernetes tools. It is designed to support cloud-native developers by providing a command-line interface that integrates with familiar Kubernetes tools like [`kubectl`](https://kubernetes.io/docs/reference/kubectl/). The operator works by using various APIM resources to keep your Google Kubernetes Engine cluster synchronized with the Apigee runtime.

**Note** : The Apigee Operator for Kubernetes is designed to be used with the Apigee runtime. It is not a standalone product.

## Benefits

The Apigee Operator for Kubernetes can benefit your organization by providing: 

  * **Simplified API Management** : The APIM Operator allows API producers to manage and secure their APIs using Kubernetes resource definitions. You can use the same tools and workflows for managing your APIs that you use for other Kubernetes resources.
  * **Streamlined Networking** : The operator enforces API policies at the load balancer level, which streamlines the networking setup and reduces complexity in managing API access and security.
  * **Fine-grained access control** : The addition of Kubernetes' role-based access control (RBAC) to Apigee custom resource definitions enables fine-grained access control for a range of roles, including API developers, platform administrators, and infrastructure administrators.
  * **Integration with Kubernetes** : The operator integrates with native Kubernetes concepts such as Custom Resource Definitions (CRDs) and Helm charts, providing a seamless experience for cloud-native developers.
  * **Reduced Context Switching** : By enabling API management directly from the Kubernetes environment, the APIM Operator reduces the need for developers to switch between different tools and interfaces.



## When to use Apigee Operator for Kubernetes 

The Apigee Operator for Kubernetes is designed to be used by API producers who want to manage their APIs using Kubernetes tools. It is especially useful for cloud-native developers who are familiar with Kubernetes and want to use the same tools and workflows for managing their APIs that they use for other Kubernetes resources. The Apigee Operator for Kubernetes enables existing Apigee customers to extend their API management infrastructure with tools based on [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io) technologies.

## How Apigee Operator for Kubernetes works

The Apigee Operator for Kubernetes uses the GKE gateway of an [ Application Load Balancer](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs), along with a [traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) to act as a policy enforcement point (PEP). The traffic extension calls out to Apigee using the Apigee Extension Processor and Apigee acts as the policy decision point (PDP).

When configuring the Apigee Operator for Kubernetes, you can use one of the following approaches to describe the traffic extension: 

  * Create an `APIMExtensionPolicy`. With this approach, the Apigee Operator for Kubernetes creates the required traffic extension on the GKE gateway with the appropriate configuration. We recommend using this approach if you do not have other traffic extensions or you do not want to create one yourself. Do not use the `APIMExtensionPolicy` if you have other traffic extensions on the GKE gateway that need to work with the Apigee traffic extension. 

See [Create an APIMExtensionPolicy](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension) for more information on using this approach to implement the Apigee Operator for Kubernetes.

  * Use an `ApigeeBackendService`. We recommend using this approach if you are creating and managing [Cloud Load Balancing traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) and you want to add Apigee as an extension in your [traffic extension](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcp-extensions) resource. You must use the `ApigeeBackendService` if the Apigee traffic extension has to work in conjunction with other traffic extensions. **Note:** The `ApigeeBackendService` requires GKE version 1.34.x or later.

See [Create an ApigeeBackendService](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice) for more information on using this approach to implement the Apigee Operator for Kubernetes.




## Requirements

Before you install the Apigee Operator for Kubernetes, note the following: 

  * The Apigee Operator for Kubernetes requires a GKE cluster with GKE version 1.27 or later.
  * The Apigee Operator for Kubernetes is only supported for use with Apigee version `1-15-0-apigee-4` or later. It can't be used with Apigee hybrid at this time.
  * The Apigee Operator for Kubernetes requires [Helm version 3.13.3](https://helm.sh/docs/intro/install) or later.



## Known limitations

The following limitations apply to the Apigee Operator for Kubernetes: 

  * Only REST APIs are supported. gRPC and GraphQL are not supported.
  * A maximum of 25 regional or global GKE Gateway resources with API management policies attached are supported.
  * A maximum of 50 APIM extension policies can be applied to a single environment. To add more APIM extension policies, you must create a new environment.
  * API management policies can only be attached to Gateway resources and not to HTTPRoutes. API management policies can't be used to govern HTTPRoutes. As an alternative, policies can be applied conditionally on a route (basepath or header), using the conditional policy feature of the [ApimTemplate resource](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-reference#apimtemplate). 
  * Region expansion is not supported. Once configured, the Apigee Operator for Kubernetes can't be expanded to additional regions.
  * If using the `ApigeeBackendService` to implement the GKE traffic extensions, you must use GKE version 1.34.x or later and deploy all gateway resources in the `default` namespace.
  * The API version has changed from the public preview (now `apim.googleapis.com/v1`). The GA version of Apigee Operator for Kubernetes is not compatible with or upgradeable from the public preview version previously released.



## What's next

  * Learn how to [Install the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install).
  * [Create an `APIMExtensionPolicy`](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
