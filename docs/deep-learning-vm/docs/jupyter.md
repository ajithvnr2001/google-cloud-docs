---
url: https://docs.cloud.google.com/deep-learning-vm/docs/jupyter/
title: Connect to JupyterLab \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:37.455539+00:00
---

# Connect to JupyterLab  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/jupyter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Connect to JupyterLab Stay organized with collections  Save and categorize content based on your preferences. 

When you start a Deep Learning VM Images instance, a JupyterLab session is initialized.

To set up [SSH port forwarding](https://cloud.google.com/solutions/connecting-securely#port-forwarding-over-ssh), complete the following steps, and then access your JupyterLab session through a local browser:

  1. Run the following command by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) in your preferred terminal or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true):
         
         gcloud compute ssh \
             --project PROJECT_ID \
             --zone ZONE \
             INSTANCE_NAME \
             -- -L 8080:localhost:8080

Replace the following:

     * `PROJECT_ID`: your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where your instance is located
     * `INSTANCE_NAME`: the name of your instance

**Note:** If using Cloud Shell to run the command, add a `-4` to the SSH flags to use IPv4 to connect. Example: `-- -4 -L LOCAL_PORT:localhost:REMOTE_PORT`

  1. Access your JupyterLab session through a local browser:

     * If you ran the command on your local machine, visit `https://localhost:8080` to access JupyterLab.

     * If you ran the command using [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), access JupyterLab through the ![](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg) Web Preview on port 8080.




## Troubleshooting

**Symptom** : When [using SSH port forwarding to connect to JupyterLab](https://docs.cloud.google.com/deep-learning-vm/docs/jupyter), you are unable to connect to the instance.

**Problem** : You are trying to connect to the wrong TCP socket.

**Solution** :

  * On some Linux clients, the localhost resolves to the IPv6 loopback address (`::1`). Check this by using `ping -c 1 localhost`. If this command returns the IPv6 address, use `-L 8080:127.0.0.1:8080` (rather than `-L 8080:localhost:8080`) in the `gcloud compute ssh` command.

  * Ensure that you connect to `http://localhost:8080` (instead of `https://localhost:8080`) on your local client.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
