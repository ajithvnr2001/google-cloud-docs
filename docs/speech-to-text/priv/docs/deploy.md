---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/deploy/
title: Quickstart: Deploy the API \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:31.257425+00:00
---

# Quickstart: Deploy the API  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  Quickstart: Deploy the API Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

## Prerequisites

  1. Complete all required steps in the [before you begin](https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin) quickstart.



## Deploy the API using the marketplace app UI

  1. Navigate to the [on-prem solution](https://console.cloud.google.com/marketplace/details/speech-onprem/speech-to-text-on-prem) and enter your [chosen configuration values](https://docs.cloud.google.com/speech-to-text/priv/docs/configurations):

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/deploy.png)

  2. You can either use an existing namespace, or create a new one:

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/namespace.png)


**Note:** For instructions on deleting or uninstalling the On-Prem solution, see [manage your Speech-to-Text On-Prem solution](https://docs.cloud.google.com/speech-to-text/priv/docs/manage).

## Deploy the marketplace app using the command line

  1. You can either set the configuration payload with customized [parameter values](https://docs.cloud.google.com/speech-to-text/priv/docs/configurations) or use a set of default values for easy copy-pasting. If you would like to use customized parameter values choose Option A, below. Otherwise, use the default values in Option B.

     1. **Option A** : Configuration payload with customized values:
            
            PARAMETERS='{
              "name": "'$NAME'",
              "namespace": "'$NAMESPACE'",
              "asr.publicIP": "'$PUBLIC_IP'",
              "asr.cpu": '$CPU',
              "asr.memory": "'$MEMORY'",
              "reportingSecret": "reporting-secret",
              "asr.image": "gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem:'$VERSION'",
              "configure.image": "gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem/configure:'$VERSION'",
              "asr.metric_project_id": "'$METRIC_PROJECT'",
              "asr.gsa_secret": "'$GSA_SECRET'",
              "istio.enabled": "'$ENABLE_ISTIO'",
              "configure.model1": "'$MODEL1'",
              "configure.model2": "'$MODEL2'",
              "configure.model3": "'$MODEL3'"
            }'
            

     2. **Option B** : Default configuration payload:
            
            PARAMETERS='{
              "name": "speech",
              "namespace": "speech",
              "reportingSecret": "reporting-secret",
              "asr.image": "gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem:'$VERSION'",
              "configure.image": "gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem/configure:'$VERSION'",
              "asr.metric_project_id": "$METRIC_PROJECT",
            }'
            

  2. Select a version :
         
         VERSION=1.0
         

  3. For On-Prem clusters, run the below command($KUBECONFIG is the path of the yaml file of the user cluster):
         
         export KUBE_CONFIG=${KUBECONFIG}
         

  4. Run the deploy command:
         
         mpdev /scripts/install --deployer=gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem/deployer:$VERSION
         --parameters="$PARAMETERS"
         

  5. Check to see if the deployment is ready (this can take several minutes the first time it's run). The number of **READY** pods should match your chosen $REPLICA value.
         
         kubectl get deployment $NAME --namespace $NAMESPACE
         

For example:

![](https://docs.cloud.google.com/static/speech-to-text/priv/docs/images/output.png)




## What's next

Learn how to [send a query](https://docs.cloud.google.com/speech-to-text/priv/docs/query) to the Speech-to-Text On-Prem API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
