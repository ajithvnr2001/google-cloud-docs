---
url: https://docs.cloud.google.com/apigee/docs/locations/
title: Apigee locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:16.668112+00:00
---

# Apigee locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee locations Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee organization resources can be created in many [locations](https://cloud.google.com/about/locations). These locations represent the geographical _regions_ where Apigee resources, such as the Apigee runtime infrastructure and Apigee API Analytics data, are stored and accessed. Google manages these resources so that they are available redundantly in [all zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Apigee resources are located. You should consider the locations where Apigee is available and the [locations](https://cloud.google.com/about/locations#region) of the other Google Cloud products and services that Apigee may use. Using services across multiple locations can affect Apigee's latency and its [pricing](https://docs.cloud.google.com/apigee/pricing). 

## Select a runtime region

You select the Apigee runtime hosting region when you provision your Apigee instance. You can select the runtime region when you provision using the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee) or using the API. The following resources outline the steps required to select a runtime hosting region, based on your organization type: 

Organization type | Provisioning method | Documentation  
---|---|---  
Evaluation organization |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Provisioning an eval org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs#apigee-evaluation-organization)  
---  
[Provision an eval org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval#create-org) [Provision an eval org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org)  
Subscription organization |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting)  
---  
[Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#runtime-instance) [Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#runtime-instance)  
Pay-as-you-go organization |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)  
---  
[Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo#runtime-instance) [Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo#runtime-instance)  
  
## Available Apigee runtime regions

The following table lists available regions for the Apigee runtime. 

### Americas

Region description | Region name | Details  
---|---|---  
Iowa |  `us-central1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Oregon |  `us-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Los Angeles |  `us-west2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Salt Lake City |  `us-west3` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Las Vegas |  `us-west4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Montréal |  `northamerica-northeast1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Toronto |  `northamerica-northeast2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Mexico |  `northamerica-south1` |  | South Carolina |  `us-east1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Northern Virginia |  `us-east4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Columbus |  `us-east5` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Dallas |  `us-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Santiago |  `southamerica-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
São Paulo |  `southamerica-east1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Europe

Region description | Region name | Details  
---|---|---  
Belgium |  `europe-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
London |  `europe-west2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Frankfurt |  `europe-west3` |  [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Netherlands |  `europe-west4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Zurich |  `europe-west6` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Milan |  `europe-west8` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Paris |  `europe-west9` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Berlin |  `europe-west10` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supportedtd>  
Turin |  `europe-west12` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Warsaw |  `europe-central2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Madrid |  `europe-southwest1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Finland |  `europe-north1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Stockholm |  `europe-north2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
  
### Asia-Pacific

Region description | Region name | Details  
---|---|---  
Sydney |  `australia-southeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Melbourne |  `australia-southeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Mumbai |  `asia-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Delhi |  `asia-south2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Singapore |  `asia-southeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Jakarta |  `asia-southeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Bangkok |  `asia-southeast3` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Tokyo |  `asia-northeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Osaka |  `asia-northeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Seoul |  `asia-northeast3` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Taiwan |  `asia-east1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Hong Kong |  `asia-east2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Middle East

Region description | Region name | Details  
---|---|---  
Doha | `me-central1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Dammam | `me-central2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Tel Aviv | `me-west1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Africa

Region description | Region name | Details  
---|---|---  
Johannesburg | `africa-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
## Select an Apigee API Analytics region

You select the region where your Apigee API Analytics data is stored when you provision your Apigee organization. You can select the runtime region when you provision using the [Apigee UI in Cloud console](https://console.cloud.google.com/apigee) or using the API. The following resources outline the steps required to select an Apigee API Analytics region, based on your organization type: 

Organization type | Provisioning method | Documentation  
---|---|---  
Evaluation |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Provisioning an eval org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs#apigee-evaluation-organization)  
---  
[Provision an eval org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-eval#create-org) [Provision an eval org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval#create-org)  
Subscription |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting)  
---  
[Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) [Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org)  
Pay-as-you-go |  | Apigee UI in Cloud console  
---  
Command line interface  
| [Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)  
---  
[Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo#create-org) [Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo#create-org)  
  
## Available Apigee API Analytics regions

The following table lists available regions for Apigee API Analytics. 

### Americas

Region description | Region name | Details  
---|---|---  
Iowa |  `us-central1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Oregon |  `us-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Los Angeles |  `us-west2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Salt Lake City |  `us-west3` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Las Vegas |  `us-west4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Montréal |  `northamerica-northeast1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Toronto |  `northamerica-northeast2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
South Carolina |  `us-east1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Northern Virginia |  `us-east4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Columbus |  `us-east5` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Dallas |  `us-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Santiago |  `southamerica-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
São Paulo |  `southamerica-east1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Europe

Region description | Region name | Details  
---|---|---  
Belgium |  `europe-west1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)  
London |  `europe-west2` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Frankfurt |  `europe-west3` |  [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Netherlands |  `europe-west4` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Zurich |  `europe-west6` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Milan |  `europe-west8` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Paris |  `europe-west9` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Berlin |  `europe-west10` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Turin |  `europe-west12` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Madrid |  `europe-southwest1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Warsaw |  `europe-central2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Finland |  `europe-north1` |  ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Asia-Pacific

Region description | Region name | Details  
---|---|---  
Sydney |  `australia-southeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Melbourne |  `australia-southeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Mumbai |  `asia-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Delhi |  `asia-south2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Singapore |  `asia-southeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Jakarta |  `asia-southeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Taiwan |  `asia-east1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Hong Kong |  `asia-east2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Tokyo |  `asia-northeast1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Osaka |  `asia-northeast2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Seoul |  `asia-northeast3` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Middle East

Region description | Region name | Details  
---|---|---  
Doha | `me-central1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Dammam | `me-central2` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
Tel Aviv | `me-west1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
### Africa

Region description | Region name | Details  
---|---|---  
Johannesburg | `africa-south1` | [API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) supported  
  
## Select an Apigee API control plane hosting jurisdiction

You select the specific Apigee control plane hosting jurisdiction where your data is stored when you provision your Apigee instance. Note that a jurisdiction refers to a location within a geopolitical boundary that may span more than one region.

You can select the control plane hosting jurisdiction when you provision using the Apigee UI in Google Cloud console, or using the API. The following resources outline the steps required to select a control plane hosting jurisdiction, based on your organization type: 

Organization type | Provisioning method | Documentation  
---|---|---  
Subscription organization |  | Apigee UI in Cloud console  
---  
Command line interface  
| [ Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-hosting)  
---  
[ Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) [ Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered#create-org)science  
Pay-as-you-go organization |  | Apigee UI in Cloud console  
---  
Command line interface  
| [ Step 3: Configure hosting and encryption](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-hosting)  
---  
[ Provision a paid org with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo#create-org) [ Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo#create-org)science  
  
## Available Apigee API control plane hosting jurisdictions

The Apigee control plane directly binds to the API host name. `apigee.googleapis.com` has a global control plane. If you want to use a regionalized control plane, you need to use the [regional endpoints for data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint). 

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
