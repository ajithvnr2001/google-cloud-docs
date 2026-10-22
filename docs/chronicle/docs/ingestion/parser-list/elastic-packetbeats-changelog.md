---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-packetbeats-changelog/
title: Change log for ELASTIC_PACKETBEATS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:12.919662+00:00
---

# Change log for ELASTIC_PACKETBEATS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-packetbeats-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ELASTIC_PACKETBEATS

Date | Changes  
---|---  
2025-02-13 |  Enhancement:  
\- Added support to parse string value of `dhcpv4.client_mac` to `network.dhcp.client_identifier_string`.   
2025-01-28 |  Enhancement:  
\- Mapped `dns.response_code` to `additional.fields`.   
2025-01-02 |  Enhancement:  
\- When `rCode` is `0` then mapped `rCode` to `dns.response_code`.   
2024-08-20 |  Enhancement:  
\- Mapped `dhcpv4.assigned_ip` to `network.dhcp.yiaddr`.  
\- Mapped `dhcpv4.flags`, `dhcpv4.hardware_type`, `dhcpv4.option.rebinding_time_sec`, `dhcpv4.option.rebinding_time_sec`, `dhcpv4.option.renewal_time_sec`, and `dhcpv4.option.max_dhcp_message_size` to `security_result.detection_fields`.  
\- Mapped `dhcpv4.option.parameter_request_list`, and `dhcpv4.option.dns_servers` to `additional.fields`.  
\- Mapped `dhcpv4.hops` to `network.dhcp.hops`.  
\- Mapped `dhcpv4.relay_ip` to `network.dhcp.giaddr`.  
\- Mapped `dhcpv4.option.domain_name` to `network.dhcp.client_hostname`.  
\- Mapped `dhcpv4.option.router` to `network.dhcp.ciaddr`.  
\- Mapped `dhcpv4.seconds` to `network.dhcp.seconds`.   
2024-03-23 |  Enhancement:  
\- Mapped `headers.accept_encoding` and `headers.x_envoy_attempt_count` to `security_result.about.labels`.  
\- Mapped `headers.content_length`, `headers.content_type`, `headers.x_forwarded_proto`, `headers.x_b3_sampled`, `headers.http_accept`, `headers.x_b3_parentspanid`, `headers.x_envoy_original_path`, `client_cert` and `headers.x_request_id` to `additional.labels`.  
\- Mapped `headers.http_user_agent` to `network.http.user_agent`.  
\- Mapped `headers.request_method` to `network.http.method`.  
\- Mapped `dns.resolved_ip` to `network.dns.additional`.  
\- Mapped `headers.http_host` to `principal.hostname`.  
\- Mapped `headers.x_forwarded_for` and `host` to `principal.ip`  
2022-05-09 |  Added mapping for server_name, application, user_id, user_name, level, msg, logger, audit_category, audit_cluster_name, audit_node_id, audit_node_name, audit_request_effective_user, component, uuid.   
2022-04-12 |  Added generic string for Vendor name and replaced different product names to a generic value string.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
