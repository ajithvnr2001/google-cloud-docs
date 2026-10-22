---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness/
title: RSA NetWitness \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:44.582301+00:00
---

# RSA NetWitness  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RSA NetWitness

**Deprecated:** This integration is deprecated. Use the RSA NetWitness Platform integration instead.

## Configure RSA NetWitness Integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Ping

#### Description

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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Query NetWitness for Events Around Host

#### Description

Assign an issue to a user.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | Logic-When to apply  
---|---  
payload.req | Returns if it exists in JSON result  
org.src | Returns if it exists in JSON result  
domain.src | Returns if it exists in JSON result  
netname | Returns if it exists in JSON result  
lifetime | Returns if it exists in JSON result  
rid | Returns if it exists in JSON result  
payload | Returns if it exists in JSON result  
size | Returns if it exists in JSON result  
country.src | Returns if it exists in JSON result  
service | Returns if it exists in JSON result  
longdec.src | Returns if it exists in JSON result  
eth.src | Returns if it exists in JSON result  
tcp.dstport | Returns if it exists in JSON result  
direction | Returns if it exists in JSON result  
medium | Returns if it exists in JSON result  
ip.dst | Returns if it exists in JSON result  
latdec.src | Returns if it exists in JSON result  
city.src | Returns if it exists in JSON result  
alert | Returns if it exists in JSON result  
sessionid | Returns if it exists in JSON result  
eth.type | Returns if it exists in JSON result  
ip.src | Returns if it exists in JSON result  
tcp.flags | Returns if it exists in JSON result  
eth.dst | Returns if it exists in JSON result  
did | Returns if it exists in JSON result  
tcp.srcport | Returns if it exists in JSON result  
packet | Returns if it exists in JSON result  
streams | Returns if it exists in JSON result  
time | Returns if it exists in JSON result  
ip.proto | Returns if it exists in JSON result  
****  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
    {
    "EntityResult":
    [
    {
    "payload.req": "0",
    "org.src": "Blue",
    "domain.src": "example.com",
    "netname": "other src",
    "lifetime": "0",
    "rid": "29",
    "payload": "0",
    "size": "66",
    "country.src": "France",
    "service": "0",
    "longdec.src": "-2.2595",
    "eth.src": "11:1C:1C:11:22:87",
    "tcp.dstport": "40906",
    "direction": "inbound",
    "medium": "1",
    "ip.dst": "1.1.1.1",
    "latdec.src": "48.3175",
    "city.src": "Tru00e9meur",
    "alert": "test App rule",
    "sessionid": "29",
    "eth.type": "2048",
    "ip.src": "1.1.1.1",
    "tcp.flags": "20",
    "eth.dst": "11:11:11:B1:1B:11",
    "did": "nwappliance5805",
    "tcp.srcport": "80",
    "packets": "1",
    "streams": "1",
    "time": 1547013286,
    "ip.proto": "6"
    },
    {
    "Entity": "example.com"
    }]
    

### Query NetWitness for Events Around IP

#### Description

Run a query on RSA NetWitness to retrieve all events for a specific query (conditions) for a given IP address in the alert.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
payload.req | Returns if it exists in JSON result  
ubc.req | Returns if it exists in JSON result  
netname | Returns if it exists in JSON result  
lifetime | Returns if it exists in JSON result  
rid | Returns if it exists in JSON result  
payload | Returns if it exists in JSON result  
size | Returns if it exists in JSON result  
service | Returns if it exists in JSON result  
mcb.req | Returns if it exists in JSON result  
eth.src | Returns if it exists in JSON result  
tcp.flags | Returns if it exists in JSON result  
tcp.dstport | Returns if it exists in JSON result  
direction | Returns if it exists in JSON result  
medium | Returns if it exists in JSON result  
ip.dst | Returns if it exists in JSON result  
alert | Returns if it exists in JSON result  
sessionid | Returns if it exists in JSON result  
eth.type | Returns if it exists in JSON result  
ip.src | Returns if it exists in JSON result  
Eth.dst | Returns if it exists in JSON result  
did | Returns if it exists in JSON result  
tcp.srcport | Returns if it exists in JSON result  
packets | Returns if it exists in JSON result  
streams | Returns if it exists in JSON result  
time | Returns if it exists in JSON result  
entropy.req | Returns if it exists in JSON result  
ip.proto | Returns if it exists in JSON result  
****  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
    {
    "EntityResult":
    [{
    "payload.req": "110",
    "ubc.req": "44",
    "netname": "private dst",
    "lifetime": "0",
    "rid": "792830",
    "payload": "110",
    "size": "242",
    "service": "0",
    "mcb.req": "48",
    "eth.src": "11:6C:AC:61:11:11",
    "tcp.flags": "24",
    "tcp.dstport": "39497",
    "direction": "lateral",
    "medium": "1",
    "ip.dst": "1.1.1.1",
    "alert": "test App rule",
    "sessionid": "792831",
    "eth.type": "2048",
    "ip.src": "1.1.1.1",
    "mcbc.req": "9",
    "eth.dst": "00:50:56:A5:45:70",
    "did": "nwappliance5805",
    "tcp.srcport": "389",
    "packets": "2",
    "streams": "1",
    "time": 1547467411,
    "entropy.req": "5075",
    "ip.proto": "6"
    },
    "Entity": "1.1.1.1"
    }]
    

### Query NetWitness for Events Around User

#### Description

Run a query on RSA NetWitness to retrieve all events for a specific query (conditions) for a given username in the alert.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on the User entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
payload.req | Returns if it exists in JSON result  
ubc.req | Returns if it exists in JSON result  
netname | Returns if it exists in JSON result  
lifetime | Returns if it exists in JSON result  
rid | Returns if it exists in JSON result  
payload | Returns if it exists in JSON result  
size | Returns if it exists in JSON result  
service | Returns if it exists in JSON result  
mcb.req | Returns if it exists in JSON result  
mcbc.req | Returns if it exists in JSON result  
tcp.dstport | Returns if it exists in JSON result  
direction | Returns if it exists in JSON result  
medium | Returns if it exists in JSON result  
ip.dst | Returns if it exists in JSON result  
alert | Returns if it exists in JSON result  
sessionid | Returns if it exists in JSON result  
eth.type | Returns if it exists in JSON result  
ip.src | Returns if it exists in JSON result  
tcp.flags | Returns if it exists in JSON result  
Tcp.srcport | Returns if it exists in JSON result  
packets | Returns if it exists in JSON result  
user.src | Returns if it exists in JSON result  
streams | Returns if it exists in JSON result  
time | Returns if it exists in JSON result  
entropy.req | Returns if it exists in JSON result  
ip.proto | Returns if it exists in JSON result  
  
##### Insights

N/A

#### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
    {
    "EntityResult":
    [{
    "payload.req": "110",
    "ubc.req": "44",
    "netname": "private dst",
    "lifetime": "0",
    "rid": "792830",
    "payload": "110",
    "size": "242",
    "service": "0",
    "mcb.req": "48",
    "mcbc.req": "9",
    "tcp.dstport": "39497",
    "direction": "lateral",
    "medium": "1",
    "ip.dst": "1.1.1.1",
    "alert": "test App rule",
    "sessionid": "792831",
    "eth.type": "2048",
    "ip.src": "1.1.1.1",
    "tcp.flags": "24",
    "tcp.srcport": "389",
    "packets": "2",
    "user.src": "user",
    "streams": "1",
    "time": 1547467411,
    "entropy.req": "5075",
    "ip.proto": "6"
    },
    "Entity": "user"
    }]
    

### Run General Query

#### Description

Run free query and receive event and a PCAP file.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Query | 0 | N/A | Custom query string.  
  
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
events_json | True/False | events_json:False  
  
##### JSON Result
    
    
    [
    {
    "payload.req": "66",
    "ubc.req": "18",
    "netname": "multicast dst",
    "lifetime": "0",
    "rid": "48908",
    "payload": "66",
    "size": "150",
    "service": "0",
    "mcb.req": "0",
    "eth.src": "00:50:56:B5:76:2B",
    "udp.srcport": "60807",
    "udp.dstport": "5355",
    "direction": "lateral",
    "medium": "1",
    "ip.dst": "1.1.1.1",
    "alert": "test App rule",
    "sessionid": "48908",
    "eth.type": "2048",
    "ip.src": "1.1.1.1",
    "mcbc.req": "24",
    "eth.dst": "11:11:5E:11:11:FC",
    "did": "nwappliance5805",
    "packets": "2",
    "streams": "1",
    "time": 1547047123,
    "entropy.req": "3498",
    "ip.proto": "17"
    }]
    

### Update The 'TI' Database of NetWitness

#### Description

Set custom feed configuration in NetWitness to enrich entities with specific metadata keys and values. These will be later correlated in the NetWitness correlation rules

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Key Value string | 0 | N/A | A key value string,which is presented in the current format: key1:val1,key2:val2  
  
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
    

### Update the TI database Of NetWitness raw Input

#### Description

Set custom feed configuration in NetWitness to enrich entities with specific metadata keys and values. These will be later correlated in the NetWitness correlation rules.

#### Parameters

**Parameter** | **Type** | Default Value | Description  
---|---|---|---  
Identifiers | 0 | N/A | Comma separated identifiers list.  
Key and Value Items | 0 | N/A | Key and Value Items.  
  
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
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

## Connectors

### Configure RSA NetWitness connectors in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

To configure the selected connector use the connector-specific parameters listed in the following tables:

  * [RSA NetWitness Incidents Connector configuration parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness#rsa-netwitness-incidents-connector-parameters)
  * [RSA NetWitness Query Connector configuration parameters](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness#rsa-netwitness-query-connector-parameters)



### RSA NetWitness Incidents Connector

#### Description

RSA NetWitness Incidents Connector.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | 2 | device_product | The field name used to determine the device product.  
EventClassId | 2 | name | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | 2 | 60 | The timeout limit (in seconds) for the python process running current script.  
UI URI | 2 | https://x.x.x.x/ | N/A  
Concentrator URI | 2 | http://x.x.x.x:50105/ | N/A  
Decode URI | 2 | https://x.x.x.x:50102/ | N/A  
Username | 2 | null | N/A  
Password | 3 | null | N/A  
Rule Generator Field | 2 | null | N/A  
Event Time Field | 2 | time | N/A  
Max Days Backwards | 1 | 1 | N/A  
Incidents Count Limit | 1 | 10 | N/A  
Verify SSL | o | null | N/A  
Proxy Server Address | 2 | null | The address of the proxy server to use.  
Proxy Username | 2 | null | The proxy username to authenticate with.  
Proxy Password | 3 | null | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

### RSA NetWitness Query Connector

#### Description

RSA NetWitness static query connector.

#### Connector parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | 2 | device_product | The field name used to determine the device product.  
EventClassId | 2 | name | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | 2 | 60 | The timeout limit (in seconds) for the python process running current script.  
Concentrator URI | 2 | http://x.x.x.x:50105/ | N/A  
Decode URI | 2 | https://x.x.x.x:50102/ | N/A  
Username | 2 | null | N/A  
Password | 3 | null | N/A  
Query | 2 | null | N/A  
Rule Generator Field | 2 | null | N/A  
Alert Count Limit | 1 | 10 | N/A  
Max Days Backwards | 1 | 1 | N/A  
Event Time Field | 2 | time | N/A  
Verify SSL | o | null | N/A  
Proxy Server Address | 2 | null | The address of the proxy server to use.  
Proxy Username | 2 | null | The proxy username to authenticate with.  
Proxy Password | 3 | null | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
