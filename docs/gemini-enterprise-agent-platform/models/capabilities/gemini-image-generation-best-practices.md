---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-best-practices/
title: Gemini image generation best practices \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:34.335753+00:00
---

# Gemini image generation best practices  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini image generation best practices Stay organized with collections  Save and categorize content based on your preferences. 

To improve your image generation results, follow these best practices:

  * **Be specific:** More details give you more control. For example, instead of "fantasy armor," try "ornate elven plate armor, etched with silver leaf patterns, with a high collar and pauldrons shaped like falcon wings."

  * **Provide context and intent:** Explain the purpose of the image to help the model understand the context. For example, "Create a logo for a high-end, minimalist skincare brand" works better than "Create a logo."

  * **Iterate and refine:** Don't expect a perfect image on your first attempt. Use follow-up prompts to make small changes, for example, "Make the lighting warmer" or "Change the character's expression to be more serious."

  * **Use step-by-step instructions:** For complex scenes, split your request into steps. For example, "First, create a background of a serene, misty forest at dawn. Then, in the foreground, add a moss-covered ancient stone altar. Finally, place a single, glowing sword on top of the altar."

  * **Describe what you want, not what you don't:** Instead of saying "no cars", describe the scene positively by saying, "an empty, deserted street with no signs of traffic."

  * **Control the camera:** Guide the camera view. Use photographic and cinematic terms to describe the composition, for example, "wide-angle shot", "macro shot", or "low-angle perspective".

  * **Prompt for images:** Describe the intent by using phrases such as "create an image of" or "generate an image of". Otherwise, the multimodal model might respond with text instead of the image.

  * **Pass[Thought Signatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking/thought-signatures):** When using Gemini, we recommend that you pass thought signatures back to the model during multi-turn image creation and editing. This lets you preserve reasoning context across interactions. For code samples related to multi-turn image editing using Gemini, see [Example of multi-turn image editing using thought signatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking/thought-signatures#multi-turn-image-editing).




## What's next?

See the following links for more information about Gemini image generation:

  * [Generate images with Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/image-generation)

  * [Edit images with Gemini](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-edit-images)

  * [Gemini image generation limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-generation-limitations)

  * [Gemini image generation and responsible AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/gemini-image-responsible-ai)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
