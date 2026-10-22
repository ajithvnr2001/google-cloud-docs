---
url: https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview/
title: Code customization overview \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:46.929047+00:00
---

# Code customization overview  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Code customization overview Stay organized with collections  Save and categorize content based on your preferences. 

Code customization, a feature in [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) Enterprise, lets you get code suggestions from Gemini Code Assist Enterprise that are based on your organization's private repositories, and thus aligned to your organization's coding style.

With code customization, developers can use remote context from your organization directly in the IDE, as the following diagram shows:

![Code customization connects Gemini Code Assist to your code repository, which lets Gemini Code Assist offer coding suggestions in your IDE.](https://docs.cloud.google.com/static/gemini/images/code-customization-with-gemini-cli.png)

As you code, Gemini Code Assist searches your private index for code that is similar to what you're trying to write. It then includes relevant matches in the code prompt and sends these matches to the Gemini Code Assist recommendations service. Code customization keeps recommendations fresh by reindexing your codebase every 24 hours to ensure that code suggestions remain up to date. Gemini Code Assist returns the generated code to you.

Unlike the full codebase awareness feature, which is limited to searching files in the current folder and open tabs in your IDE, code customization searches all repositories in your index. After code customization is set up, it works as part of the code completion and code generation features.

Both Gemini Code Assist and code customization are managed services. You license usage by seats per month.

## Securing access and storage of private code

Google provides security of your stored private code in several ways:

  * We index and store your code in a dedicated single-tenant environment.
  * [Administrative access controls](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access) help prevent Google employees from accessing your content without justification and, optionally, explicit approval.
  * The Gemini model doesn't train on your private source code.
  * Your results are private to you, and we don't share your results with other customers.



For further details on Google's security measures, see the [Google security overview](https://cloud.google.com/security/overview/whitepaper).

Here's how you can control access to your data:

  * You can use Identity and Access Management (IAM) permissions to help control individuals who can get code suggestions from your codebase.
  * You can [create an `.aiexclude` file](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization#optional_choose_which_files_are_not_indexed) to choose specific repositories or parts of repositories that Gemini Code Assist indexes.



To configure code customization in your IDE, see [Configure Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

## Limitations

  * Google limits the number of code repository indexes to one for each project and for each organization.
  * The maximum number of repositories that can be indexed is 20,000.
  * The maximum number of repository groups per code repository index is 500.
  * The maximum number of repositories per repository group is 500.
  * Code customization is supported in the VS Code Gemini Code Assist extension (version 2.18.0+), the IntelliJ Gemini Code Assist plugin (version 1.1.0), Cloud Workstations, and the Cloud Shell Editor.
  * Code customization supports repositories hosted on github.com, gitlab.com, bitbucket.org, and on-premises repositories hosted on GitLab Enterprise, GitHub Enterprise, and Bitbucket Data Center.
  * Code customization doesn't support [GitHub Enterprise Cloud IP restrictions](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization).
  * Code customization supports only [Developer Connect connections](https://docs.cloud.google.com/developer-connect/docs/git-repo-connections) in the following locations (regions):

    * `us-central1`
    * `europe-west1`
    * `asia-southeast1`
  * Code customization doesn't index media. Code customization supports only documentation (in Markdown) and the following languages:

    * C, C++, and C#
    * Golang
    * Java
    * JavaScript
    * Kotlin
    * PHP
    * Python
    * Rust
    * TypeScript
    * Verilog and SystemVerilog

All other coding languages are not indexed or used in code customization. To request support for a coding language, click **Send feedback** on this page, and then select **Product feedback**.




## What's next

  * [Configure Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).
  * [Use code customization](https://docs.cloud.google.com/gemini/docs/codeassist/use-code-customization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
