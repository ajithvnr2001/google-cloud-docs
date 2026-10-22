---
url: https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve/
title: Accelerate research and development with Co-Scientist agent \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:37.007457+00:00
---

# Accelerate research and development with Co-Scientist agent  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Accelerate research and development with Co-Scientist agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

These features are Generative AI Preview offerings, subject to the "Pre-GA Offerings Terms" of the [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). For these Generative AI Preview offerings, Customers may elect to use them for production or commercial purposes, or disclose Generated Output to third-parties, and may process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud.

The AI/ML Data Location terms also apply to Co-Scientist, as an Agentic AI Service on Gemini Enterprise, subject to its restrictions and those listed in the [Google Cloud Platform Services with Data Residency](https://cloud.google.com/terms/data-residency) page.

Co-Scientist and AlphaEvolve are Google-developed agents that accelerate research and development processes. These agents leverage Gemini to automate complex scientific reasoning and algorithmic discovery.

**Note:** Access to these agents is restricted. To request access, contact your Google account team. Your account team provides detailed product documentation once they grant access.

## Overview of Co-Scientist agent

Co-Scientist is a multi-agent AI system built on Gemini, designed to act as a virtual scientific collaborator. The system helps researchers uncover original knowledge and formulate novel research hypotheses and experimental proposals. By combining AI reasoning with the scientific method, Co-Scientist enables scientists to navigate literature, synthesize insights across domains, and accelerate biomedical discoveries.

![Co-scientist](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/coscientist-alphaevolve/coscientist.png)

### How it works

Co-Scientist is built on a multi-agent architecture and an asynchronous task execution framework to scale test-time computation. This design allows the system to reason, debate, and improve outputs iteratively.

When you provide a research goal in natural language, Co-Scientist coordinates the following specialized agents:

  * **Generation agent:** Explores literature using web search, synthesizes findings, and formulates initial hypotheses.
  * **Reflection agent:** Acts as a peer reviewer to examine the correctness, quality, and safety of generated hypotheses.
  * **Ranking agent:** Evaluates and prioritizes research proposals using an Elo-based tournament.
  * **Evolution agent:** Refines top-ranked hypotheses by grounding them in literature and combining innovative ideas.
  * **Proximity agent:** Organizes tournament matches and deduplicates hypotheses using a proximity graph.
  * **Meta-review agent:** Synthesizes insights from all reviews and debates into a comprehensive research roadmap.



A dedicated **Supervisor agent** orchestrates the process, allocates resources, and manages the worker queue to maintain a self-improving loop of scientific reasoning.

### Use cases

Co-Scientist solves complex problems across multiple scientific disciplines, specifically those requiring deep subject matter expertise and trans-disciplinary insights. Example use cases include:

  * **Drug repurposing:** Identify novel therapeutic indications for approved drugs by analyzing molecular signatures, signaling pathways, and literature-based information.

  * **Target discovery:** Propose new biological components and epigenetic targets for complex diseases and streamline hypothesis selection for experimental validation.

  * **Mechanistic explanations:** Generate hypotheses for intricate problems, such as antimicrobial resistance, by synthesizing fragmented scientific data.




For more information and additional use cases, see the [Accelerating scientific breakthroughs with an AI Co-Scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) blog.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
