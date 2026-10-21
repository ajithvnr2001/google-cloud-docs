---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/external-lb-for-mc/
title: Deploy a Load Balancer for Manufacturing Connect (MC) \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:41.796031+00:00
---

# Deploy a Load Balancer for Manufacturing Connect (MC)  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/external-lb-for-mc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy a Load Balancer for Manufacturing Connect (MC)

Manufacturing Connect edge (MCe) can be deployed with a TCP Load Balancer, in which case you must upload an SSL certificate to the Manufacturing Connect (MC) application to secure traffic between MC and clients. However, MDE provides a Helm chart to provision an External HTTP Load Balancer with a Google-managed SSL certificate.

#### Before you begin

Make sure to complete the following prerequisites:

  * You deployed [MCe](https://console.cloud.google.com/marketplace/product/litmus-public/intelligent-manufacturing-connect) from the Google Cloud Marketplace.
  * MC is deployed in the `default` GKE cluster namespace. If MC is deployed in a different namespace, append the `--namespace` option to `helm` and `kubectl` commands and provide the name of the namespace in which MC is deployed.
  * You are authorized to deploy Kubernetes resources to the GKE cluster in which MCe is deployed.
  * You have downloaded and un-archived the MDE release package.



#### Steps

  1. From the MDE release package root, navigate to the `optional/charts/mc/helm-mc-lb` directory using the following command:
         
         cd optional/charts/mc/helm-mc-lb
         

  2. Obtain the cluster credentials using the following commands:
         
         export CLUSTER_NAME="mc-cluster"
         
         export CLUSTER_LOCATION=$(gcloud container clusters list \
         --filter="name:${CLUSTER_NAME}" \
         --format="value(LOCATION)" )
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} \
         --region ${CLUSTER_LOCATION}
         
         export KUBE_CONFIG_PATH=~/.kube/config
         

  3. Update the `values.yaml`:

Open the `values.yaml` in a text editor and set the value to `ingress.domain` to a domain name under which you want MC to be accessible. You must have permissions to create domain name system (DNS) records for this domain name.

  4. Install the Helm chart using the following command:
         
         helm install mc-http-lb .
         

  5. Obtain the IP address of the External HTTP Load Balancer:

After the Load Balancer finishes provisioning (it may take up to five minutes), look up the external IP address of the Load Balancer using the following command:
         
         gcloud compute addresses list --filter="name~'.*mc-http-lb.*'" --format="value(address)" --global
         

  6. Create a DNS entry:

Create an A record for the domain you specified in Step 3. Consult your DNS host for details on how to create an A record.

**Note:** While in most cases DNS changes propagate in less than an hour, it may take up to 24 hours. Your application won't be accessible under the domain name until DNS propagation completes and the subsequent provisioning of an SSL certificate succeeds.
  7. Change the Base Domain Name in MC:

Use `mc-nginx` Service IP to access the MC administration console by navigating to `https://<IP>/admin-ui/settings/domain`, and change the Base Domain Name to the domain name you selected in the step earlier. You can obtain the Service IP address using the following command:
         
         kubectl get service/mc-nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}{"\n"}'
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
