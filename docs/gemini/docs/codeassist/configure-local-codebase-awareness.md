---
url: https://docs.cloud.google.com/gemini/docs/codeassist/configure-local-codebase-awareness/
title: Configure local codebase awareness \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:35.070115+00:00
---

# Configure local codebase awareness  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/configure-local-codebase-awareness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Configure local codebase awareness Stay organized with collections  Save and categorize content based on your preferences. 

Local codebase awareness improves the relevance of Gemini Code Assist responses through indexing and supporting techniques. Gemini Code Assist uses the current open file as context. An [agent](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode) is able to use tools to find and read the files it needs. You can also [specify files and folders in your workspace context](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#specify-context).

By default, local codebase awareness is enabled, but you can [exclude files from Gemini Code Assist use](https://docs.cloud.google.com/gemini/docs/codeassist/create-aiexclude-file), and VS Code users can disable local codebase awareness entirely. To disable local codebase awareness entirely, perform the following steps:

###  VS Code 

  1. In your IDE, navigate to **Settings** > **Extensions** > **Gemini Code Assist**.

  2. Search for the **Local Codebase Awareness** setting.

  3. Unselect the checkbox to disable local codebase awareness.

  4. Reload your IDE.




###  IntelliJ 

Local codebase awareness configuration settings aren't supported in Gemini Code Assist for IntelliJ and other JetBrains IDEs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
