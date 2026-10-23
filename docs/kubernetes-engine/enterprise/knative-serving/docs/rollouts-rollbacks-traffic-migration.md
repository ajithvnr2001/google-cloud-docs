---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration/
title: Rollbacks, gradual rollouts, and traffic migration \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:31.528415+00:00
---

# Rollbacks, gradual rollouts, and traffic migration  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Rollbacks, gradual rollouts, and traffic migration Stay organized with collections  Save and categorize content based on your preferences. 

Knative serving allows you to specify which revisions should receive traffic and to specify traffic percentages that are received by a revision. This feature allows you to rollback to a previous revision, gradually roll out a revision (also known as blue-green deployment), and split traffic between multiple revisions. This page describes how to use this feature to manage traffic to your Knative serving revisions.

## Rolling back to a previous revision

To roll back to a previous revision:

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click the _Revisions_ tab to show the list of current revisions for that service.

  4. In the list of revisions, click the ellipsis icon to the right of the revision you are rolling back:

  5. Click **Manage Traffic** to display the manage traffic form:

     1. Select the previous revision you want to roll back to in the dropdown list.
     2. Set that previous revision's traffic percentage to 100.
     3. Set the currently serving revision's percentage to 0.
     4. Click **Save**.



### Command line

Use the following command:
    
    
    gcloud run services update-traffic SERVICE --to-revisions REVISION=100

  * Replace SERVICE with the name of the service.
  * Replace REVISION with the name of the revision you are rolling back to.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `traffic` attribute that is located under `spec`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         spec:
         ...
           traffic:
           - revisionName: REVISION
             percent: 100
         

Replace

     * REVISION with the name of the revision you are rolling back to.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




## Gradually rolling out a revision

To roll out a new revision gradually (blue-green deployment):

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click **Deploy New Revision**.

  4. Fill out the deploy form as needed, but make sure the checkbox labelled _Serve this revision immediately_ is UNCHECKED.

  5. Click **Deploy**.

  6. Click **Manage Traffic**.

  7. The new revision is listed but with a 0 percentage set: it is currently not serving any traffic. In the form:

     1. Set it to the desired percentage, for example, 5. Note that the currently serving version's percentage is automatically reduced by that same amount.
     2. Click **Save**.
     3. Repeat these _Manage Traffic_ steps but with changed percentages, increasing the percentage as needed for the new revision. You do not need to redeploy to change the traffic percentages.



### Command line

  1. To deploy the revision you want to roll out gradually, initially setting it to receive no traffic, you use the `update` command with `--no-traffic` parameter:
         
         gcloud run deploy --image IMAGE --no-traffic

Replace IMAGE with the image you are deploying.

  2. Specify the percentage of traffic you want the new revision to handle, for example, 5 percent:
         
         gcloud run services update-traffic SERVICE --to-revisions REVISION=PERCENTAGE

     * Replace SERVICE with the name of the service.
     * Replace REVISION with the name of the revision you are rolling out gradually. To specify the latest revision, you can use `LATEST`, for example, `LATEST=5`.
     * Replace PERCENTAGE with the percentage of traffic you want to send to the new revision, for example, `5` to send it 5% of traffic.
  3. After the revision's performance is satisfactory, repeat the preceding `update-traffic` step, but increase the percentage value as desired.




### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. Make any desired configuration changes to the service as described in the various [configuration pages](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits), and specify the revision name you want for the new revision:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         template:
           metadata:
             annotations:
               ...
             name: REVISION-NAME
          ```
         
         Replace
         

     * REVISION-NAME with the name you want the new revision to have.
  3. Below the `spec` attribute, locate and update the `traffic` attribute so that the new revision serves only a small amount of traffic:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         spec:
         ...
           traffic:
           - revisionName: REVISION-NEW
             percent: PERCENT-NEW
           - revisionName: REVISION-FORMER
             percent: PERCENT-FORMER
         

Note that the percentages must add up to 100. Replace

     * REVISION-NEW with the name of the revision you are rolling out gradually.
     * REVISION-FORMER with the name of the currently serving revision.
     * PERCENT-NEW with the traffic percentage you want to send to the new revision, for example use `10` to send 10% of the traffic to that revision.
     * PERCENT-FORMER with the traffic percentage you want to send to the old revision



## Splitting traffic between multiple revisions

To split traffic between two or more revisions:

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click **Manage Traffic**.

  4. The currently serving new revision is listed. In the form:

     1. Set the currently serving revision percentage to the desired split.
     2. Select one of the previous revisions using the dropdown list and set it to the desired percentage split.
     3. To split traffic between more revisions, click **Add Revision** , select the desired revision, and set the percentage to the desired split.
     4. Click **Save**.



### Command line

Specify the revisions and the percentage of traffic for each revision in a comma-delimited list:
    
    
    gcloud run services update-traffic SERVICE --to-revisions LIST

Replace:

  * SERVICE with the name of the service.
  * LIST with a comma-delimited list of revisions that you want to receive traffic and the corresponding percentage of traffic, totalling to 100 percent:  
REVISION1=PERCENTAGE1,REVISION2=PERCENTAGE2,REVISIONn=PERCENTAGEn  
for example, `hello2-00005-red=25,hello2-00001-bod=25,hello2-00002-nan=50`.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `traffic` attribute so that the new revision serves only a small amount of traffic:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         spec:
         ...
           traffic:
           - revisionName: REVISION-A
             percent: PERCENT-A
           - revisionName: REVISION-B
             percent: PERCENT-B
           - revisionName: REVISION-C
             percent: PERCENT-C
         

Note that percentages must add up to 100. Replace

     * REVISION-A, REVISION-B, REVISION-C with the revisions you are allotting traffic to.
     * PERCENT-A, PERCENT-B, PERCENT-C with the percentage for the corresponding revision.
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




## Sending all traffic to the latest revision

When you deploy a new revision, you can make this revision and all future ones serve 100% of the traffic as soon as possible, overriding any established traffic split:

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it.

  3. Click **Deploy New Revision**.

  4. Fill out the deploy form as needed, making sure you check the checkbox labelled _Serve this revision immediately_. This will override any existing traffic splitting, with the new revision serving 100 percent of traffic.

  5. Click **Deploy**.




### Command line

To send all traffic to the most recently deployed revision:
    
    
    gcloud run services update-traffic SERVICE --to-latest

Replace SERVICE with the name of the service.

### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. In your local file, update the `traffic` attribute that is located under `spec`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         spec:
         ...
           traffic:
           - latestRevision: true
             percent: 100
         

  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




## Using tags for testing, traffic migration and rollbacks

After you deploy a service, you can create a new revision and assign a tag that allows you to access the revision at a specific URL without serving traffic. You can then use that tag to gradually migrate traffic to the tagged revision, and to rollback a tagged revision.

A common use case for this feature is to use it for testing and vetting of a new service revision before it serves any traffic, in this typical sequence:

  1. Run integration tests on a container during development.
  2. Deploy the container to a Google Cloud project that you use only for staging, serving no traffic, and test against a tagged revision.
  3. Deploy it to production, without serving traffic, and test against a tagged revision in production.
  4. Migrate traffic to the tagged revision.



### Deploying a new tagged revision

To deploy a new revision of an existing service to production:
    
    
    gcloud run deploy myservice --image IMAGE_URL  --no-traffic --tag TAG_NAME

Replace:

  * IMAGE_URL with the URL for your image
  * TAG_NAME with your lower-case tag name



The tag allows you to directly test the new revision at a specific URL, without serving traffic. The [test URL](https://docs.cloud.google.com/anthos/run/docs/default-domain) starts with the tag name you provided: `http://{TAG_NAME}---{SERVICE_NAME}.{NAMESPACE}.kuberun.{EXTERNAL_IP}.nip.io`

For example if you used the tag name `green` on the service `myservice`, you would test the tagged revision at the URL: `https://green---myservice.default.kuberun.11.111.11.111.nip.io`

### Migrating traffic to a tagged revision

After confirming that the new revision works properly, you can start migrating traffic to it using the Google Cloud console, the gcloud command line, or a YAML file:

### Console

  1. Go to Knative serving in the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Locate the service in the services list, and click on it:

  3. Select the tagged revision you want to send traffic to:

  4. Click **Manage Traffic**.

  5. Locate the tagged revision name: it is listed but with a 0 percentage set: it is currently not serving any traffic. In the _Manage traffic_ * form:

     1. Set it to the desired percentage, for example, 5. Note that the currently serving version's percentage is automatically reduced by that same amount.
     2. Click **Save**.
     3. Over a period of hours or days, as needed, repeat these _Manage Traffic_ steps but with changed percentages, increasing the percentage as needed for the tagged revision. You do not need to redeploy to change the traffic percentages.



### Command line

To migrate traffic to a specific revision tag:
    
    
    gcloud run deploy update-traffic myservice --tag TAG_NAME=TRAFFIC_PERCENT

Replace

  * TAG_NAME with the name of the tag you are migrating traffic to
  * TRAFFIC_PERCENT with the percentage of traffic you want to the tagged revision to serve, for example, `1`.



### YAML

**Caution:** Deploying configuration changes using YAML files replaces the configuration of your existing services. Since a YAML file completely overwrites all configurations, you should avoid using multiple methods to modify your services. For example, do not use YAML files in conjunction with the Google Cloud console or `gcloud` commands.

You can download the configuration of an existing service into a YAML file with the `gcloud run services describe` command by using the [`--format=export`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/describe) flag. You can then modify that YAML file and deploy those changes with the `gcloud run services replace` command. You must ensure that you modify only the specified attributes.

  1. Download the configuration of your service into a file named `service.yaml` on local workspace:
         
         gcloud run services describe SERVICE --format export > service.yaml

Replace SERVICE with the name of your Knative serving service.

  2. Make any desired configuration changes to the service as described in the various [configuration pages](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/memory-limits).

  3. Below the `spec` attribute, locate and update the `traffic` attribute for the tagged revision so that the tagged revision serves only a small amount of traffic:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
          name: SERVICE
         spec:
         ...
           traffic:
           - revisionName: REVISION
             tag: TAG_NAME
             percent: PERCENT-NEW
           - revisionName: REVISION-FORMER
             percent: PERCENT-FORMER
         

Note that the percentages must add up to 100. Replace

     * REVISION with the name of the tagged revision.
     * TAG_NAME with the name of the tag you are rolling out gradually.
     * PERCENT-NEW with the traffic percentage you want to send to the tagged revision, for example use `10` to send 10% of the traffic to that revision.
     * REVISION-FORMER with the name of the currently serving revision.
     * PERCENT-FORMER with the traffic percentage you want to send to the old revision
  4. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
