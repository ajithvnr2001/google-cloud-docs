---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/api-development-lifecycle/
title: API development lifecycle \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:28.782701+00:00
---

# API development lifecycle  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/api-development-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API development lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The following sections summarize the API development lifecycle using Apigee. 

## Developing API proxies

Apigee supports the following options for iterative API proxy development: 

  * Cloud development using Apigee
  * Local development using Apigee in VS Code



For more information about API proxies, see [Understanding APIs and API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies). 

### Cloud development using Apigee

Develop your API proxies using the API proxy editing and debugging tools provided with Apigee. As you work on an API proxy, Apigee saves iterations of your configuration as _revisions_. 

When you deploy an API proxy, you choose a specific revision to deploy. Typically, you deploy the most recent revision, and, if necessary, revert to a previous revision. See Deploying API proxies. 

To get started developing your API proxies using Apigee, see [Building a simple API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy). 

### Local development using Apigee in VS Code

**Note** : This is a limited **preview release** of local development using Apigee in Visual Studio Code (VS Code). To enable and use the features described in this section, contact [Apigee Sales](https://cloud.google.com/contact/?direct=true&pre_product=).

Use Apigee in Visual Studio Code (VS Code) to develop your API proxies and verify the functionality through unit and manual testing (for example, send a request and view the results). 

After you complete your local validation, deploy your API proxy configurations as _archives_ to your Apigee environments. See Deploying API proxies. 

To get started developing your API proxies locally using Apigee in VS Code, see [Building your first API proxy using Apigee in VS Code](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/get-started). 

## Deploying API proxies

You create **environments** in which to deploy API proxies. The distinction between different environments is arbitrary — each environment is simply identified by a different set of network addresses (URLs). The goal is to provide you with a domain in which you can build and verify API proxies before the API is exposed to external developers. For more information, see [About environments and environment groups](https://cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

By deploying your APIs to multiple environments, you can segregate traffic between the API proxies that you are working on in a _test_ environment, and those that are being accessed by external apps at runtime in a _production_ environment. 

Apigee supports the following deployment types in an environment: 

**Type** | **Description**  
---|---  
Proxy  | Develop and test your API proxies in your Apigee development environments, and then deploy them to Apigee integration test and production environments. See [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new).   
Archive  | Develop and test your [programmable API proxies using Apigee in VS Code](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview).   
  
## Adding policies

Apigee enables you to program API behavior without writing any code, by using policies. A policy is like a module that implements a specific, limited management function. Policies are designed to let you add common types of management capabilities to an API easily and reliably. Policies provide features like security, rate-limiting, transformation, and mediation capabilities, saving you from having to code and maintain this functionality on your own. You can also write custom scripts and code (such as JavaScript applications), that extend API proxy functionality and enable you to innovate on top of the basic management capabilities supported by Apigee policies. For more information about Apigee policies, see [What's a policy?](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement)

Apigee provides ready to use polices for various features such as traffic management, security, mediation, and extension policies. To view the complete list of policies available in Apigee, see [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

## Promoting to production

You choose where to deploy an API. For instance, you can promote a revision to a production environment to allow developers to start working with your API. At the same time, you may be iterating multiple revisions in a local or test environment, where you're adding features or fine-tuning policies. Then, when you're ready, you can deploy the new revision to the production environment, overwriting the existing revision in that environment. Using this method, you can always have a live revision of your API available to developers while you're developing and testing new features. 

### Scripting deployment using the Apigee API

Apigee provides a RESTful API that enables you to integrate API proxy deployment and management into your organization's software development lifecycle (SDLC). For example, to ensure that security, reliability, and consistency requirements are met, a common usage of the Apigee API is to write scripts or code that programmatically deploy API proxies and promote them from one environment to another, as part of a larger automated process. 

For more information, see [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). 

### Managing environment resources

Environments provide segregation of data and resources. You can, for example, set up different caches in your `test` and `production` environments that can be accessed only by API proxies executing in that environment. Additionally, API keys that are issued in a test environment are not valid in a production environment, and vice-versa. 

For additional control during promotion, it is recommended that you only iterate on API proxies in a test environment, and make as few changes as necessary to API proxies deployed in a production environment. 

To do so, you need to ensure that certain resources associated with each environment are configured in such a way that they can remain static in an API proxy configuration. 

  * **Key value maps (KVMs)** : If scoped to the environment, you should ensure that naming conventions are used to enable API proxies to store data without requiring configuration changes during promotion. For more information, see [Using key value maps](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps). 
  * **Target URLs** : It is common for API proxies to call different backend URLs during testing and production. You can use TargetServer configurations to create environment-independent TargetEndpoint configurations. For more information, see 
    * [Load balancing across backend servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers) (Cloud development)
    * [Configuring the target servers](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#target-servers) (Local development)
  * **ServiceCallout targets** : Service callouts may use different targets depending on the environment, if, for example, a ServiceCallout in the test environment consumes a demo service. See [ServiceCallout policy](https://cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).



To make API proxy configurations environment-independent, you can also use conditional statements. Conditional statements built with the `environment.name` variable can be used to evaluate the current environment before enforcing a policy or before routing to a URL on the backend. For more information, see [Conditions with flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
