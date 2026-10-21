---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/cloud-storage-data-store/
title: Cloud storage data store tool \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:22.355390+00:00
---

# Cloud storage data store tool  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/cloud-storage-data-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Cloud storage data store tool Stay organized with collections  Save and categorize content based on your preferences. 

This tool is used to search and retrieve information from unstructured documents or FAQ content by connecting to a data store populated with your own files.

When you first create the tool, you provide:

  * **Name** : A descriptive name that helps the AI understand the tool's job. Names should start with a verb (for example, `search_internal_docs` or `query_product_manuals`).
  * **Description** : (Optional) An explanation of what the tool does and when the AI should use it. This helps the model decide if this specific data store contains the answer to a user's prompt.
  * **Mock tool response** : An optional configuration used to simulate the tool's output for testing purposes before the data is fully indexed.
  * **Location** : The region where the data store is hosted (for example, global).
  * **Data type** : The format of the content you are importing:

    * Unstructured data: Best for documents like PDFs, HTML files, or text files.
    * FAQ: Best for structured question-and-answer pairs.
  * **Select a folder or a file** : The path to your data in Google Cloud Storage (`gs://*`). You can choose to import a single **File** or an entire **Folder**.

  * **Synchronization frequency** : How often the tool checks for updates in your source files.

    * One time: A single import of the current data.
    * Periodic: Automatically updates the data store when source files change (this setting cannot be changed after creation).



## FAQ data store

FAQ data stores can hold answers to frequently asked questions (FAQ). When user questions are matched with high confidence to an uploaded question, the agent returns the answer to that question without any modification. You can provide a title and a URL for each question and answer pair that is displayed by the agent.

Data must be uploaded to the data store in `CSV` format. Each file must have a header row describing the columns.

For example:
    
    
    "question","answer","title","url"
    "Why is the sky blue?","The sky is blue because of Rayleigh scattering.","Rayleigh scattering","https://en.wikipedia.org/wiki/Rayleigh_scattering"
    "What is the meaning of life?","42","",""
    

The `title` and `url` columns are optional and can be omitted:
    
    
    "answer","question"
    "42","What is the meaning of life?"
    

During the upload process, you can select a folder where each file is treated as a `CSV` file regardless of extension.

Limitations:

  * An extra space character after `,` causes an error.
  * Blank lines (even at the end of the file) cause an error.



## Unstructured data store

Unstructured data stores can contain content in the following formats:

  * `HTML`
  * `PDF`
  * `TXT`
  * `CSV`

**Note:** `CSV` files can also be imported as unstructured content. The same schema requirements outlined in the FAQ data section still apply. Metadata is generated automatically if `title` and `url` columns are provided. Each question and answer pair gets indexed separately. The matching requirements are less strict compared to FAQ `CSV` data stores, and the answer might be rewritten by the agent rather than returned word-for-word.

It's possible (but uncommon) to import files from another project's Cloud Storage bucket. To do this, you need to grant explicit access to the import process. Follow the instructions in the error message, which will contain the name of the user that needs read access to the bucket in order to perform the import.

Limitations:

  * The maximum file size is 2.5MB for text-based formats, 100MB for other formats.



See also [Import from Cloud Storage](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
