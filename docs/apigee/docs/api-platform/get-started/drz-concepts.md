---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts/
title: Introduction to data residency \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:44.759914+00:00
---

# Introduction to data residency  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Introduction to data residency Stay organized with collections  Save and categorize content based on your preferences. 

For many industry verticals and enterprises, using a cloud offering results in increased scrutiny from security and compliance teams. The following questions are often asked:

  * Where is data stored?
  * What data is stored in the cloud?
  * Who has access to the data?
  * How is data handled during processing or transmission?



In addition to this, many countries have passed data privacy laws that prohibit Personally Identifiable Information (PII) data from being stored outside the country or region.

This document describes data residency for Apigee and how it helps you to meet compliance and regulatory requirements.

**Note** : Apigee has achieved [FedRAMP High authorization](https://cloud.google.com/security/compliance/fedramp), successfully meeting standards required for data residency. For more information, see FedRAMP compliance and data residency. 

## Overview

Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is being:

  * Stored (at rest) 
  * Processed (in use) 
  * Transmitted (in transit) 



**Tip:** In this documentation, we use **advanced data residency** to refer to compliance and regulatory requirements for data that is being processed (in use) or transmitted (in transit) in addition to being stored (at rest). See About advanced data residency.

You enable data residency when provisioning an Apigee organization. During provisioning, you select the region where all customer content is stored. See [Provision your organization with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision). 

Once the Apigee organization is provisioned with data residency, Apigee organization admins must do the following: 

  * Inform Apigee users, including API developers and other admins, about the data residency configuration and requirements. Apigee users must follow the guidelines in [Use Apigee with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-use-apigee).
  * Set the location organization policy as described in [Restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 



Note the following: 

  * You can't enable data residency for an Apigee organization that is already provisioned.
  * By default, the control plane is a global entity unless you select data residency (regionalization) at the time the Apigee organization is created. 
  * Once you select data residency and the control plane location, it can't be changed. If you later need a different location, you will need to create a new Google Cloud project. 



See also [Google Cloud Services with Data Residency](https://cloud.google.com/terms/data-residency). 

## About advanced data residency

Advanced data residency refers to compliance and regulatory requirements for data that is being processed (in use) or transmitted (in transit) in addition to being stored (at rest).

To comply with advanced data residency, the following actions are required when setting up and using Apigee. 

Create Assured Workloads  | Provision your organization | Use Apigee  
---|---|---  
Google Cloud admin creates an Assured Workloads folder in the Google Cloud organization and applies a control package. The control package automatically sets the control plane location and organization policy constraints that enforce the regional data boundaries.  See [Create an Assured Workloads folder](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#create-assured-workload-folder).  | Apigee organization admin provisions your paid organization with advanced data residency using the location-based jurisdictional console to access the Apigee UI or the regional endpoint to access the Apigee APIs.  See [Provision your organization with advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#provision-advanced-drz).  | Apigee users use the jurisdictional console to access the Apigee UI or regional endpoint to access the APIs.  See [Use Apigee with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-use-apigee).   
  
## Support for data residency

The following table summarizes the features that are supported and not supported for Apigee with data residency.

Supported | Not supported  
---|---  
  
  * [ Apigee organizations (Subscription or Pay-as-you-go)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro)
  * [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid) for data residency at rest only, as described in Apigee hybrid data residency
  * [Operations anomalies](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/operations-anomalies-overview) for non-hybrid Subscription organizations
  * [ Monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview)
  * [API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview)
  * [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security)
  * [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub). 
  * [ Data collectors](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors) for Subscription and Pay-as-you-go organizations, and hybrid versions 1.14.0 and later (at rest only)

| 
* [ Data Studio Integration](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/looker)
* Preview- or Beta-release features, such as [Shadow API Discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery)
* [ Eval organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval)
* [ Integrated portals](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal)
* [Apigee Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/concepts)
* End-user analysis features, such as the [Devices dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/devices-dashboard) and the [Geomap dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/geomap-dashboard), aren't supported with advanced data residency
* Developer analysis features, such as the [Developer engagement dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/partner-engagement-dashboard) and [Traffic composition dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/traffic-composition-dashboard), aren't supported with advanced data residency
* [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid) isn't supported for advanced data residency  
  
### FedRAMP compliance and data residency

Apigee is authorized as a FedRAMP High service for organizations where data residency is enabled. If you choose to enable data residency when provisioning an Apigee Subscription or Pay-as-you-go organization, the following services are in scope under Apigee's FedRAMP Authority To Operate (ATO): 

  * The regionalized Apigee organization's [control plane, runtime plane, and analytics](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts).
  * The regionalized Apigee hybrid organization's [control plane and analytics](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts).



The following Apigee offerings are _not in scope_ under Apigee's FedRAMP ATO: 

  * [API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview)
  * [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security)
  * [Integrated portals](https://docs.cloud.google.com/apigee/docs/api-platform/publish/intro-portals#integrated-portal)
  * [Apigee evaluation organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval)
  * [Apigee data collectors](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors)

For more information about the significance of a FedRAMP ATO, see [FedRAMP Compliance](https://cloud.google.com/security/compliance/fedramp). 

### Apigee hybrid data residency

**Notes:**

  * Advanced data residency is not supported for Apigee hybrid.
  * Apigee hybrid with data residency at rest enabled doesn't support distributed trace. See the [Known Issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-distributed-trace-drz).



You can configure new Apigee hybrid installations to use data residency, starting with hybrid version 1.12. See [Using data residency with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/latest/using-data-residency-with-apigee-hybrid). 

Apigee hybrid [version 1.14.0](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1140) and later with data residency enabled supports [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security), [Apigee API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview), and the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview). 

## Choose regions for data residency

You choose the regions (physical location) for the [control plane data](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#control-plane-data) based on your data residency requirements as follows: 

**Data residency requirements** | **How to choose region**  
---|---  
Data residency at rest only  | When provisioning your Apigee organization, your Apigee admin sets the **control plane location** to the required region (for example, `us`). See [Provision your organization with data residency at rest only](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#provision-at-rest-drz).   
Advanced data residency (in use and in transit)  | When creating an Assured Workloads folder for the Google Cloud organization, your Google Cloud admin selects a **control package** to define the regional data boundaries. During provisioning the control plane location is set automatically and other locations are filtered based on the control package selected. See [Provision your organization with advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#provision-advanced-drz).   
  
During provisioning, you must also specify a **single region** (for example, `us-west1`) for other consumer services that can run only in a single region, such as Analytics reports. 

All resources must be within the region specified. For example, if you select `us` for the control plane location, the other Apigee resources, such as the runtime instance, referencing CMEK, endpoint attachment, and so on, must also be within the `us` region. 

## Use the jurisdictional console

When provisioning or using Apigee with advanced data residency, you must use one of the jurisdictional Google Cloud consoles to access the Apigee UI based on your [location](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#locations).

For example, the jurisdictional console URL for the United States region is: `console.us.cloud.google.com`

When provisioning or using Apigee with data residency at rest only, you can use either the global or jurisdictional console. To use the jurisdictional console, the Apigee organization must have been provisioned within one of the [supported locations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#locations).

The benefits of using the jurisdictional Google Cloud console are as follows: 

  * Simplifies the provisioning UI by automatically setting the control plane location and filtering the region selectors accordingly.
  * Alters the UI interactions with Google Cloud services based on the data residency requirements, such as filtering region selectors and the options available for service endpoint attachments to prevent Apigee from connecting to a private target using Private Service Connect (PSC) if the target is outside the permitted region.



For information about how to access the jurisdictional console, see [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console). 

## Use regional endpoints for data residency

A [service endpoint](https://docs.cloud.google.com/apis/design/glossary#api-service-endpoint), or hostname, is a base URL that specifies the network address of an API service. The Apigee API service endpoint is `apigee.googleapis.com`. This is the global endpoint used when data residency is not supported. 

To support data residency, you'll need to use regional endpoints. The following sections describe how to use regional endpoints for data residency at rest only and advanced data residency.

### Use regional endpoints for data residency at rest only

To access the Apigee API with data residency at rest only, use the following regional endpoint: `CONTROL_PLANE_LOCATION-apigee.googleapis.com`

Where **CONTROL_PLANE_LOCATION** is the physical location at which Apigee control plane data will be stored. For a list of available control plane locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#control-plane-location). 

**Note:** Alternatively, if the Apigee organization was provisioned within one of the supported locations you can use the regional endpoints provided for advanced data residency, described in the following section.

For example, the following shows the curl call used to create an organization using the regional endpoint for the United States: 
    
    
    curl "https://**us-apigee.googleapis.com** /v1/organizations?parent=projects/PROJECT_ID" ...

### Use regional endpoints for advanced data residency

To access the Apigee API with advanced data residency, use the following regional endpoint:

`apigee.CONTROL_PLANE_LOCATION.rep.googleapis.com`

Where CONTROL_PLANE_LOCATION is the physical location where Apigee control plane data is stored.

The following list the supported control plane locations and their corresponding regional endpoints: 

**Location** | **Regional endpoint**  
---|---  
United States (US)  | `apigee.us.rep.googleapis.com`  
European Union (EU)  | `apigee.eu.rep.googleapis.com`  
India (IN)  | `apigee.in.rep.googleapis.com`  
  
For example, the following shows the curl call used to create an organization using the regional endpoint for the United States: 
    
    
    curl "https://**apigee.us.rep.googleapis.com** /v1/organizations?parent=projects/PROJECT_ID" ...

## Encryption and data residency

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using encryption keys that are owned and managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK). See [ Introduction to CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts). 

## Use organization policy constraints with data residency

Google Cloud's [ organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) make it possible to define a set of locations where location-based Google Cloud resources can be created for your Google Cloud organization. If you have a Google Cloud [ organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy) that uses a [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) (`constraints/gcp.resourceLocations`), the constraint will apply to the following Apigee resources that are created when Apigee is provisioned: 

  * [Control plane](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions)
  * [Consumer data](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions)
  * [Runtime ](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-runtime-regions)
  * [Endpoints attachment](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#create-an-endpoint-attachment)
  * [Analytics](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions)



If you are provisioning a new Apigee organization within a Google Cloud project with a resource location constraint applied, you must ensure that the location constraint is compatible with the control plane location specified for your Apigee organization: 

  * If you provision an Apigee organization _without_ data residency, the resource location constraint in your Google Cloud organization policy must be set to `global`. Because the Apigee control plane is a global entity by default, provisioning will fail if a constraint other than `global` is applied.
  * If you provision an Apigee organization _with_ data residency, confirm that any resource location constraint that may be set in your Google Cloud organization policy does not exclude the region you select for your control plane data. Otherwise, provisioning will fail.



## Data residency and FedRAMP compliance

Apigee is authorized as a FedRAMP High service for organizations where data residency is enabled. If you choose to enable data residency when provisioning an Apigee Subscription or Pay-as-you-go organization, the following services are in scope under Apigee's FedRAMP Authority To Operate (ATO): 

  * The regionalized Apigee organization's [control plane, runtime plane, and analytics](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts).
  * The regionalized Apigee hybrid organization's [control plane and analytics](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts).



The following Apigee offerings are _not in scope_ under Apigee's FedRAMP ATO: 

  * [API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview)
  * [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security)
  * [Integrated portals](https://docs.cloud.google.com/apigee/docs/api-platform/publish/intro-portals#integrated-portal)
  * [Apigee evaluation organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval)
  * [Apigee data collectors](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/data-collectors)

For more information about the significance of a FedRAMP ATO, see [FedRAMP Compliance](https://cloud.google.com/security/compliance/fedramp). 

## Use VPC Service Controls with data residency

To use VPC Service Controls with data residency at rest, you must use the following regional endpoint: `CONTROL_PLANE_LOCATION-apigee.googleapis.com`

At this time, you can't use VPC Service Controls with advanced data residency. For advanced data residency, using the `apigee.CONTROL_PLANE_LOCATION.rep.googleapis.com` endpoint will require you to create a private connection between Apigee and backend target services use [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
