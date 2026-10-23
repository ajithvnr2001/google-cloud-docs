---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/manage/
title: Manage your Speech-to-Text On-Prem solution \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:30.752237+00:00
---

# Manage your Speech-to-Text On-Prem solution  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  Manage your Speech-to-Text On-Prem solution Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

## Scale your solution

To scale (horizontally) the number of replicas in the solution to $REPLICAS, run:
    
    
    kubectl scale deployment $NAME --namespace $NAMESPACE
    --replicas $REPLICAS
    

## Delete/Uninstall your solution

Run:
    
    
    kubectl delete application $NAME --namespace $NAMESPACE
    

## Update the image version

When there is a new model update, you need to do a [rolling deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) directly. When there is a new version for either infra or language change, set the version to $VERSION by running:
    
    
        kubectl set image deployment/$NAME --namespace $NAMESPACE
        asr=gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem:$VERSION
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
