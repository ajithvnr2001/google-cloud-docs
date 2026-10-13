---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataProfileJobConfig
title: Class DataProfileJobConfig (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:14.945795+00:00
---

# Class DataProfileJobConfig (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataProfileJobConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataProfileJobConfig (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    DataProfileJobConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for setting up a job to scan resources for profile generation. Only one data profile configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

## Attributes  
  
---  
**Name** | **Description**  
`location` |  `[google.cloud.dlp_v2.types.DataProfileLocation](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataProfileLocation)`   
The data to scan.   
`project_id` |  `str`   
The project that will run the scan. The DLP service account that exists within this project must have access to all resources that are profiled, and the DLP API must be enabled.   
`other_cloud_starting_location` |  `[google.cloud.dlp_v2.types.OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.OtherCloudDiscoveryStartingLocation)`   
Must be set only when scanning other clouds.   
`inspect_templates` |  `MutableSequence[str]`   
Detection logic for profile generation. Not all template features are used by profiles. FindingLimits, include_quote and exclude_info_types have no impact on data profiling. Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned. For more information, see https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency.   
`data_profile_actions` |  `MutableSequence[[google.cloud.dlp_v2.types.DataProfileAction](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.DataProfileAction)]`   
Actions to execute at the completion of the job.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
