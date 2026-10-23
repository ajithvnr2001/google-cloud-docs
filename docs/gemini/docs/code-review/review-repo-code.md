---
url: https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code/
title: Review GitHub code using Gemini Code Assist \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:39.854863+00:00
---

# Review GitHub code using Gemini Code Assist  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Review GitHub code using Gemini Code Assist Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Code Assist on GitHub lets you automatically summarize pull requests and generate in-depth code reviews. This helps speed up review cycles and improve overall code quality across your repositories.

Once you've [set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github), you can [invoke Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github) at any stage of the pull request to review the code. You can interact with Gemini Code Assist in the pull request comments directly by:

  * Asking clarifying questions on the review that Gemini Code Assist creates.
  * Prompting Gemini Code Assist by adding the `/gemini` tag to your comments to ask questions in the context of the pull request.



Gemini Code Assist will automatically retrieve helpful information from the repository and pull request to perform its tasks.

This document is intended for developers of all skill levels. It assumes that you have a working knowledge of GitHub.

## Enterprise version

**Important:** The enterprise version of Gemini Code Assist on GitHub is a separate and distinct product from [Gemini Code Assist Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/overview#supported-features).

Gemini Code Assist on GitHub is available in an enterprise version, which you [install](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github) through Google Cloud.

The following table summarizes different aspects of the enterprise version:

| Enterprise version [(Preview)](https://cloud.google.com/products#product-launch-stages)  
---|---  
Terms of service | [Google Cloud terms of service](https://cloud.google.com/terms/)  
[Quotas](https://docs.cloud.google.com/gemini/docs/quotas#github) | 100+ pull requests per day  
[Managing configurations](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review) |  Per-repository within GitHub Across multiple repositories using [Google Cloud](https://console.cloud.google.com/gemini-code-assist/agents-tools)  
[Adding a style guide](https://docs.cloud.google.com/gemini/docs/code-review/style-guide) |  Per-repository within GitHub Across multiple repositories using [Google Cloud](https://console.cloud.google.com/gemini-code-assist/agents-tools)  
GitHub support |  GitHub [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server/admin/overview/about-github-enterprise-server) [GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/data-residency/about-github-enterprise-cloud-with-data-residency)  
  
## Considerations

  * Gemini Code Assist on GitHub does not generate summaries or code suggestions for any files located within the `.github/workflows` directory. This exclusion helps prevent the introduction of potentially insecure configurations to the repository.

  * Gemini Code Assist on GitHub uses a [Developer Connect connection](https://docs.cloud.google.com/developer-connect/docs/git-repo-connections) to connect your GitHub repositories to Google Cloud.

    * This Developer Connect connection is always created in the region `us-east1`.

    * This Developer Connect connection must be created using the **Code Assist Source Code Management** section found in Gemini Code Assist **Agents & Tools**. For instructions, see [Set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github).

    * If you want to add a GitHub repository to a Developer Connect connection that you previously created during Gemini Code Assist on GitHub setup, you must [use Developer Connect](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#link-repos) to do so.




## What's next

  * [Set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github).
  * [Use Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github).
  * Learn how to [customize Gemini Code Assist on GitHub behavior](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
