---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:01.114525+00:00
---

# Security bulletins  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Gemini Enterprise Agent Platform.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader:
        
        https://cloud.google.com/feeds/vertex-ai-security-bulletins.xml




## GCP-2026-012

**Published:** 2026-02-20

Description | Severity | Notes  
---|---|---  
In Google Cloud Gemini Enterprise Agent Platform, a vulnerability involving predictable bucket naming was identified in Vertex AI Experiments from version 1.21.0 up to (but not including) 1.133.0. **What should I do?** No customer action is needed for mitigation. [CVE-2026-2473](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2473) allows an unauthenticated remote attacker to achieve cross-tenant remote code execution, model theft, and poisoning using pre-creating predictably named Cloud Storage buckets (Bucket Squatting). This vulnerability was identified in Vertex AI Experiments version 1.21.0 and is listed under CVE-2026-2473. Mitigations have already been applied to version 1.133.0 and later. | High |  [CVE-2026-2473](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2473)  
  
## GCP-2026-011

**Published:** 2026-02-20

Description | Severity | Notes  
---|---|---  
A stored Cross-site Scripting (XSS) vulnerability in _genai/_evals_visualization was identified in Google google-cloud-aiplatform (Gemini Enterprise Agent Platform Python SDK Visualization) on Exclusively-Hosted-Service. **What should I do?** Customers will need to update their google-cloud-aiplatform Python SDK to version 1.131.0 (released on 2025-12-16) or later to receive the fix. [CVE-2026-2472](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2472) allows an unauthenticated remote attacker to execute arbitrary JavaScript in a victim's Jupyter or Colab environment using injecting script escape sequences into model evaluation results or dataset JSON data. This vulnerability was identified in Google google-cloud-aiplatform (Gemini Enterprise Agent Platform Python SDK) prior to 1.131.0 and is listed under CVE-2026-2472. | High |  [CVE-2026-2472](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2472)  
  
## GCP-2023-036

**Published:** 2023-10-30

Description | Severity | Notes  
---|---|---  
[Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) is a set of prepackaged virtual machine images with a deep learning framework that are ready to be run out of the box. Recently, an out-of-bounds write vulnerability was discovered in the `ReadHuffmanCodes()` function in the `libwebp` library. This might impact images that use this library. Google Cloud continuously scans its publicly published images and updates the packages to assure patched distros are included in the latest releases available for customer adoption. Deep Learning VM Images have been updated to ensure that the latest VM images include the patched distros. Customers adopting the latest VM images are not exposed to this vulnerability. **What should I do?** Google Cloud customers using published VM images should ensure that they are adopting the latest images and that their environments are up to date as per the [shared responsibility model](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate). [CVE-2023-4863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4863) could be exploited by an attacker to execute arbitrary code. This vulnerability was identified in Google Chrome prior to 116.0.5845.187 and in `libwebp` prior to 1.3.2 and is being listed under CVE-2023-4863. | High |  [CVE-2023-4863](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4863)  
  
## GCP-2023-029

**Published:** 2023-10-03

Description | Severity | Notes  
---|---|---  
TorchServe is used to host PyTorch machine learning models for online prediction. Gemini Enterprise Agent Platform provides prebuilt PyTorch model serving containers which depend on TorchServe. Vulnerabilities were recently discovered in TorchServe which would allow an attacker to take control of a TorchServe deployment if its model management API is exposed. Customers with PyTorch models deployed to Gemini Enterprise Agent Platform online prediction are not affected by these vulnerabilities, since Gemini Enterprise Agent Platform does not expose TorchServe's model management API. Customers using TorchServe outside of Gemini Enterprise Agent Platform should take precautions to ensure their deployments are set up securely. **What should I do?** Gemini Enterprise Agent Platform customers with deployed models using Gemini Enterprise Agent Platform's [prebuilt PyTorch serving containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers#pytorch) do not need to take any action to address the vulnerabilities, since Gemini Enterprise Agent Platform's deployments do not expose TorchServe's management server to the internet. Customers who are using the prebuilt PyTorch containers in other contexts, or who are using a custom-built or third-party distribution of TorchServe, should do the following:

  * Ensure that TorchServe's model management API is not exposed to the internet. The model management API can be restricted to local access only by ensuring that the `[management_address](https://pytorch.org/serve/configuration.html#configure-torchserve-listening-address-and-port)` is bound to `127.0.0.1`.
  * Use the `[allowed_urls](https://pytorch.org/serve/configuration.html#other-properties)` setting to ensure that models can be loaded from intended sources only. 
  * Upgrade TorchServe to version 0.8.2, which includes mitigations for this issue, as soon as possible. As a precaution, Gemini Enterprise Agent Platform will release fixed prebuilt containers by 2023-10-13.

**What vulnerabilities are being addressed?** TorchServe's management API is bound to `0.0.0.0` by default in most TorchServe Docker images, including those released by Gemini Enterprise Agent Platform, making it accessible to external requests. The default IP address for the management API is changed to `127.0.0.1` in TorchServe 0.8.2, mitigating this issue. [CVE-2023-43654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-43654) and [CVE-2022-1471](https://github.com/pytorch/serve/security/advisories/GHSA-4mqg-h5jf-j9m7) allow a user with access to the management API to load models from arbitrary sources and remotely execute code. Mitigations for both of these issues are included in TorchServe 0.8.2: the remote code execution path is removed, and a warning is emitted if the default value for `allowed_urls` is used. | High |  [CVE-2023-43654](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-43654), [CVE-2022-1471](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1471)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
