---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/using-data-residency-with-apigee-hybrid/
title: Using data residency with Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:51:12.669935+00:00
---

# Using data residency with Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/using-data-residency-with-apigee-hybrid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using data residency with Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/using-data-residency-with-apigee-hybrid.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/using-data-residency-with-apigee-hybrid.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/using-data-residency-with-apigee-hybrid.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/using-data-residency-with-apigee-hybrid.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/using-data-residency-with-apigee-hybrid.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/using-data-residency-with-apigee-hybrid.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/using-data-residency-with-apigee-hybrid.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/using-data-residency-with-apigee-hybrid.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/using-data-residency-with-apigee-hybrid.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/using-data-residency-with-apigee-hybrid.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/using-data-residency-with-apigee-hybrid.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/using-data-residency-with-apigee-hybrid.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/using-data-residency-with-apigee-hybrid.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/using-data-residency-with-apigee-hybrid.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/using-data-residency-with-apigee-hybrid.html)



## Overview

Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored. With data residency, selecting the control plane location ensures that all customer content is stored within the specified region. 

For an overview of data residency for Apigee, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

##  Data residency with Apigee hybrid 

**Note:** [Apigee API analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview) and the [Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) are not supported in Apigee hybrid organizations with data residency enabled.

Starting with hybrid version 1.12, you can use Data residency with new Apigee hybrid installations. You cannot convert an existing installation to use data residency.

### When creating your Apigee org

Creating your Apigee organization using data residency requires the following differences. See [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-provision). 

  * **Control plane location** : You need to specify the location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). 

The control plane location is the location of the service endpoint location, for example `us` for United States. 

The following table lists available hosting jurisdictions and regions for the Apigee control plane. 

### Americas

Control plane hosting jurisdiction description | Control plane hosting jurisdiction name | Details  
---|---|---  
United States |  `us (multiple regions in United States)` | Service endpoint: `apigee.us.rep.googleapis.com` **Note:** See also [Use VPC Service Controls with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-vpc-sc).   
Canada |  `ca (multiple regions in Canada)` | Service endpoint: `ca-apigee.googleapis.com`  
Consumer data region description | Consumer data region name | Details  
---|---|---  
Iowa |  `us-central1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Oregon |  `us-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Los Angeles |  `us-west2` |   
Salt Lake City |  `us-west3` |   
Las Vegas |  `us-west4` |   
South Carolina |  `us-east1` |   
Northern Virginia |  `us-east4` |   
Columbus |  `us-east5` |   
Dallas |  `us-south1` |   
Montréal |  `northamerica-northeast1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Toronto |  `northamerica-northeast2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Europe

Control plane hosting jurisdiction description | Control plane hosting jurisdiction name | Details  
---|---|---  
European Union |  `eu (multiple regions in the European Union)` | Service endpoint: `apigee.eu.rep.googleapis.com` **Note:** See also [Use VPC Service Controls with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-vpc-sc).  
Germany |  `de (multiple regions in Germany)` | Service endpoint: `de-apigee.googleapis.com`  
France |  `fr (single region europe-west9)` | Service endpoint: `fr-apigee.googleapis.com`  
Switzerland |  `ch (single region europe-west6)` | Service endpoint: `ch-apigee.googleapis.com`  
Consumer data region description | Consumer data region name | Details  
---|---|---  
Belgium |  `europe-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Frankfurt |  `europe-west3` |   
Netherlands |  `europe-west4` |   
Zurich |  `europe-west6` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Milan |  `europe-west8` |   
Paris |  `europe-west9` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Turin |  `europe-west12` |   
Warsaw |  `europe-central2` |   
Madrid |  `europe-southwest1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
Finland |  `europe-north1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Asia-Pacific

Control plane hosting jurisdiction description | Control plane hosting jurisdiction name | Details  
---|---|---  
Australia |  `au (multiple regions in Australia)` | Service endpoint: `au-apigee.googleapis.com`  
India |  `in (multiple regions in India)` | Service endpoint: `apigee.in.rep.googleapis.com` **Note:** See also [Use VPC Service Controls with data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-vpc-sc).  
Japan |  `jp (multiple regions in Japan)` | Service endpoint: `jp-apigee.googleapis.com`  
Consumer data region description | Consumer data region name | Details  
---|---|---  
Sydney |  `australia-southeast1` |   
Melbourne |  `australia-southeast2` |   
Mumbai |  `asia-south1` |   
Delhi |  `asia-south2` |   
Tokyo |  `asia-northeast1` |   
Osaka |  `asia-northeast2` |   
  
### Middle East

Control plane hosting juridiction description | Control plane hosting jurisdiction name | Details  
---|---|---  
Qatar |  `qa (single region me-central1)` | Service endpoint: `qa-apigee.googleapis.com`  
Saudi Arabia |  `sa (single region me-central2)` | Service endpoint: `sa-apigee.googleapis.com`  
Israel |  `il (single region me-west1)` | Service endpoint: `il-apigee.googleapis.com`  
Consumer data region description | Consumer data region name | Details  
---|---|---  
Doha  | `me-central1` |   
Dammam | `me-central2` |   
Tel Aviv | `me-west1` |   
  
  * **Consumer data region** : You need to specify a region where API consumer data is stored. This must be a sub-region of the control plane region. For a list of available consumer data regions, see[ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#consumer-data-region). 
  * **Billing type** : You can only use data residency with paid subscription orgs. 



### When creating environments

When creating environments in and installation using data residency, you must create them in the control plane location. See [Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-add-environment). 

### Overrides file adjustments

When using data residency, you must add the [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref#contractprovider) configuration property to each overrides file and point it to the path for APIs in the control plane location. For example: 
    
    
    instanceID: "my_hybrid_example"
    namespace: apigee
    
    gcp:
      projectID: hybrid-example
      region: us-central1
    
    k8sCluster:
      name: apigee-hybrid
      region: us-central1
    
    org: hybrid-example
    
    **contractProvider: https://us-apigee.googleapis.com**
    

See [Step 6: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-overrides)

### When calling the Apigee APIs

When you make `curl` calls to Apigee APIs to perform tasks in your hybrid installation, you will need to call APIs from within the control plane location. For example:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
      "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/$ORG_NAME/envgroups"

or
    
    
    curl -H "Authorization: Bearer $TOKEN" \
      "https://**us** -apigee.googleapis.com/v1/organizations/my-hybrid-org/envgroups"

**Note:** If you are using forward proxy with data residency, you must allowlist: `CONTROL_PLANE_LOCATION-apigee.googleapis.com` for each control plane location. 

If your security protocols permit, you can allowlist `*-apigee.googleapis.com`

For a list of specific URLs required by Apigee hybrid, see [Google Cloud URLs to allow for Hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/allow-gcp-urls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
