---
url: https://docs.cloud.google.com/service-health/docs/enable-api-config-connector/
title: Enable Personalized Service Health for a project using Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:19.514992+00:00
---

# Enable Personalized Service Health for a project using Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/enable-api-config-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Enable Personalized Service Health for a project using Config Connector Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to enable a project for service health events processing using [Config Connector](https://cloud.google.com/config-connector/docs/overview) programmatically, if you're using Kubernetes and want to use the Service Health API.

  1. Follow the [prerequisites](https://cloud.google.com/config-connector/docs/how-to/getting-started#before_you_begin) for using Config Connector.

  2. Decide on the API VERSION: `v1` or `v1beta`.

  3. Create a file named `psh-enable.yaml` and copy the following snippet into it: 
         
         apiVersion: serviceusage.cnrm.cloud.google.com/API VERSION
         kind: Service
         metadata:
           name: servicehealth.googleapis.com
         spec:
           projectRef:
             external: projects/PROJECT_ID
         

  4. Run the following command: 
         
         kubectl apply -f psh-enable.yaml 
         

The following message appears:
         
         service.serviceusage.cnrm.cloud.google.com/servicehealth.googleapis.com created
         




Personalized Service Health will take up to 24 hours to start processing service health events.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
