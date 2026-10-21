---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin_sso_changelog/
title: Change log for ONELOGIN_SSO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:47:11.177137+00:00
---

# Change log for ONELOGIN_SSO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin_sso_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONELOGIN_SSO 

Date | Changes | 2022-03-23 | Enhancement-map following raw logs elements to UDM elements   
\- user_agent to event.idm.read_only_udm.network.http.user_agent.   
\- uuid to event.idm.read_only_udm.metadata.product_log_id.   
\- group_id to event.idm.read_only_udm.target.group.product_object_id.   
\- group_name to event.idm.read_only_udm.target.group.group_display_name.   
\- policy_type to security_result.rule_type.   
\- policy_id to security_result.rule_id.   
\- policy_name to security_result.rule_name.   
\- authentication_factor_type to event.idm.read_only_udm.extensions.auth.auth_details.   
\- risk_reasons to security_result.description.   
\- risk_score to security_result.severity_details.   
Logic enhancements for the following app_id, app_name, directory_id, directory_name, privilege_id, privilege_name, role_name, role_id.   
  
---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
