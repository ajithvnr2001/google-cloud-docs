---
url: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Results
title: Class Results (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:05.508267+00:00
---

# Class Results (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Results

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Results (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.1  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.3  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.2  3.23.3  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.1  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.1  3.10.0  3.9.3  3.8.3  3.7.1  3.6.0  3.5.2  3.4.0  3.3.2  3.2.1  3.1.1  3.0.2  2.0.2  1.1.2  1.0.0  0.1.0 
    
    
    Results(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Artifacts created by the build pipeline.

## Attributes  
  
---  
**Name** | **Description**  
`images` |  `MutableSequence[[google.cloud.devtools.cloudbuild_v1.types.BuiltImage](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.BuiltImage)]`   
Container images that were built as a part of the build.   
`build_step_images` |  `MutableSequence[str]`   
List of build step digests, in the order corresponding to build step indices.   
`artifact_manifest` |  `str`   
Path to the artifact manifest for non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage.   
`num_artifacts` |  `int`   
Number of non-container artifacts uploaded to Cloud Storage. Only populated when artifacts are uploaded to Cloud Storage.   
`build_step_outputs` |  `MutableSequence[bytes]`   
List of build step outputs, produced by builder images, in the order corresponding to build step indices. `Cloud Builders   
`artifact_timing` |  `[google.cloud.devtools.cloudbuild_v1.types.TimeSpan](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.TimeSpan)`   
Time to push all non-container artifacts to Cloud Storage.   
`python_packages` |  `MutableSequence[[google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedPythonPackage)]`   
Python artifacts uploaded to Artifact Registry at the end of the build.   
`maven_artifacts` |  `MutableSequence[[google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedMavenArtifact)]`   
Maven artifacts uploaded to Artifact Registry at the end of the build.   
`go_modules` |  `MutableSequence[[google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedGoModule)]`   
Optional. Go module artifacts uploaded to Artifact Registry at the end of the build.   
`npm_packages` |  `MutableSequence[[google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.UploadedNpmPackage)]`   
Npm packages uploaded to Artifact Registry at the end of the build.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
