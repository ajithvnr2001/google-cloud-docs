---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/locations/
title: Firestore with MongoDB compatibility locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:58:56.125450+00:00
---

# Firestore with MongoDB compatibility locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Resources ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Firestore with MongoDB compatibility locations

When you provision a Firestore database, you must choose a _location_ for it. To reduce latency and increase availability, store your data close to the users and services that need it.

You can optionally [create multiple databases](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-databases) in your project, each with its own location setting.

Be aware that once you provision a database, you cannot change its location setting.

## Types of locations

You can store your Firestore with MongoDB compatibility data in a _multi-region_ location or a _regional_ location.

### Multi-region locations

Select a multi-region location to maximize the availability and durability of your database.

A multi-region location consists of a defined set of [regions](https://cloud.google.com/docs/geography-and-regions#regions_and_zones) where multiple replicas of the database are stored. Each replica is either a read-write replica which contains all of the data in the database or a witness replica which does not maintain a full set of data but participates in replication.

By replicating the data between multiple regions, data can continue to be served even with the loss of an entire region. Within a region, data is replicated across [zones](https://cloud.google.com/docs/geography-and-regions#regions_and_zones) so that data can continue to be served within that region even with the loss of a zone.

Firestore with MongoDB compatibility supports the following multi-region locations:

Multi-region name | Multi-region description | Read-Write regions | Witness region  
---|---|---|---  
`eur3` | Europe | `europe-west1` (Belgium), `europe-west4` (Netherlands) | `europe-north1` (Finland)  
`nam5` | United States (Central) | `us-central1` (Iowa), `us-central2` (Oklahoma—private Google Cloud region) | `us-east1` (South Carolina)  
`nam7` | United States (Central and East) | `us-central1` (Iowa), `us-east4` (Northern Virginia) | `us-central2` (Oklahoma—private Google Cloud region)  
  
### Regional locations

A regional location is a specific geographic place, such as South Carolina. Data in a regional location is replicated in multiple zones within a [region](https://cloud.google.com/docs/geography-and-regions#regional_resources). All regional locations are separated from other regional locations by at least 100 miles.

Select a regional location for lower costs, for lower write latency if your application is sensitive to latency, or for [co-location with other Google Cloud resources](https://cloud.google.com/about/locations/#products-available-by-region).

Firestore with MongoDB compatibility supports the following regional resource locations:

| Region name| Region description  
---|---|---  
**North America**  
| `us-west1`| Oregon  
| `us-west2`| Los Angeles  
| `us-west3`| Salt Lake City  
| `us-west4`| Las Vegas  
|  `us-central1` | Iowa  
| `northamerica-northeast1`| Montréal  
|  `northamerica-northeast2` | Toronto  
|  `northamerica-south1` | Queretaro  
| `us-east1`| South Carolina  
| `us-east4`| Northern Virginia  
|  `us-east5` | Columbus  
|  `us-south1` | Dallas  
**South America**  
|  `southamerica-west1` | Santiago  
| `southamerica-east1`| São Paulo  
**Europe**  
| `europe-west2`| London  
|  `europe-west1` | Belgium  
|  `europe-west4` | Netherlands  
|  `europe-west8` | Milan  
|  `europe-southwest1` | Madrid  
|  `europe-west9` | Paris  
|  `europe-west12` | Turin  
|  `europe-west10` | Berlin  
| `europe-west3`| Frankfurt  
|  `europe-north1` | Finland  
|  `europe-north2` | Stockholm  
| `europe-central2`| Warsaw  
| `europe-west6`| Zürich  
**Middle East**  
|  `me-central1` | Doha  
|  `me-central2` | Dammam  
|  `me-west1` | Tel Aviv  
**Asia**  
| `asia-south1`| Mumbai  
|  `asia-south2` | Delhi  
| `asia-southeast1`| Singapore  
| `asia-southeast2`| Jakarta  
| `asia-southeast3`| Bangkok  
| `asia-east2`| Hong Kong  
| `asia-east1`| Taiwan  
| `asia-northeast1`| Tokyo  
| `asia-northeast2`| Osaka  
| `asia-northeast3`| Seoul  
**Australia**  
| `australia-southeast1`| Sydney  
|  `australia-southeast2` | Melbourne  
**Africa**  
|  `africa-south1` | Johannesburg  
  
## Location SLA

Your Firestore with MongoDB compatibility location type determines the [Service Level Agreement (SLA)](https://docs.cloud.google.com/firestore/sla) uptime percentage at General Availability (GA):

Covered service | Monthly uptime percentage  
---|---  
Firestore with MongoDB compatibility Multi-Region | >= 99.999%  
Firestore with MongoDB compatibility Regional | >= 99.99%  
  
## Location pricing

Your Firestore with MongoDB compatibility location determines the cost of database operations.

For a comprehensive explanation of pricing per region and per region type, see [Understand Firestore with MongoDB compatibility billing](https://cloud.google.com/firestore/enterprise/pricing).

## View the location of your databases

Use one of the following methods to view the location setting for your databases:

  * Run the [`gcloud firestore databases list`](https://cloud.google.com//sdk/gcloud/reference/firestore/databases/list) command.

  * Open the [database list](https://console.cloud.google.com/firestore/databases) in the Google Cloud console. The location for each database is in the location column.




## Next steps

  * To create a Firestore with MongoDB compatibility database in a specific location, see [Create and manage databases](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/create-databases)

  * For more information about building applications to meet your latency, availability, and durability requirements, refer to [Geography and Regions](https://cloud.google.com/docs/geography-and-regions#multi-regional_resources).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
