---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/obfuscate-userdata-for-analytics/
title: Obfuscate user data for analytics \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:40:53.839933+00:00
---

# Obfuscate user data for analytics  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/obfuscate-userdata-for-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Obfuscate user data for analytics Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/obfuscate-userdata-for-analytics.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/obfuscate-userdata-for-analytics.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/obfuscate-userdata-for-analytics.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/obfuscate-userdata-for-analytics.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/obfuscate-userdata-for-analytics.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/obfuscate-userdata-for-analytics.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/obfuscate-userdata-for-analytics.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/obfuscate-userdata-for-analytics.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/obfuscate-userdata-for-analytics.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/obfuscate-userdata-for-analytics.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/obfuscate-userdata-for-analytics.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/obfuscate-userdata-for-analytics.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/obfuscate-userdata-for-analytics.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/obfuscate-userdata-for-analytics.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/obfuscate-userdata-for-analytics.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/obfuscate-userdata-for-analytics.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/obfuscate-userdata-for-analytics.html)



This feature allows you to obscure data before sending it as part of the analytics payload. With this feature, Apigee uses SHA512 to hash the original value before sending data from the runtime plane to the control plane. 

## Procedure

You can set the salt value for the hash with the [`axHashSalt`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#axhashsalt) property in the `overrides.yaml` file. The `axHashSalt` property specifies a value used as a salt when computing SHA512 hashes to obfuscate sensitive analytics data. Apigee recommends using the same value across different clusters that host the same Apigee organization. Apply the value with [`apigeectl`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cli-reference).

Enable this feature for each environment by setting `features.analytics.data.obfuscation.enabled` to **true**.

When using `PUT`, be careful to include the entire set of properties for your environment. PUT overwrites the entire property set each time you issue it. 
    
    
    curl -v -X PUT \
       https://apigee.googleapis.com/v1/organizations/your_org_name/environments/your_env_name \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
      "name" : "your_env_name",
      "properties" : {
        "property" : [ {
          "name" : "features.analytics.data.obfuscation.enabled",
          "value" : "true"
        },]
      }
    }'

With obfuscation enabled, Apigee hybrid will hash the following fields with SHA512 at the runtime plane before sending the information to analytics backend: 

  * client_id
  * client_ip
  * developer_email
  * proxy_client_ip
  * proxy_pathsuffix
  * request_uri
  * request_path
  * target_basepath
  * target_url
  * x_forwarded_for_ip
  * x-apigee.edge.true_client_ip
  * x-apigee.intelligence.client_ip_header



Apigee hybrid will hash the following dimension values in custom analytics reports:

  * Client ID
  * Client IP Address
  * Developer Email
  * Proxy Client IP
  * Proxy Path Suffix
  * Referred Client IP
  * Request Path
  * Request URI
  * Resolved Client IP
  * Target Base Path
  * Target URL
  * X Forwarded For



See [ Analytics metrics, dimensions, and filters reference](https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions) for detailed descriptions of analytics dimensions.

##  Viewing obfuscated results 

The obfuscated results display in the Apigee hybrid analytics dashboard. It may take several minutes before you see the hashed results in the UI. 

![Custom reports showing hashed user data](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/hybrid-mask-example-small.png)

**Note:** Analytics reports will display unhashed data communicated from the runtime plane before you enabled obfuscating or after you disable it.  
![Custom reports showing mixed hashed and unhashed user data](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/hybrid-mask-example-mixed.png)

## Example

The following example shows the data before and after obfuscating: 
    
    
    // JSON data sent to AX before obfuscating
    {
       "proxy_basepath":"/APP_NAME",
       "x-apigee.edge.execution.stats.request_flow_endtimestamp":1582770652814,
       "apiproxy":"APP_NAME",
       "x-apigee.edge.is_policy_error":0,
       "client_sent_start_timestamp":1582770652817,
       "x-apigee.edge.is_target_error":0,
       "client_received_start_timestamp":1582770652813,
       "client_ip":"10.10.0.99",
       "is_error":false,
       "x-apigee.edge.stats.steps":"{\"JS1.0\":1}",
       "request_size":0,
       "x-apigee.intelligence.client_ip_header":"10.10.0.99",
       "virtual_host":"default",
       "x-apigee.edge.mp_host":"mp",
       "sla":false,
       "x-apigee.intelligence.service":"{}",
       "client_sent_end_timestamp":1582770652817,
       "request_uri":"/APP_NAME",
       "proxy":"default",
       "proxy_client_ip":"10.10.0.99",
       "x-apigee.edge.dn.region":"dc-1",
       "apigee.edge.execution.is_apigee_fault":0,
       "x-apigee.edge.target.latency.stats":"{\"targetList\":[]}",
       "useragent":"Apache-HttpClient/4.3.6 (java 1.6)",
       "proxy_pathsuffix":"",
       "x-apigee.edge.execution.stats.request_flow_start_timestamp":1582770652814,
       "x_forwarded_for_ip":"10.10.0.99",
       "x_forwarded_proto":"http",
       "response_status_code":200,
       "request_verb":"GET",
       "x-apigee.edge.execution.stats.response_flow_end_timestamp":1582770652816,
       "gateway_source":"message_processor",
       "environment":"env_82hw",
       "client_received_end_timestamp":1582770652814,
       "organization":"Org_1582769880344",
       "x-apigee.edge.execution.stats.response_flow_start_timestamp":1582770652814,
       "request_path":"/APP_NAME",
       "gateway_flow_id":"rt-8644-188-1",
       "apiproxy_revision":"1"
    }
    
    
    // JSON data sent to AX after obfuscating
    {
       "proxy_basepath":"/APP_NAME",
       "x-apigee.edge.execution.stats.request_flow_endtimestamp":1582749361836,
       "apiproxy":"APP_NAME",
       "x-apigee.edge.is_policy_error":0,
       "client_sent_start_timestamp":1582749361884,
       "x-apigee.edge.is_target_error":0,
       "client_received_start_timestamp":1582749361790,
       "client_ip":"090cdae81ea6e58e55093f702661cf2325cef6a68aa801f1209e73bb0649c2b931bcad468911da887a42ce1d1daee07b24933e3dbbde6eb7438cfc9020a25445",
       "is_error":false,
       "x-apigee.edge.stats.steps":"{\"JS1.0\":30}",
       "request_size":0,
       "x-apigee.intelligence.client_ip_header":"090cdae81ea6e58e55093f702661cf2325cef6a68aa801f1209e73bb0649c2b931bcad468911da887a42ce1d1daee07b24933e3dbbde6eb7438cfc9020a25445",
       "virtual_host":"default",
       "x-apigee.edge.mp_host":"mp",
       "sla":false,
       "x-apigee.intelligence.service":"{}",
       "client_sent_end_timestamp":1582749361886,
       "request_uri":"0176937d9c4a33094d3c3f38ac8b15fa05dd6380a6bb544e4002c98de9f27bdbfea754901b0acb487f4980b09f7d312ad1e7027b96b2c8bfd8b9c24e833fbb5a",
       "proxy":"default",
       "proxy_client_ip":"090cdae81ea6e58e55093f702661cf2325cef6a68aa801f1209e73bb0649c2b931bcad468911da887a42ce1d1daee07b24933e3dbbde6eb7438cfc9020a25445",
       "x-apigee.edge.dn.region":"dc-1",
       "apigee.edge.execution.is_apigee_fault":0,
       "x-apigee.edge.target.latency.stats":"{\"targetList\":[]}",
       "useragent":"Apache-HttpClient/4.3.6 (java 1.6)",
       "proxy_pathsuffix":"cf83e1.67eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81.638327af927da3e",
       "x-apigee.edge.execution.stats.request_flow_start_timestamp":1582749361833,
       "x_forwarded_for_ip":"090cdae81ea6e58e55093f702661cf2325cef6a68aa801f1209e73bb0649c2b931bcad468911da887a42ce1d1daee07b24933e3dbbde6eb7438cfc9020a25445",
       "x_forwarded_proto":"http",
       "response_status_code":200,
       "request_verb":"GET",
       "x-apigee.edge.execution.stats.response_flow_end_timestamp":1582749361874,
       "gateway_source":"message_processor",
       "environment":"env_xj25",
       "client_received_end_timestamp":1582749361821,
       "organization":"Org_1582749068984",
       "x-apigee.edge.execution.stats.response_flow_start_timestamp":1582749361836,
       "request_path":"0176937d9c4a33094d3c3f38ac8b15fa05dd6380a6bb544e4002c98de9f27bdbfea754901b0acb487f4980b09f7d312ad1e7027b96b2c8bfd8b9c24e833fbb5a",
       "gateway_flow_id":"rt-6290-57-1",
       "apiproxy_revision":"1"
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
