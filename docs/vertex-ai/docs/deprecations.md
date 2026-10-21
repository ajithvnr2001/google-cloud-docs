---
url: https://docs.cloud.google.com/vertex-ai/docs/deprecations/
title: Vertex AI deprecations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:45.797331+00:00
---

# Vertex AI deprecations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/deprecations/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/vertex-ai/docs/release-notes)



Send feedback 

#  Vertex AI deprecations Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Vertex AI. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature | Deprecated date | Shutdown date | Details  
---|---|---|---  
Vertex Explainable AI | March 16, 2026 | March 16, 2027 | Vertex Explainable AI is deprecated. Beginning on March 16, 2026, no new features will be added. On March 16, 2027, the capability will be fully sunset and APIs will no longer be available. For alternatives, consider open source libraries for explanations such as [SHapley Additive exPlanations (SHAP)](https://shap.readthedocs.io/) and [Local Interpretable Model Agnostic Explanation (LIME)](https://arxiv.org/html/2305.02012v3).   
Vertex AI Feature Store Optimized online serving | February 17, 2026 | February 17, 2027 | Vertex AI Feature Store Optimized online serving is deprecated. Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the capability will be fully sunset and APIs will no longer be available. To improve latency and cost optimizations, migrate to [Bigtable online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/online-serving-types#bigtable_serving). To efficiently store and serve embeddings, use the purpose-built [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview).   
Vertex AI Feature Store (Legacy) | February 17, 2026 | February 17, 2027 | Vertex AI Feature Store (Legacy) is deprecated. Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023.   
AutoML Video | July 31, 2024 | July 31, 2025 | AutoML Video is no longer available. See [Video tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune_gemini/video_tune) for detailed instructions for fine-tuning Gemini on video data using supervised learning.   
AutoML Text | September 15, 2024 | June 15, 2025 | Starting on September 15, 2024, you can only customize Text classification, entity extraction, and sentiment analysis objectives by moving to Vertex AI Gemini prompts and tuning. Training or updating models for Vertex AI AutoML for Text classification, entity extraction, and sentiment analysis objectives will no longer be available. You can continue using existing Vertex AI AutoML Text models until June 15, 2025. For more information about how Gemini offers enhanced user experience through improved prompting capabilities, see [Introduction to tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models).   
Legacy AI Platform Training | January 23, 2023 | April 7, 2025 | [Migrate to Vertex AI custom training](https://docs.cloud.google.com/vertex-ai/docs/training/overview), which includes all functionality of legacy AI Platform Training as well as new features.   
Legacy AI Platform Prediction | January 23, 2023 | April 7, 2025 | All models, associated metadata, and deployments were deleted after the shutdown date. See [Overview of getting inferences on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview).   
Vertex AI Workbench managed notebooks | January 16, 2024 | April 14, 2025 |  On April 14, 2025, support for managed notebooks ended, and the ability to create managed notebooks instances was removed. Existing instances will continue to function until March 30, 2026, but patches, updates, and upgrades won't be available.  On March 30, 2026, all managed notebooks instances and their associated data will be deleted. There is no recovery of managed notebooks instances after deletion. There isn't a way to convert these instances to Compute Engine virtual machines (VMs). To continue using Vertex AI Workbench, [migrate your managed notebooks instances to Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/managed/migrate-to-instances) before March 30, 2026.   
Vertex AI Workbench user-managed notebooks | January 16, 2024 | April 14, 2025 |  On April 14, 2025, support for user-managed notebooks ended, and the ability to create user-managed notebooks instances was removed. Existing instances will continue to function until March 30, 2026, but patches, updates, and upgrades won't be available.  On March 30, 2026, your user-managed notebooks instances will be converted to standard Compute Engine virtual machines (VMs). You will have full control over these VMs, but they won't be supported or available through Vertex AI Workbench. You will incur costs for these Compute Engine VMs, so we recommend that you delete any VMs that you don't plan to use. To continue using Vertex AI Workbench, [migrate your user-managed notebooks instances to Vertex AI Workbench instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/migrate-to-instances) before March 30, 2026.   
Legacy AI Platform Pipelines | July 31, 2023 | January 31, 2025 | [Migrate to Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction), which includes all functionality of legacy AI Platform Pipelines as well as new features.   
Legacy AI Platform Data Labeling Service | January 23, 2023 | January 31, 2025 | For new labeling tasks, you can [add labels using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/datasets/label-using-console) or access data labeling solutions from our partners in the [Google Cloud Console Marketplace](https://console.cloud.google.com/marketplace/).   
Vertex AI Data Labeling Service | June 30, 2023 | October 3, 2024 | For new labeling tasks, you can [add labels using the Google Cloud console](https://docs.cloud.google.com/vertex-ai/docs/datasets/label-using-console) or access data labeling solutions from our partners in the [Google Cloud Console Marketplace](https://console.cloud.google.com/marketplace/).   
Legacy AutoML Natural Language | July 31, 2023 | August 7, 2024 | New models can no longer be trained nor deployed on the legacy platform. Already deployed models stopped working on May 30, 2024. All the functionality of legacy Vertex AI and new features are available on the Vertex AI platform. See [Migrate to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai) to learn how to migrate your resources.   
Legacy AutoML Video Intelligence | January 23, 2023 | July 31, 2024 | [Migrate to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai), which includes all functionality of legacy AutoML Video Intelligence as well as new features.   
Legacy AutoML Vision | January 23, 2023 | July 31, 2024 | [Migrate to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai), which includes all functionality of legacy AutoML Vision as well as new features.   
Legacy AutoML Tables | January 23, 2023 | July 24, 2024 | [Migrate to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai), which includes all functionality of legacy AutoML Tables as well as new features.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
