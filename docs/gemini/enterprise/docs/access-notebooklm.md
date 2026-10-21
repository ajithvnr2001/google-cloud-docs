---
url: https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm/
title: Use Gemini Notebook Enterprise within Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:02.757222+00:00
---

# Use Gemini Notebook Enterprise within Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Use Gemini Notebook Enterprise within Gemini Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Notebook Enterprise is integrated with Gemini Enterprise. This page describes how end users access Gemini Notebook Enterprise from within the Gemini Enterprise search web app UI and how they can add documents found in searches to a notebook.

**Note:** In the Gemini Enterprise Frontline edition, Gemini Notebook Enterprise support is limited to interacting with published notebooks. Creating new notebooks requires the Gemini Enterprise Standard or Gemini Enterprise Plus editions.

## Access Gemini Notebook Enterprise from the web app

To access Gemini Notebook Enterprise, do the following:

  1. Open the Gemini Enterprise web app.

  2. In the app navigation menu, go to **Agents**.

  3. In the **Made by Google** section, click **Gemini Notebook**.

The Gemini Notebook Enterprise interface opens in the web app.

The notebooks that you created in a particular project and location through the Gemini Notebook Enterprise site are accessible from within Gemini Enterprise web apps. Similarly, notebooks created from within a Gemini Enterprise app are accessible from the Gemini Notebook Enterprise site.




## Add a source to a notebook from Gemini Enterprise (Private preview)

**Preview:** To use this feature, your project must be on the allowlist. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

When Gemini Enterprise returns search results, you might want to add those search results to a notebook. For many document types, you can do this from the search web app with a single click.

Not all document types can be added to notebooks as sources. For example, you can add Google slides but not emails. If a document type can't be added, then the **Add content to…** button isn't available.

### Notebook source limitations and security

Here are a couple of security considerations related to sources in notebooks:

  * Sources as instances: When you add a document as a source to a notebook, a _copy_ of the document is added to the notebook. This means that there are now two copies of the document, one that belongs to original owner and one that belongs to the owner of the notebook. Changes to the original document aren't reflected in the copy. This has security implications: if you want to change who can access the information, you need to make the change on both documents, the original and the copy.

  * Shared notebooks:

    * Sources in shared notebooks: If a notebook is shared with others, you can't add more sources to it. This restriction is to maintain access control. See [Notebooks that can't be shared](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks#no-sharing).

    * Shared notebooks as search sources: If a notebook is shared with you, but you aren't the owner, Gemini Enterprise doesn't use it as a data source for search results. This restriction is to maintain access control and aligns with the security behavior of other data connectors.




### Procedure

To add a document returned by search as a source to a notebook, do the following:

  1. Click book_4_spark **Add content to…**.

  2. Choose to add the content to one of the following:

     * A new notebook
     * An existing notebook



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
