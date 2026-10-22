---
url: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze/
title: Analyze data and create images and videos \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:40.690698+00:00
---

# Analyze data and create images and videos  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Analyze data and create images and videos Stay organized with collections  Save and categorize content based on your preferences. 

Beyond simple conversations, the assistant offers advanced tools that let you perform complex actions, from analyzing data and generating reports to creating custom images and videos.

## Access actions with the Tools menu

To access tools within a chat:

  1. Click the **Tools** button in the chat box. A list of shortcuts appears.

![Open the Tools menu](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-tools.png)Open the Tools menu 
  2. Select a tool from the list. Some of the tools that might be available to you let you perform the following tasks:

     * **Search internal sources** to limit Gemini Enterprise to searching your enterprise data when responding to prompts.

     * **Search Google** to limit Gemini Enterprise to searching the web when responding to prompts.

     * **Run Deep Research** , a Made by Google agent, to research a topic in depth.

     * **Generate images** to generate an image based on your description using Gemini Enterprise.

     * **Create videos** to generate a video based on your description using Gemini Enterprise.

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition.



## Analyze data and create reports

The assistant can analyze data you provide by uploading files, pasting data, or referring to search results. You can ask the assistant to perform calculations and create tables or reports from your data.

To analyze data, do the following:

  1. (Optional) Upload a file.

**Note:** The first time someone in your organization adds a file from Microsoft OneDrive Business, your tenant might require administrator approval. If it does, users see a **Need admin approval** screen when they sign in to Microsoft Entra ID: "Please ask an admin to grant permission to this app before you can use it." To resolve this, a Microsoft Entra ID Global Administrator or Application Administrator for your tenant must complete the first authorization:

     1. In the Gemini Enterprise web app, click the add_circle_outline icon in the chat box, and then click **Add from OneDrive Business**.
     2. Sign in with the administrator account. If the **Need admin approval** screen appears, click **Have an admin account? Sign in with that account**.
     3. On the permissions screen, select **Consent on behalf of your organization** , and then click **Accept**.

This step is required only once for your tenant. After the administrator completes the authorization, other users can add files from OneDrive without the approval screen. For more information, see the [Microsoft Entra ID documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent).

  2. Enter a prompt. Example prompts for data analysis include the following:

     * "Can you tell me what the total revenue for December is?"

     * "Which product had the highest sales?"

     * "Generate a sales report for the last quarter, including a breakdown by product category and a comparison to the previous year."




## Generate an image

If your admin has enabled image generation, you can use the assistant to generate custom visuals like artwork, UI mockups, and charts from a text prompt.

To create an image:

  1. In the chat box, click **Tools > Generate an image**.

  2. Describe the image that you want Gemini Enterprise to create and submit the prompt. Example prompts for image and chart generation include the following:

     * "Generate a high-fidelity mockup of a mobile banking app with a clean, minimalist design, displaying a user's account balance and recent transactions."

     * "I need a visualization of our customer demographics. Can you create a chart showing the distribution of age, gender, and location?"

![Generate a custom image](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/generate-image.png)Generate a custom image 
  3. After generating the initial image, upload existing images or enter follow-up text prompts to refine the generated image.

  4. You can export any finished image or chart in PNG format.




## Generate a video

If your admin has enabled video generation, you can use the assistant to create a short video based on your description.

To create a video:

  1. In the chat box, click **Tools > Generate a video**.

  2. Describe the video that you want Gemini Enterprise to create and submit the prompt.

![Generate a custom video](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/generate-video.png)Generate a custom video 
  3. After you receive the assistant's response, you can send follow-up prompts to refine the result.




## View, download, and search generated images and videos

If your admin has enabled image or video generation, you can view and download generated images and videos from your previous chats. You can also search your generated content using natural language.

To view, search, and interact with your generated content:

  1. Click **Library**. Your generated images and videos are shown.

![View all of your generated content](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-library.png)View all of your generated content 

To filter results by type, click **Images** or **Videos**.

  2. Click a generated visual to view it.

![Interact with your generated content](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-interact.png)Interact with your generated content 

Choose an option:

     * To open the chat where you generated an image or video, click the chat_bubble_outline icon.

     * To copy an image, click the content_copy icon.

     * To download an image or video, click the save_alt icon.

  3. Click the search icon to search your generated images and videos. Type a description of what you're looking for.

**Note:** The search results show up to 10 matching images and videos.![Search your generated content](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-library-search.png)Search your generated content 



## Usage limits and overages

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

  * Your project reached its monthly spend cap.
  * Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 



This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
