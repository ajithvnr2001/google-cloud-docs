---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse
title: Class AnalyzeIamPolicyResponse (3.30.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:43.455548+00:00
---

# Class AnalyzeIamPolicyResponse (3.30.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnalyzeIamPolicyResponse (3.30.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    AnalyzeIamPolicyResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A response message for AssetService.AnalyzeIamPolicy.

## Attributes  
  
---  
**Name** | **Description**  
`main_analysis` |  `[google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis)`   
The main analysis that matches the original request.   
`service_account_impersonation_analysis` |  `Sequence[[google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p4beta1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis)]`   
The service account impersonation analysis if [AnalyzeIamPolicyRequest.analyze_service_account_impersonation][] is enabled.   
`fully_explored` |  `bool`   
Represents whether all entries in the main_analysis and service_account_impersonation_analysis have been fully explored to answer the query in the request.   
`non_critical_errors` |  `Sequence[[google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisResult.AnalysisState](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p4beta1.types.IamPolicyAnalysisResult.AnalysisState)]`   
A list of non-critical errors happened during the request handling to explain why `fully_explored` is false, or empty if no error happened.   
  
## Classes 

### IamPolicyAnalysis
    
    
    IamPolicyAnalysis(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An analysis message to group the query and results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
