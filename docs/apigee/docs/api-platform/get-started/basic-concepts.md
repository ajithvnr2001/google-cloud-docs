---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts/
title: Apigee terminology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:58.255283+00:00
---

# Apigee terminology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee terminology Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page explains some basic Apigee terminology. For additional terms, see the [Glossary](https://docs.cloud.google.com/apigee/docs/api-platform/reference/glossary).

Term | Definition  
---|---  
analytics region | The physical location where analytics data is hosted when [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) is disabled.   
API consumer data region |  A single-region location that Apigee uses for service infrastructure when the control plane location is multi-region. Some Google Cloud services can run only in a single region. If Apigee relies on any of these services, Apigee needs to know in which region these services should be running. This field is relevant only when the control plane location selected during provisioning is multi-region.  
API proxy |  An [ API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy) is an interface between incoming requests and backend services. The proxy executes policies to process all incoming requests and outgoing responses from the backend.   
control plane |  In Apigee, the control plane is part of the infrastructure of configuration of API proxy/environments and underlying infrastructures used to support Apigee functions(like analytics, etc.). The control plane supervises and directs the behavior of the data plane and other Apigee functions.   
control plane data | Any customer data handled directly or indirectly by the control plane. Control plane data is analytics data, API proxies, target servers, truststores and keystores and anything else shared across runtimes.  
control plane location | The physical location in which control plane data is stored.  
data residency | [ Data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee customer/PII data is stored and processed.  
deploy |  You [ deploy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview) an API proxy to an environment to make it accessible to clients on the internet, either publicly or privately, depending on your network configuration.  
encryption key | [Encryption](https://cloud.google.com/learn/what-is-encryption) is used to protect data from being stolen, changed, or compromised and works by scrambling data into a secret code that can only be unlocked with a unique digital key. You can use a [Google-managed](https://docs.cloud.google.com/storage/docs/encryption/default-keys), or [customer-managed](https://docs.cloud.google.com/kms/docs/cmek) encryption key.  
environment |  An Apigee [ environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) is an isolated software execution context, within an organization, where you [ deploy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) API proxies. An environment can scale to meet the demands of the proxies deployed there. You can create multiple environments in an organization.  
environment group |  An [ environment group](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) is a group of Apigee environments with one or more hostnames. The hostname is part of the URL used to [ call API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/test-proxy) deployed to any environment in the environment group.  
Google Cloud projects | [ Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) enable you to create and use Google Cloud services, including managing APIs, enabling billing, adding and removing collaborators, and managing permissions for Google Cloud resources. You need to create a Google Cloud project before you can create and [ provision](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) an Apigee organization.  
organization | An Apigee [ organization](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure) is a container for everything related to Apigee in your Google Cloud project, including API proxies, services, and the resources needed to support them. You [ create your organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org) during provisioning. **Note:** An Apigee organization is _not_ the same as a [ Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).  
policy |  A [ policy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/policy-attachment-and-enforcement) is a processing step that is executed by an API proxy. Apigee provides many pre-defined policies that perform various API tasks, such as transforming message formats or enforcing access control.  
provisioning | [ Provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) is the process for installing and configuring Apigee.   
proxy endpoint |  A proxy endpoint defines the way your API proxy interacts with client applications. You configure the proxy endpoint with a basepath that is part of the URL that your API proxy responds to. The URL has the form `https://hostname/basepath/pathsuffixes`. See [ Create an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy).  
region | A [ specific geographical location](https://docs.cloud.google.com/compute/docs/regions-zones) where you can host your resources.  
runtime database | The internal database where runtime data is stored. Runtime data is the data related to your API requests; data in the database, oauth tokens, API keys, etc.   
runtime disk | The disk used by GKE nodes where runtime data is stored.  
runtime instance |  A [ runtime instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances) is a deployment of the Apigee software. You [ create an instance](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-instance) during provisioning, and can later add more instances. Instances correspond to [Google Cloud regions](https://docs.cloud.google.com/compute/docs/regions-zones), and there can only be one runtime instance per Cloud region.  
runtime plane | In Apigee, [ the runtime plane](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee#componentsofapigeeedge-edgeapiservices) is part of the infrastructure for API creation, security, management, and operations. All API traffic passes through and is processed within the runtime plane.  
target endpoint |  A target endpoint defines the way your API proxy interacts with your backend services. You configure the target endpoint to forward requests to the appropriate backend service, and to define security settings, HTTP or HTTPS protocols, and other connection settings. See [ Changing the target endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/change-endpoint).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
