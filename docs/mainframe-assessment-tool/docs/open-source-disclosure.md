---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/open-source-disclosure/
title: Open source disclosure \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:49:35.229958+00:00
---

# Open source disclosure  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/open-source-disclosure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Resources ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/release-notes)



Send feedback 

#  Open source disclosure Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Assessment Tool values the open source community as an essential resource and partner in innovation. For this reason, you can download a list of licenses for the open source projects used in Mainframe Assessment Tool.

The license information is available in a single zip file. To download this file, run the following command:

### gcloud
    
    
    gcloud storage cp "gs://mainframe-ai-release/mat/v2/licenses.zip" FILE_NAME
    

### curl
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -L https://storage.googleapis.com/mainframe-ai-release/mat/v2/licenses.zip -o FILE_NAME
    

Replace `FILE_NAME` with your chosen filename.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
