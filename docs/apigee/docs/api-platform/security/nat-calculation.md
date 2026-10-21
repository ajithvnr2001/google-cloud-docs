---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-calculation/
title: Calculating static NAT IP requirements \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:16:51.029164+00:00
---

# Calculating static NAT IP requirements  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-calculation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Calculating static NAT IP requirements Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Southbound traffic between Apigee and a target backend with a public IP address uses [Cloud NAT](https://cloud.google.com/nat/docs/overview) to translate the private IP address of your Apigee instance into a public IP address. If your target backend requires IP allow-listing, you can reserve and activate static NAT IPs for egress traffic. This topic describes how to calculate the minimum number of static NAT IPs required to support anticipated traffic. 

## Before you begin

If you choose to use static NAT IP allocation to support allow-listing, you will need to calculate the minimum number of static IPs required to support anticipated traffic. For this calculation, you will need the following information: 

  * **Maximum time per transaction** : This is the maximum time, in seconds, that a transaction will take, from the start of the request until the end of the response. 
  * **Maximum transactions per second (TPS)** : This is the maximum number of transactions per second the Apigee instance can possibly support. 
  * **Maximum TPS for a single unique backend** : This is the maximum number of transactions per second that any single backend can possibly support.
  * **Maximum number of environments** : The maximum number of environments on this Apigee instance. 

**Note** : The maximums detailed above are a part of capacity planning for NAT, and must include consideration of possible traffic spikes, TPS increases for backends due to a maintenance or outage, and future environment additions. It is recommended to add some buffer to the projected numbers in order to handle unforeseen traffic increases, and to redo the NAT calculations when projections change.

## Calculate the number of static IPs required

You can use the following formulas to calculate the minimum number of NAT IPs that need to be statically assigned: 

  1. Calculate the maximum number of NAT source ports required per backend as $ S $. 

$$ S = \lceil (150 + T) \times B \rceil $$ 

Where: 

     * $ T $ is the maximum time per transaction, in seconds.
     * $ B $ is the maximum TPS for any single unique backend.
     * $ \lceil \rceil $ is the ceiling (least integer) function, meaning round up to the next integer
  2. Calculate the minimum ports used by the Apigee instance as $ N $. 

$$ N = max(4096 \times E, \lceil {512 \over 75} \times R \rceil) + 6144 $$

Where: 

     * $ E $ is the number of Apigee environments.
     * $ R $ is the maximum TPS for the Apigee instance.
     * $ \lceil \rceil $ is the ceiling (least integer) function, meaning round up to the next integer
     * The $ \mathit{max}() $ function takes the maximum of the two values. 
  3. Take the maximum number of ports required as $ P $. 

$$ P = max(S, N) $$ 

Where: 

     * $ S $ is the maximum number of NAT source ports required, as calculated in Step 1.
     * $ N $ is the minimum number of ports used by the Apigee instance, as calculated in Step 2.
     * The $ \mathit{max}() $ function takes the maximum of the two values. 
  4. Calculate the minimum number of NAT IPs required as $ I $. 

$$ I = \lceil P / 64512 \rceil $$

Where: 

     * $ P $ is the maximum number of ports required, calculated in Step 3.
     * $ \lceil \rceil $ is the ceiling (least integer) function, meaning round up to the next integer

**Note** : These formulas do not account for connection reuse, and instead calculate a "worst-case" scenario where no connections are reused. Actual connection reuse may vary. See [Connection Reuse](https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-performance#connection-reuse) for the factors that contribute to an Apigee instance reusing an existing connection or opening a new one. 

## Examples

### Example 1

In this example, we expect a maximum of 10,000 TPS across 1 environment. The transactions are all `HTTP GET` requests and the 99th percentile transaction duration is 50 milliseconds (ms). These requests are unevenly served by a pool of servers behind 3 load balancer backends, with one of the load balancers taking 5,000 TPS, another taking 3,000 TPS, and the last load balancer taking 2,000 TPS.

For this example, the key values are as follows: 

  * Maximum time per transaction: **50 ms**
  * Maximum TPS for the Apigee instance: **10,000**
  * Maximum TPS for a single backend: **5,000**
  * Number of Apigee environments: **1**



Using the formulas outlined earlier, we can calculate the number of NAT IPs required: 

  1. $$ \lceil (150 + 0.050) \times 5000 \rceil = \lceil 150.050 \times 5000 \rceil = \lceil 750250 \rceil = 750250 $$

The maximum number of NAT source ports required per backend, assuming no connection reuse, is **750,250**.

  2. $$ max(4096 \times 1, \lceil {512 \over 75} \times 10000 \rceil) + 6144 $$

$$ max(4096, \lceil 6.827 \times 10000 \rceil) + 6144 $$

$$ max(4096, \lceil 68270 \rceil) + 6144 $$

$$ 68270 + 6144 = 74414 $$

The minimum number of NAT source ports used by the Apigee runtime is **74,414**.

  3. $$ max(750250, 74414) = 750250 $$

The maximum number of NAT source ports required per instance is **750,250**.

  4. $$ \lceil 750250 / 64512 \rceil = \lceil 11.630 \rceil = 12 $$

The minimum number of NAT IPs required to support a maximum of 10,000 TPS of 50 ms each (or less), with a single backend IP and port pair supporting a maximum of 5,000 TPS, is **12**.




### Example 2

In this example, we expect a maximum of 1,000 TPS across 20 Apigee environments. The 99th percentile duration of these transactions is 5 seconds. These requests will be served by 8 target backends, with traffic normally evenly distributed across all of them. With consideration for maintenance and outages, a single backend is never expected to serve more than 250 TPS.

For this example, the key values are as follows: 

  * Maximum time per transaction: **5s**
  * Maximum transactions per second (TPS): **1,000**
  * Maximum TPS for a single backend: **250**
  * Number of Apigee environments: **20**



Using the formulas outlined earlier, we can calculate the number of NAT IPs required: 

  1. $$ \lceil (150 + 5) \times 250 \rceil = \lceil 155 \times 250 \rceil = \lceil 38750 \rceil = 38750 $$

The maximum number of NAT source ports required per backend, assuming no connection reuse, is **38,750**.

  2. $$ max(4096 \times 20, \lceil {512 \over 75} \times 1000 \rceil) + 6144 $$

$$ max(81920, \lceil 6.827 \times 1000 \rceil) + 6144 $$

$$ max(81920, \lceil 6827 \rceil) + 6144 $$

$$ 81920 + 6144 = 88064 $$

The minimum number of NAT source ports used by the Apigee runtime is **88,064**.

  3. $$ max(38750, 88064) = 88064 $$

The maximum number of NAT source ports required per instance is **88,064**.

  4. $$ \lceil 88064 / 64512 \rceil= \lceil 1.365 \rceil= 2 $$

The minimum number of NAT IPs required to support a maximum of 1,000 TPS of 5 seconds each (or less), with a single backend IP and port pair supporting a maximum of 250 TPS, is **2**.




### Example 3

In this example, we want to calculate the maximum TPS achievable with 2 NAT IPs to a single target backend. The maximum time per transaction is estimated to be 100 ms.

For this example, the key values are as follows: 

  * **Maximum time per transaction** : 100ms
  * **Number of NAT IPs** : 2



In this case, we can use the formulas in Step 4 and Step 1 to calculate the maximum number of NAT source ports provided and the number of TPS those source ports can support: 

  1. $$ 2 = \lceil P / 64512 \rceil $$

$$ 129024 = P $$

The maximum number of NAT source ports provided is **129,024**.

  2. $$ 129024 = \lceil (150 + 0.100) \times B \rceil $$

$$ 129024 = \lceil 150.1 \times B \rceil $$

$$ \lfloor 129024 / 150.1 \rfloor = B $$

$$ \lfloor 859.587 \rfloor = B $$

$$ 859 = B $$

The max TPS is **859** with 2 NAT IPs to a single backend, assuming no connection reuse.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
