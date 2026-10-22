---
url: https://docs.cloud.google.com/assured-workloads/docs/locations/
title: Assured Workloads locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:26.678202+00:00
---

# Assured Workloads locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/locations/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Resources ](https://docs.cloud.google.com/assured-workloads/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assured Workloads locations

This page describes the locations where Assured Workloads workloads and service-specific resources can be deployed. For more information about regions in Google Cloud, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions). To learn about supported locations for Sovereign Controls by Partners data boundaries, see [Sovereign Controls by Partners locations](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/locations).

The following concepts about locations are important in Assured Workloads:

  * **Workload location** : The location where a [`Workload`](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload) is deployed. This `Workload` type represents [an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder), and defines the folder's data boundary and other configuration details.
  * **Service-specific resource location** : The location where resources for a Google Cloud service are deployed in an Assured Workloads folder, such as a Cloud Storage blob or a Compute Engine VM. In Assured Workloads, the [`gcp.resourceLocations` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) restricts resource locations to those allowed by a given data boundary. For example, the [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary) enforces that all service-specific resources are deployed to the `us` multi-region or one of its included regions.



Available workload locations and service-specific resource locations are listed in the following sections.

## Americas

The following table lists the Americas regions where Assured Workloads is available.

Region | Region description | Supported workload location | Supported resource location  
---|---|---|---  
`us-central1` | Iowa, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-east1` | South Carolina, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-east4` | Northern Virginia, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-east5` | Ohio, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high), and  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate) | check  
`us-south1` | Texas, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high), and  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate) | check  
`us-west1` | Oregon, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-west2` | Los Angeles, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-west3` | Salt Lake City, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`us-west4` | Las Vegas, US | [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
`northamerica-northeast1` | Montréal, Canada | [Canada Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary),  
[Canada Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary-support),  
[Data Boundary for Canada Controlled Goods Program (CGP)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-controlled-goods-program), and  
[Data Boundary for Canada Protected B](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-protected-b) | check  
`northamerica-northeast2` | Toronto, Canada | [Canada Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary),  
[Canada Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary-support),  
[Data Boundary for Canada Controlled Goods Program (CGP)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-controlled-goods-program), and  
[Data Boundary for Canada Protected B](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-protected-b) | check  
`southamerica-east1` | São Paulo, Brazil | [Brazil Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/brazil-data-boundary) | check  
`southamerica-west1` | Santiago, Chile | [Chile Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/chile-data-boundary) | check  
  
## Europe

The following table lists the Europe regions where Assured Workloads is available.

Region | Region description | Supported workload location | Supported resource location  
---|---|---|---  
`europe-central2` | Warsaw, Poland | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west1` | St. Ghislain, Belgium | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west2` | London, UK | [UK Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/uk-data-boundary) | check  
`europe-west3` | Frankfurt, Germany | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west4` | Eemshaven, Netherlands | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west6` | Zurich, Switzerland | [Switzerland Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/switzerland-data-boundary) | [Switzerland Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/switzerland-data-boundary-access-justifications) | check  
`europe-west8` | Milan, Italy | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | check  
`europe-west9` | Paris, France | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west10` | Berlin, Germany | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-west12` | Turin, Italy | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) | check  
`europe-southwest1` | Madrid, Spain | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary) and  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support) | check  
`europe-north1` | Hamina, Finland | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`europe-north2` | Stockholm, Sweden | [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
  
## Asia Pacific

The following table lists the Asia Pacific regions where Assured Workloads is available.

Region | Region description | Supported workload location | Supported resource location  
---|---|---|---  
`asia-south1` | Mumbai, India | [India Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/india-data-boundary) | check  
`asia-south2` | Delhi, India | [India Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/india-data-boundary) | check  
`asia-southeast1` | Jurong West, Singapore | [Singapore Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/singapore-data-boundary) | check  
`asia-southeast2` | Jakarta, Indonesia | [Indonesia Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/indonesia-data-boundary) | check  
`asia-east1` | Changhua County, Taiwan | [Taiwan Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/taiwan-data-boundary) | check  
`asia-east2` | Hong Kong | [Hong Kong Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/hong-kong-data-boundary) | check  
`asia-northeast1` | Tokyo, Japan | [Japan Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/japan-data-boundary) | check  
`asia-northeast2` | Osaka, Japan | [Japan Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/japan-data-boundary) | check  
`asia-northeast3` | Seoul, South Korea | [South Korea Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/south-korea-data-boundary) | check  
`australia-southeast1` | Sydney, Australia | [Australia Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary) and  
[Australia Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary-support) | check  
`australia-southeast2` | Melbourne, Australia | [Australia Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary) and  
[Australia Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/australia-data-boundary-support) | check  
  
## Africa

The following table lists the Africa regions where Assured Workloads is available.

Region | Region description | Supported workload location | Supported resource location  
---|---|---|---  
`africa-south1` | Johannesburg, South Africa | [South Africa Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/south-africa-data-boundary) | check  
  
## Middle East

The following table lists the regions in the Middle East where Assured Workloads is available.

Region | Region description | Supported workload location | Supported resource location  
---|---|---|---  
`me-central1` | Doha, Qatar | [Qatar Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/qatar-data-boundary) | check  
`me-central2` | Dammam, Kingdom of Saudi Arabia (KSA) | [KSA Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/ksa-data-boundary-access-justifications) | check  
`me-west1` | Tel Aviv, Israel | [Israel Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/israel-data-boundary) and  
[Israel Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/israel-data-boundary-support) | check  
  
## Multi-regions

The following table lists the multi-regions where Assured Workloads is available.

Multi-region | Multi-region description | Supported workload location | Supported resource location  
---|---|---|---  
`ca` | Data centers within Canada. The following regions are included:  


  * `northamerica-northeast1`
  * `northamerica-northeast2`

  
| [Canada Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-data-boundary-support),   
[Data Boundary for Canada Controlled Goods Program (CGP)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-controlled-goods-program), and  
[Data Boundary for Canada Protected B](https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-protected-b) | check  
`europe` | Data centers within [member states](https://europa.eu/european-union/about-eu/countries_en) of the European Union. The following regions are included:  


  * `europe-central2`
  * `europe-north1`
  * `europe-north2`
  * `europe-west1`
  * `europe-west3`
  * `europe-west4`
  * `europe-west9`
  * `europe-west10`

  
| [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary),  
[EU Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support), and  
[EU Data Boundary with Access Justifications](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-access-justifications) | check  
`us` | Data centers within the United States. The following regions are included:  


  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`

  
| [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary),  
[US Data Boundary and Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support),  
[Data Boundary for CJIS](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis),  
[Data Boundary for FedRAMP High](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high),  
[Data Boundary for FedRAMP Moderate](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate),  
[Data Boundary for IL2](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2),  
[Data Boundary for IL4](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4),  
[Data Boundary for IL5](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5),  
[Data Boundary for IRS 1075](https://docs.cloud.google.com/assured-workloads/docs/control-packages/irs-1075),  
[Data Boundary for ITAR](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar),  
[US Data Boundary for Healthcare and Life Sciences](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences), and  
[US Data Boundary for Healthcare and Life Sciences with Support](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-healthcare-life-sciences-support) | check  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
