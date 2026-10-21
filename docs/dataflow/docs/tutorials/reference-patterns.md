---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/reference-patterns/
title: Reference patterns \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:56.910893+00:00
---

# Reference patterns  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/reference-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Reference patterns Stay organized with collections  Save and categorize content based on your preferences. 

This page provides links to sample code and technical reference guides for common Dataflow use cases. Use these resources to learn, identify best practices, and build features with sample code.

The reference patterns listed here are code-oriented and meant to get you quickly to implementation. To see a broader range of Dataflow solutions, review the list of [Dataflow technical reference guides](https://docs.cloud.google.com/docs/tutorials?q=Dataflow).

## General analytics

Solution | Description | Links  
---|---|---  
**Building a real-time website analytics dashboard** | Learn how to build a dashboard that provides real-time metrics you can use to understand the performance of incentives or experiments on your website. |  Sample code: [Realtime Analytics using Dataflow and Memorystore](https://github.com/GoogleCloudPlatform/redis-dataflow-realtime-analytics) Overview video: [Level Up - Real-time analytics using Dataflow and Memorystore](https://www.youtube.com/watch?v=7NvgleOy480)  
**Building a pipeline to transcribe and analyze speech files** | Use Dataflow to transcribe and analyze uploaded speech files, then save that data to BigQuery for use in visualizations. |  Sample code: [Speech Analysis Framework](https://github.com/GoogleCloudPlatform/dataflow-contact-center-speech-analysis)  
  
## Log analytics

Solution | Description | Links  
---|---|---  
**Building a pipeline to capture Dialogflow interactions** |  Use Dataflow to build a pipeline to capture and store Dialogflow interactions for further analysis. |  Sample code: [Dialogflow log parser](https://github.com/GoogleCloudPlatform/dialogflow-log-parser-dataflow-bigquery)  
  
## Pattern recognition

Solution | Description | Links  
---|---|---  
**Detecting objects in video clips** | This solution shows you how to build a real-time video clip analytics solution for object tracking by using Dataflow and the Video Intelligence API, allowing you to analyze large volumes of unstructured data in near real time. |  Sample code: [Video Analytics Solution Using Dataflow and the Video Intelligence API](https://github.com/GoogleCloudPlatform/dataflow-video-analytics) Apache Beam `Ptransform` for calling Video Intelligence API: [apache_beam.ml.gcp.videointelligenceml module](https://beam.apache.org/releases/pydoc/2.22.0/apache_beam.ml.gcp.videointelligenceml.html)  
**Anonymize (de-identify) and re-identify PII data in your smart analytics pipeline** | This series of solutions shows you how to use Dataflow, Sensitive Data Protection, BigQuery, and Pub/Sub to de-identify and re-identify [_personally identifiable information (PII)_](https://wikipedia.org/wiki/Personal_data) in a sample dataset.  | Technical reference guides:

  * [De-identification and re-identification of PII in large-scale datasets using Sensitive Data Protection](https://docs.cloud.google.com/solutions/de-identification-re-identification-pii-using-cloud-dlp)

Sample code: [Inspect, de-identify, and re-identify sensitive data using the DLP API and Dataflow](https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification)  
  
## Predictive forecasting

Solution | Description | Links  
---|---|---  
**Predict mechanical failures using a vision analytics pipeline** | This solution guides you through building a Dataflow pipeline to derive insights from large-scale image files stored in a Cloud Storage bucket. Automated visual inspection can help meet manufacturing goals, such as improving quality control processes or monitoring worker safety, while reducing costs. |  Sample code: [Vision Analytics Solution Using Dataflow and Cloud Vision API](https://github.com/GoogleCloudPlatform/dataflow-vision-analytics)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
