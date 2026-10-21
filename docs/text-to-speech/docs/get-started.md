---
url: https://docs.cloud.google.com/text-to-speech/docs/get-started/
title: Get started with Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:17.165245+00:00
---

# Get started with Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback 

#  Get started with Cloud Text-to-Speech Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Text-to-Speech is an API that is powered by Google's artificial intelligence (AI) technology. You send your transcript data to Cloud Text-to-Speech in an API call, then receive natural-sounding, synthetic human speech as playable audio in response. For more information on how Cloud Text-to-Speech works, see the [basics](https://docs.cloud.google.com/text-to-speech/docs/basics) page.

This guide walks you through the steps necessary to start sending requests to the Cloud Text-to-Speech API. See the [code samples](https://docs.cloud.google.com/text-to-speech/docs/samples) section for examples of how to make a request to the API and receive a response, or learn how to use these samples by following the Cloud Text-to-Speech [quickstarts](https://docs.cloud.google.com/text-to-speech/docs/quickstarts) and [how-to guides](https://docs.cloud.google.com/text-to-speech/docs/how-to).

## Enable the Cloud Text-to-Speech API

Before you can begin using Cloud Text-to-Speech, you must enable the API in the Google Cloud console:

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).

  2. Open the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard) and either choose an existing project or create a new one. For details about creating a project, see the [Google Cloud documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  3. If you create a new project, you will be prompted to link a billing account to this project. If you are using a pre-existing project, make sure that you have billing enabled.

[Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

**Note:** You must enable billing to use Cloud Text-to-Speech API; however, you won't be charged unless you exceed the free quota. See our [pricing](https://docs.cloud.google.com/text-to-speech/pricing) page for more details.
  4. Once you have selected a project and linked it to a billing account, you can enable the Cloud Text-to-Speech API. Go to the **Search products and resources** bar at the top of the page and type in **"speech"**. Select the **Cloud Text-to-Speech API** from the list of results.

  5. To try Cloud Text-to-Speech without linking it to your project, choose the **Try this app** option. To enable the Cloud Text-to-Speech API for use with your project, click **Enable**.

  6. Set up authentication for your development environment. For instructions, see [Set up authentication for Cloud Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/authentication#authn-how-to).




## Disable the Cloud Text-to-Speech API

To disable the Cloud Text-to-Speech API, navigate to your Google Cloud dashboard and click the **Go to APIs overview** link in the **APIs** box. Click **Cloud Text-to-Speech API** , then click the **Disable API** button at the top of the page.

## What's next

Learn how to send a transcription request to the Cloud Text-to-Speech API using [client libraries](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries) or the [command line](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-command-line).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
