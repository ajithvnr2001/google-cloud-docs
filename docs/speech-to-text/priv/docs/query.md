---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/query/
title: Quickstart: Query the API \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:27.356735+00:00
---

# Quickstart: Query the API  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  Quickstart: Query the API Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

## Prerequisites

  1. Complete all required steps in the [before you begin](https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin) quickstart.
  2. [Deploy the API](https://docs.cloud.google.com/speech-to-text/priv/docs/deploy).



## Overview

You can query the API using the same methods regardless of which installation method you used. How you query the API depends on whether or not you have configured a public endpoint. If your endpoint is **not public** , you will need to determine how to expose the API yourself. There are many options for doing this, including creating an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) if your cluster supports it, [publishing the created service](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types), running [Istio](https://istio.io/), and so on.

The steps outlined below walk you through querying an endpoint. There are two methods:

  1. Query the endpoint from within your cluster (no public IP required).
  2. Query a public IP.



## Query the internal DNS name (no public IP required)

This example runs a query from within the cluster using the Domain Name Service (DNS) name assigned to the service: `$NAME.$NAMESPACE`, such as `speech.speech.` You can either set the environment variables or replace them with actual value in the commands.

  1. Create a new job within the cluster to query the API from. If this job already exists in the cluster, you should remove it first.
         
         kubectl delete jobs.batch -n $NAMESPACE query-api
         
         echo "apiVersion: batch/v1
         kind: Job
         metadata:
           name: query-api
           namespace: $NAMESPACE
         spec:
           template:
             metadata:
               annotations:
                 sidecar.istio.io/inject: 'false'
               labels:
                 app: query
             spec:
               containers:
               - name: entrypoint
                 image: gcr.io/cloud-marketplace/speech-onprem/speech-to-text-on-prem:$VERSION
                 command: ["/bin/sh", "-c"]
                 args:
                 - curl https://raw.githubusercontent.com/GoogleCloudPlatform/python-docs-samples/master/speech/snippets/resources/commercial_mono.wav --output /tmp/audio.wav;
                   /bin/onprem_client --address=$NAME.$NAMESPACE:443 --file_paths /tmp/audio.wav
               restartPolicy: Never
         " | kubectl apply -f -
         

  2. Check the logs to see the transcript:
         
         kubectl logs -n $NAMESPACE --follow $(kubectl get po -n $NAMESPACE -l
         app=query -o=jsonpath='{.items[0].metadata.name}') -c entrypoint
         




## Query a public IP

If you installed Istio in your cluster, make sure that you have Istio Ingress Gateway running with a public IP. If you haven't installed Istio you can set the value for `$PUBLIC_IP`. Once this is completed, you can submit transcription queries to a public endpoint.

  1. If you have Istio installed, follow the [instructions](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/#determining-the-ingress-ip-and-ports) to get the Ingress public IP and set it to `PUBLIC_IP`.

  2. If you don't have Istio installed, validate that the IP address was bound. It should appear under `EXTERNAL-IP` below. If it doesn't appear after a few minutes, navigate to [your cluster in the console](https://console.cloud.google.com/kubernetes/list) for troubleshooting.
         
         kubectl get service $NAME --namespace $NAMESPACE
         

     1. Copy the `onprem_client` binary from the docker image:
            
            kubectl cp -n $NAMESPACE $(kubectl get pod -n $NAMESPACE -l
            app.kubernetes.io/name=$NAME -o=jsonpath='{.items[0].metadata.name}'
            ):/bin/onprem_client ./onprem_client
            
            kubectl cp -n $NAMESPACE $(kubectl get pod -n $NAMESPACE -l
            app.kubernetes.io/name=$NAME -o=jsonpath='{.items[0].metadata.name}'
            ):/usr/grte.tar ./grte.tar
            
            sudo tar -xvf grte.tar -C /
            
            chmod a+x ./onprem_client
            

     2. Use the `onprem_client` binary to submit a query:
            
            ./onprem_client --address ${PUBLIC_IP}:443
            --file_paths /path/to/audio.wav
            


**Note:** For languages other than en-us, an extra parameter is needed, such as \--language_code yue-Hant-HK.

## What's next

Learn how to [send a transcription request](https://docs.cloud.google.com/speech-to-text/priv/docs/transcribe) to the Speech-to-Text On-Prem API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
