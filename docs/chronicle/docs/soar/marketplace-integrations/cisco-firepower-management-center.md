---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-firepower-management-center/
title: Cisco Firepower Management Center \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:53.549749+00:00
---

# Cisco Firepower Management Center  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-firepower-management-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco Firepower Management Center

**Important:** Cisco Firepower Management Center was renamed to Cisco Secure Firewall Management Center (FMC).

This document describes how to integrate Cisco Firepower Management Center with Google Security Operations.

## Configure Cisco Firepower Management Center integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
API Root | String | N/A | Yes | API root of the Cisco Firepower Management Center instance.  
Username | String | N/A | Yes | The email address of the user.  
Password | String | N/A | Yes | The user account password.  
Verify SSL | Checkbox | Checked | No | If enabled, verifies if the SSL certificate for the connection to the Cisco Firepower Management Center server is valid.  
  
## Actions

### Block Address

Block an IP address by assigning it to a network group attached to a policy

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Network Group Name | String | N/A | Network object name.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Block Port

Block a port that is assigned to a port group that is attached to a policy.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Port Group Name | String | N/A | Name of the port object group.  
Port | String | N/A | Port to blockExample: 9856  
Port Protocol | String | N/A | Target port protocolExample: TCP  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Block URL

Block the URL by assigning it to a set of URLs attached to it.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
URL Group Name | String | N/A | URL group object name.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Get Addresses List by Name

Get a list of blocked addresses by its name in a particular group of networks.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Network Group Name | String | N/A | The name of the needed network group**.**  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
addresses_list | True/False | addresses_list:False  
  
##### JSON Result

N/A

### Get Ports List by Name

Get a list of blocked ports by its name for a particular group.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Port Group Name | String | N/A | The name of the needed ports group.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
ports_list | N/A | N/A  
  
##### JSON Result

N/A

### Get URL List by Name

Get a list of URLs by its name from a specific group.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
URL Group Name | String | N/A | The name of the needed URL group.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
urls_list | N/A | N/A  
  
##### JSON Result

N/A

### Ping

Test Connectivity.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Unblock Address

Unblock an address in Cisco Firepower.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Network Group Name | String | N/A | Network object name.  
  
#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Unblock Port

Remove a port from a group of blocked ports.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Port Group Name | String | N/A | Name of the port object group.  
Port | String | N/A | Target portExample: 9856  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

### Unblock URL

Remove a URL from a group of blocked URLs.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
URL Group Name | String | N/A | URL group object name.  
  
#### Use cases

N/A

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

N/A

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
