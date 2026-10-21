---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/obfuscate-user-data-for-analytics/
title: Obfuscate user data for Apigee API Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:06:48.055403+00:00
---

# Obfuscate user data for Apigee API Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/obfuscate-user-data-for-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Obfuscate user data for Apigee API Analytics Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Data obfuscation is the process of replacing sensitive information with fake data, so that it can't be used by malicious agents and is protected for privacy reasons. This feature allows you to obscure data before sending it as part of the analytics payload. With this feature, Apigee uses SHA512 to hash the original value before communicating from the runtime plane to the control plane. 

## Procedure

Enable this feature per environment by setting `features.analytics.data.obfuscation.enabled` to **true**.

When using `PUT`, be careful to include the entire set of properties for your environment. PUT overwrites the entire property set each time you issue it. 

### No data residency
    
    
    curl -v -X PUT \
      https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
      "name" : "ENV_NAME",
      "properties" : {
        "property" : [ {
          "name" : "features.analytics.data.obfuscation.enabled",
          "value" : "true"
        },]
      }
    }'

### Data residency
    
    
    curl -v -X PUT \
      https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $TOKEN" \
      -d '{
      "name" : "ENV_NAME",
      "properties" : {
        "property" : [ {
          "name" : "features.analytics.data.obfuscation.enabled",
          "value" : "true"
        },]
      }
    }'

With obfuscation enabled, Apigee hashes the following fields at the runtime plane before sending the information to the Analytics backend: 

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



Apigee hashes the following dimension values in custom analytics reports:

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



See the [ Analytics metrics, dimensions, and filters reference](https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions) for detailed descriptions of analytics dimensions.

##  Viewing obfuscated results 

The obfuscated results display in the [analytics dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards). It may take several minutes before you see the hashed results in the UI. 

**Note:** Analytics reports display unhashed data communicated from the runtime plane before you enabled obfuscating or after you disable it.

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
