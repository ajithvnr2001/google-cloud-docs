---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview/
title: MedLM models overview \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:08.263082+00:00
---

# MedLM models overview  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  MedLM models overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** MedLM is deprecated. Access to MedLM will no longer be available on or after September 29, 2025. 

**Disclaimer:** MedLM on Vertex AI is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) in the US, Brazil, and Singapore to a limited group of customers, and available in [Preview](https://cloud.google.com/products#product-launch-stages) to a limited group of customers outside the US. This releases focuses on Medical Q&A and Medical Summarization use. By using the MedLM API, you agree to the [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy) and the Google Cloud Platform [Service-Specific Terms](https://cloud.google.com/terms/service-terms), and you agree to notify and coordinate with Google in good faith to address any regulatory inquiries regarding your use of MedLM. For this product, you can process personal data as outlined in the Data Processing Security Terms, subject to the restrictions described in the Google Cloud Platform Terms of Service. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Provided that you enter into a Business Associate Agreement with Google that covers your use of Google Cloud Platform Services, MedLM API can be used to process Protected Health Information subject to the Health Insurance Portability and Accountability Act (HIPAA) of 1996 and/or any amendments or regulations under HIPAA.

**Caution:**

  * Before activating Production use for MedLM, customers must reach out to Google Product Team to discuss usage. 
  * MedLM has not been designed or developed to be used as a medical device. Any output should be verified by a Healthcare Professional (HCP), and no direct diagnosis should be claimed. 
  * The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased (for example, stereotypes or other harmful content) information and should be reviewed. All summaries or answers should be considered draft and not final. 
  * If Vertex AI detects content that violates our policies, including [Google Cloud Platform Acceptable Use Policy](https://cloud.google.com/terms/aup) and [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy), a response is not returned. 
  * When used by HCPs for Q&A purposes, MedLM is only intended for use as an educational tool for medical training or to reinforce the HCP's prior training. 
  * LLM output may not follow the exact format laid out in the prompt. The prompt design to extract information for each field should take into account that the format may deviate from the original (for example, dashes in field names, exact capitalization of letters). 



## Background

MedLM is a family of foundation models fine-tuned for the healthcare industry. [Med-PaLM 2](https://sites.research.google/med-palm/) is one of the text-based models developed by Google Research that powers MedLM, and was the first AI system to reach human expert level on answering US Medical Licensing Examination (USMLE)-style questions. The development of these models has been informed by specific customer needs such as answering medical questions and drafting summaries. 

## MedLM model card

The MedLM model card outlines the model details, such as MedLM's intended use, data overview, and safety information. Click the following link to download a PDF version of the MedLM model card:

[Download the MedLM model card](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/medlm/MedLM-model-card.pdf)

## Regulatory information

### MedLM intended use

MedLM is based on Google Research's medically-tuned large language model, Med-PaLM 2. It is intended to be used for question answering and creating draft summaries from existing documentation -- to be reviewed, edited, and approved by the user before use. MedLM is also used for educational purposes for a Healthcare Professional (HCP) to engage in medical questioning and answering to help support the HCP.

**Caution:** The output of the model(s) is not considered final, and gives only a draft response which the HCP should review. MedLM must not be used for any diagnostic or therapeutic purpose, and is not to be used in direct patient care.

### Conditions of use and out-of-scope applications

  * MedLM customers and users must abide by the [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy), Google Cloud Platform [Service Specific Terms](https://cloud.google.com/terms/service-terms), [Terms of Service](https://cloud.google.com/terms), [Acceptable Use Policy](https://cloud.google.com/terms/aup), [User Guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview), and other product documentation.
  * As part of [Service Specific Terms](https://cloud.google.com/terms/service-terms), customers may not use MedLM for clinical purposes (for clarity, non-clinical research, scheduling, and other administrative tasks are not restricted), to provide medical advice, or in any manner that is overseen by or requires clearance or approval from a medical device regulatory agency. 
    * Direct patient use is prohibited. The product functions as an assistive tool for a clinician, HCP, or knowledge worker with a high degree of expertise, education, or experience in the healthcare and life sciences industry.
    * Use of MedLM as a Software as a Medical Device is prohibited.
  * The intended use for MedLM is to draft documents and responses that would be reviewed by a "human in the loop" before usage.
  * We recommend usage of MedLM solely for Medical Q&A and Summarization use cases at this stage: 
    * Long form Q&A
    * Multiple choice Q&A
    * Summarizations, such as creation of After Visit Summaries or History and Physical Examination notes
  * Examples of medical device uses that are not permitted include (but are not limited to): 
    * Analysis of patient records, prescription patterns, geographical data, and so forth to identify patients with possible diagnosis of opioid addiction.
    * Analysis of patient-specific medical information to detect a life-threatening condition, such as stroke or sepsis, and generate an alarm or an alert to notify a HCP.
    * Analysis of patient-specific medical information found in the medical records, including the most recent mammography report findings, to provide a list of follow-up actions or treatment options.
    * Analyzing prioritized list of FDA-authorized depression treatment options to an HCP based on an analysis of reported outcomes in a database of clinical studies using medical information (for example, diagnosis and demographics) from the patient's medical record.



MedLM is not intended to be used as a medical device. Customer use cases must be consistent with the intended use and conditions of use. Q&A should only be used for educational purposes and summarization outputs must always be independently reviewed and verified by the user based on their clinical judgment.

### MedLM locations

MedLM is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) in the US, Brazil, and Singapore to a limited group of customers, and available in [Preview](https://cloud.google.com/products#product-launch-stages) to a limited group of customers outside the US.

## MedLM versus PaLM

Usage of MedLM is similar to that of PaLM. However, unlike PaLM, MedLM has been tuned for specific medical tasks, such as select forms of summarization and medical question-answering.

As with most new applications of LLMs, however, we encourage performing careful validation and/or tuning your usage of MedLM to ensure good performance on these tasks. For tasks that don't require specialized medical expertise (for example, general NLP tasks or tasks which operate on medical data but don't require expertise), we expect that MedLM may perform similar to more generic models such as PaLM, and encourage experimenting with both on the specific use-case. See also the [Med-PaLM paper](https://www.nature.com/articles/s41586-023-06291-2) for more details on the Q&A tasks that MedLM has been trained and validated on. Capabilities like grounding of the responses in authoritative medical sources or accounting for the time-varying nature of medical consensus are not built into the model, as called out in the publication.

As per our [Generative AI Service-Specific Terms](https://cloud.google.com/terms/service-terms), customers may not use MedLM for clinical purposes (for clarity, non-clinical research, scheduling, or other administrative tasks is not restricted), to provide medical advice, or in any manner that is overseen by or requires clearance or approval from a medical device regulatory agency.

## MedLM models

In the current MedLM release, two models are being made available:

  * MedLM-medium
  * MedLM-large



MedLM-medium and MedLM-large have separate endpoints and provide customers with additional flexibility for their use cases. MedLM-medium provides customers with better throughputs and includes more recent data. MedLM-large is the same model from the preview phase. Both models will continue to be refreshed over the product lifecycle. In this page, "MedLM" refers to both models.

## Customer responsibilities

MedLM has been developed with trained and licensed healthcare practitioner users in mind. Google Cloud customers and end users should understand that LLMs and Generative AI are inherently probabilistic and may not always be accurate. Without adequate consideration or controls by customers, use of Generative AI models in healthcare may constitute a hazard to patients due to inaccurate content, missing content, or misleading, biased content.

  * Customers should implement appropriate hazard mitigations for all MedLM uses, such as adequate practitioner education, training, assessment of equity, and appropriate technical controls.
  * Customers must also perform their own evaluations for performance and safety to ensure prevention of harm for their use cases.



MedLM may produce less accurate results for some groups compared to others depending on the question and how it is posed. Customers should be aware that differing performance of outputs of the model across demographic groups has the potential to exacerbate health inequities and perpetuate harmful biases. _Such inaccuracies of outputs are not unique to MedLM_ and often stem from multiple factors, such as existing social and structural inequities, medical misconceptions, negative stereotypes, and lack of diversity in training data.

  * Customers should consider implementing equity-focused evaluations and mitigations. This includes assessing model performance and behavior for intended use cases within various populations (for example, race/ethnicity, socioeconomic status (SES), geography, gender identity, sexual orientation, age, language preference, caste, and so forth); obtaining feedback on performance; engaging interdisciplinary experts and external partners that specialize in defining and addressing social and structural aspects of health; and conducting continuous monitoring efforts to assess and address issues of bias.



## Request access

Access to the MedLM models is restricted. To request access, contact your Google Cloud account team.

## Provide feedback

Your feedback throughout your experience will help us improve future model versions and ensure that we continue to deliver the best possible experience for our users. Contact [medlm-feedback@google.com](mailto:medlm-feedback@google.com) and copy your Google Cloud account team and Google Cloud Customer Engineer (CE). _This email address is not for immediate support. To request immediate support, contact your Google Cloud account team or Google Cloud Customer Engineer (CE)._

Email responses will be used as Feedback under the terms of your Agreement for Google Cloud Services and will be collected in accordance with the Google Cloud Privacy Notice. Do not include any personal information (names, email addresses) in this feedback form or other data that is sensitive or confidential. Note that data may be reviewed using both human reviewed and automated processing.

## Report abuse

You can report suspected abuse of the MedLM API, any generated output that contains inappropriate material, or inaccurate information in [Report suspected abuse on Google Cloud](https://support.google.com/code/contact/cloud_platform_report). In the **Google Cloud Platform Service** list, select **Cloud AI**.

## Pricing

**Content access:** Access to the MedLM pricing page is restricted to approved users signed in with an authorized email address. To request access, contact your Google Cloud account team. If you have access, see [MedLM pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/pricing). 

## What's next

  * See examples of how to [create MedLM prompts](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/medlm/medlm-prompts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
