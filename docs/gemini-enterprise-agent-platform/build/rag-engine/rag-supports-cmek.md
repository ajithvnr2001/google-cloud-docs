---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-supports-cmek/
title: Use CMEK with RAG Engine on Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:29.426585+00:00
---

# Use CMEK with RAG Engine on Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-supports-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Use CMEK with RAG Engine on Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

The [VPC-SC security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.

This page shows you how to enable CMEK to work with RAG Engine on Gemini Enterprise Agent Platform.

## Overview

RAG Engine provides robust options for managing how your data at rest is encrypted. By default, all user data within `RagManagedDb` is encrypted using a Google-owned and Google-managed encryption key, which is the default setting. This default setting helps you to verify that your data is secure without requiring any specific configuration.

If you require more control over your keys used for encryption, RAG Engine supports [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). With CMEK, you can use your cryptographic keys, managed within Cloud Key Management Service (KMS), to protect your RAG corpus data.

## Set up the encryption key with your RAG corpus

To set up an encryption key, follow the steps at [Set up your KMS key and grant permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-ragmanageddb-with-rag#set_up_your_kms_key_and_grant_permissions).

## CMEK limitations for RAG Engine on Gemini Enterprise Agent Platform

RAG Engine on Gemini Enterprise Agent Platform supports CMEK with the following limitations:

  * Before creating a RAG corpus, you must manually enable the RAG Service account. For detailed instructions, see [Grant Permissions to the RAG Engine service agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-ragmanageddb-with-rag#grant_permissions_to_the_vertex_ai_rag_engine_service_agent).

  * CMEK is only supported on `RagVectorDbConfig` of type `RagManagedDb`.

  * The `encryption_spec` field defines the KMS key, and the field is immutable, which means that CMEK can't be enabled or disabled after the RAG corpus is created.

  * No more than 50 unique KMS keys can be used to create RAG corpora per project per region.




## What's next

  * For information about managing your encryption, see [Manage your encryption](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-ragmanageddb-with-rag#manage_your_encryption).

  * For more information on RAG Engine, see [RAG Engine on Gemini Enterprise Agent Platform overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview).

  * To learn more about data at rest, see [Data residency](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency).

  * To learn more about RAG API methods and resources, see [Agent Platform API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
