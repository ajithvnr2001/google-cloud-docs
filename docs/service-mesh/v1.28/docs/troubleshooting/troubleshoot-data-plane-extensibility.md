---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-data-plane-extensibility/
title: Resolving data plane extensibility issues \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:18.110977+00:00
---

# Resolving data plane extensibility issues  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-data-plane-extensibility/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving data plane extensibility issues

This section explains common Cloud Service Mesh data plane extensibility problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.28/docs/getting-support).

## EnvoyFilter configuration issues

If you are having issues with `EnvoyFilter` configuration, use the following steps to troubleshoot:

  1. Validate that the EnvoyFilter CR `status` doesn't report any errors:
         
         kubectl get envoyfilter NAME  -n NAMESPACE  -o yaml
         

  2. Inspect the workload's envoy config dump to validate that the appropriate config has propagated. Since the config dump is usually vast, look for an unique identifier corresponding to the applied configuration, for example the patch name (`envoy.filters.http.local_ratelimit`) in the EnvoyFilter configuration.
         
         gcloud beta container fleet mesh debug proxy-config POD_NAME .NAMESPACE  --type=listener --membership=<membership_id> --location=MEMBERSHIP_LOCATION  --project=PROJECT_ID  --output=yaml | grep IDENTIFIERS  -C SURROUNDING_LINES_OF_CONTEXT 
         

  3. Various Envoy extensions emit extension-specific statistics at the workload level, for example [statistics for local rate limit filter](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/local_rate_limit_filter#statistics). These can be utilized to monitor the filter's operational state.
         
         kubectl port-forward POD_NAME  -n NAMESPACE  15000:15000 &
         curl http://localhost:15000/stats | grep STAT_NAME 
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
