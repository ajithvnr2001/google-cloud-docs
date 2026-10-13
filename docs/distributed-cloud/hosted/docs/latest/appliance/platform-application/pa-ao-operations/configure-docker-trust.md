---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-trust/
title: Configure Docker to trust the Harbor root CA \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:10.286706+00:00
---

# Configure Docker to trust the Harbor root CA  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/configure-docker-trust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure Docker to trust the Harbor root CA Stay organized with collections  Save and categorize content based on your preferences. 

Harbor instances use Transport Layer Security (TLS) certificates issued by your organization's trusted root Certificate Authority (CA). This encrypts the connection between your Docker client and Harbor registry to secure images from unauthorized access.

## Before you begin

You must perform these steps before managing your container images:

  1. Install Docker if it is not already installed by following the instructions at <https://docs.docker.com/engine/install/ubuntu/>. Docker is included in Cloud Shell.
  2. Docker requires privileged access to interact with registries. On Linux or Windows, add the user that you use to run Docker commands to the Docker security group. This step is not required on macOS since Docker Desktop runs on a virtual machine as the root user.

     1. For Linux, add the user:
            
            sudo usermod -a -G docker USER
            

     2. For Windows:
            
            net localgroup docker-users DOMAIN\Upan>SER /add
            

Replace `USER` with the username you want to add.




## Configure Docker to trust Harbor Root CA

You must configure your local Docker client to trust your organization's root CA when using the Docker client to communicate with the Harbor instance.

To configure the Docker client to trust the root CA, request the `.crt` file of the root CA from your organization administrator, and copy the organization root CA to:
    
    
    /etc/docker/certs.d/HARBOR_INSTANCE_URL/ca.crt
    

Replace `HARBOR_INSTANCE_URL` with the URL of your Harbor instance. For example, `harbor-1.org-1.zone1.google.gdc.test`.

This command allows your Docker client to establish a HTTPS connection with the Harbor instance.

Alternatively, use the gdcloud CLI to sign in to the organization, generate and use the kubeconfig file for the management API server, and copy the trust bundle in the cluster. For more information, see [Fetch GDC trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pki/fetch-trust-bundles).
    
    
      export REGISTRY=HARBOR_INSTANCE_URL
      mkdir -p /etc/docker/certs.d/${REGISTRY} && echo $(kubectl get secret trust-store-global-root-ext -n platform -o
      jsonpath='{.data.ca\.crt}') | openssl base64 -A -d >
      /etc/docker/certs.d/${REGISTRY}/ca.crt
    

Replace `HARBOR_INSTANCE_URL` with the URL of your Harbor instance. For example, `harbor-1.org-1.zone1.google.gdc.test`.

If the configuration is unsuccessful, you see the following error message:
    
    
    Error response from daemon: Get "https://<HARBOR_INSTANCE_URL>": x509: certificate signed by unknown authority
    

Repeat the steps to solve this issue, and escalate to GDC engineering if necessary.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
