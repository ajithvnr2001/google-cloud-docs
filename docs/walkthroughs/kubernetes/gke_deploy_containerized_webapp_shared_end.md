---
url: https://docs.cloud.google.com/walkthroughs/kubernetes/gke_deploy_containerized_webapp_shared_end/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:45.717505+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/walkthroughs/kubernetes/gke_deploy_containerized_webapp_shared_end/




Stay organized with collections  Save and categorize content based on your preferences. 

### 🎉 Success

You have successfully deployed a containerized web application!

To learn about next steps, click **Next**.

## Next steps

### Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, delete your project if you're not going to use it again. If you intend to use it again, you can delete the individual resources.

#### Delete the project

To delete the Cloud project:
    
    
    gcloud projects delete ${PROJECT_ID}
    

#### Delete individual resources

  1. **Delete the Service** : This deallocates the Cloud Load Balancer created for your Service:
         
         kubectl delete service hello-app-service
         

  2. **Delete the cluster** : This deletes the resources that make up the cluster. Replace COMPUTE_ZONE in the command below with your own zone:
         
         gcloud container clusters delete hello-cluster --zone COMPUTE_ZONE
         

  3. **Delete your container images** : This deletes the Docker images you pushed to Artifact Registry. Replace PROJECT-ID with your own:
         
         gcloud artifacts docker images delete \
             ${REGION}-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v1 \
             --delete-tags --quiet
         gcloud artifacts docker images delete \
             ${REGION}-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v2 \
             --delete-tags --quiet
         




### Do more with Google Kubernetes Engine

  * [Learn about Pricing for GKE](https://cloud.google.com/kubernetes-engine/pricing).
  * [Use the Pricing Calculator to estimate costs](https://cloud.google.com/products/calculator).
  * [Read the Load Balancers tutorial, which demonstrates advanced load balancing configurations for web applications](https://cloud.google.com/kubernetes-engine/docs/tutorials/http-balancer).
  * [Configure a static IP and domain name for your application](https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip).
  * [Explore other Kubernetes Engine tutorials](https://cloud.google.com/kubernetes-engine/docs/tutorials).
  * [Try out other Google Cloud features for yourself. Have a look at our tutorials](https://cloud.google.com/docs/tutorials).




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
