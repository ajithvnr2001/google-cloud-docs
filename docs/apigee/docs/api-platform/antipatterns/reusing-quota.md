---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/reusing-quota/
title: Antipattern: Re-use a Quota policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:18.476429+00:00
---

# Antipattern: Re-use a Quota policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/reusing-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Re-use a Quota policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/reusing-quota) documentation._

Apigee provides the ability to configure the number of allowed requests for an API Proxy for a specific period of time using the [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy).

## Antipattern

If a [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) is reused, then the quota counter will be decremented each time the Quota policy gets executed irrespective of where it is used. That is, if a Quota policy is reused:

  * Within the same flow or different flows of an API proxy 
  * In different target endpoints of an API proxy 



Then the quota counter gets decremented each time it is executed and we will end up getting Quota violation errors much earlier than the expected for the specified interval of time.

Let's use the following example to explain how this works.

### API Proxy

Let's say we have an API proxy named "TestTargetServerQuota", which routes traffic to two different target servers based on the resource path. And we would like to restrict the API traffic to 10 requests per minute for each of these target servers. Here's the table that depicts this scenario:

Resource Path | Target Server | Quota  
---|---|---  
`/target-us` | `target-US.somedomain.com` | 10 requests per minute  
`/target-eu` | `target-EU.somedomain.com` | 10 requests per minute  
  
### Quota policy

Since the traffic quota is same for both the target servers, we define single Quota policy named "Quota-Minute-Target-Server" as shown below:
    
    
    <!-- /antipatterns/examples/1-8.xml -->
    <Quota name="Quota-Minute-Target-Server">
      <Interval>1</Interval>
      <TimeUnit>minute</TimeUnit>
      <Distributed>true</Distributed>
      <Allow count="10"/>
    </Quota>

### Target endpoints

Let's use the Quota policy "Quota-Minute-Target-Server" in the preflow of the target endpoint "Target-US":
    
    
    <!-- /antipatterns/examples/1-9.xml -->
    <TargetEndpoint name="Target-US">
      <PreFlow name="PreFlow">
        <Request>
          <Step>
            <Name>Quota-Minute-Target-Server</Name>
          </Step>
        </Request>
      </PreFlow>
      <HTTPTargetConnection>
        <URL>http://target-us.somedomain.com</URL>
      </HTTPTargetConnection>
    </TargetEndpoint>

And reuse the same Quota policy "Quota-Minute-Target-Server" in the preflow of the other target endpoint "Target-EU" as well:
    
    
    <!-- /antipatterns/examples/1-10.xml -->
    <TargetEndpoint name="Target-EU">
      <PreFlow name="PreFlow">
        <Request>
          <Step>
            <Name>Quota-Minute-Target-Server</Name>
          </Step>
        </Request>
      <Response/>
      </PreFlow>
      <HTTPTargetConnection>
        <URL>http://target-us.somedomain.com</URL>
      </HTTPTargetConnection>
    </TargetEndpoint>

### Incoming traffic pattern

Let's say we get a total of 10 API requests for this API proxy within the first 30 seconds in the following pattern:

Resource Path | `/target-us` | `/target-eu` | All  
---|---|---|---  
# Requests | 4 | 6 | 10  
  
A little later, we get the 11th API request with the resource path as `/target-us`, let's say after 32 seconds.

We expect the request to go through successfully assuming that we still have 6 API requests for the target endpoint `target-us` as per the quota allowed.

However, in reality, we get a `Quota violation error`.

**Reason:** Since we are using the same Quota policy in both the target endpoints, a single quota counter is used to track the API requests hitting both the target endpoints. Thus we exhaust the quota of 10 requests per minute collectively rather than for the individual target endpoint.

## Impact

This antipattern can result in a fundamental mismatch of expectations, leading to a perception that the quota limits got exhausted ahead of time.

## Best practice

  * Use the `<Class>` or `<Identifier>` elements to ensure multiple, unique counters are maintained by defining a single [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy). Let's redefine the Quota policy "Quota-Minute-Target-Server" that we just explained in the previous section by using the header `target_id` as the `<Identifier>` for as shown below: 
        
        <!-- /antipatterns/examples/1-11.xml -->
        <Quota name="Quota-Minute-Target-Server">
          <Interval>1</Interval>
          <TimeUnit>minute</TimeUnit>
          <Allow count="10"/>
          <Identifier ref="request.header.target_id"/>
          <Distributed>true</Distributed>
        </Quota>

    * We will continue to use this Quota policy in both the target endpoints "Target-US" and "Target-EU" as before. 
    * Now let's say if the header `target_id` has a value "US" then the requests are routed to the target endpoint "Target-US". 
    * Similarly if the header `target_id` has a value "EU" then the requests are routed to the target endpoint "Target-EU". 
    * So even if we use the same Quota policy in both the target endpoints, separate quota counters are maintained based on the `<Identifier>` value. 
    * Therefore, by using the `<Identifier>` element we can ensure that each of the target endpoints get the allowed quota of 10 requests. 
  * Use separate Quota policy in each of the flows/target endpoints/API Proxies to ensure that you always get the allowed count of API requests. Let's now look at the same example used in the above section to see how we can achieve the allowed quota of 10 requests for each of the target endpoints. 
    * Define a separate Quota policy, one each for the target endpoints "Target-US" and "Target-EU" 

Quota policy for Target Endpoint "Target-US":
          
          <!-- /antipatterns/examples/1-12.xml -->
          <Quota name="Quota-Minute-Target-Server-US">
            <Interval>1</Interval>
            <TimeUnit>minute</TimeUnit>
            <Distributed>true</Distributed>
            <Allow count="10"/>
          </Quota>

Quota policy for Target Endpoint "Target-EU":
          
          <!-- /antipatterns/examples/1-13.xml -->
          <Quota name="Quota-Minute-Target-Server-EU">
            <Interval>1</Interval>
            <TimeUnit>minute</TimeUnit>
            <Distributed>true</Distributed>
            <Allow count="10"/>
          </Quota>

    * Use the respective quota policy in the definition of the target endpoints as shown below: 

Target Endpoint "Target-US":
          
          <!-- /antipatterns/examples/1-14.xml -->
          <TargetEndpoint name="Target-US">
            <PreFlow name="PreFlow">
              <Request>
                <Step>
                  <Name>Quota-Minute-Target-Server-US</Name>
                </Step>
              </Request>
              <Response/>
            </PreFlow>
            <HTTPTargetConnection>
              <URL>http://target-us.somedomain.com</URL>
            </HTTPTargetConnection>
          </TargetEndpoint>

Target Endpoint "Target-EU":
          
          <!-- /antipatterns/examples/1-15.xml -->
          <TargetEndpoint name="Target-EU">
            <PreFlow name="PreFlow">
              <Request>
                <Step>
                  <Name>Quota-Minute-Target-Server-EU</Name>
                </Step>
              </Request>
              <Response/>
            </PreFlow>
            <HTTPTargetConnection>
              <URL>http://target-eu.somedomain.com</URL>
            </HTTPTargetConnection>
          </TargetEndpoint>

    * Since we are using separate Quota policy in the target endpoints "Target-US" and "Target-EU", a separate counter will be maintained. This ensures that we get the allowed quota of 10 API requests per minute for each of the target endpoints.
  * Use the `<Class>` or `<Identifier>` elements to ensure multiple, unique counters are maintained.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
