---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-helm-charts/
title: Step 11: Install Apigee hybrid Using Helm charts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:46:40.335573+00:00
---

# Step 11: Install Apigee hybrid Using Helm charts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-helm-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 11: Install Apigee hybrid Using Helm charts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-install-helm-charts.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-install-helm-charts.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/helm-install-helm-charts.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-install-helm-charts.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/helm-install-helm-charts.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-install-helm-charts.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-helm-charts.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/helm-install-helm-charts.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/helm-install-helm-charts.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/helm-install-helm-charts.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/helm-install-helm-charts.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/helm-install-helm-charts.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/helm-install-helm-charts.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/helm-install-helm-charts.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/helm-install-helm-charts.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/helm-install-helm-charts.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/helm-install-helm-charts.html)



## Install the Apigee hybrid Helm charts

In this step, you will use Helm to install the following Apigee hybrid components: 

  * Apigee operator 
  * Apigee datastore 
  * Apigee telemetry 
  * Apigee Redis 
  * Apigee ingress manager 
  * Apigee organization 
  * Your Apigee environment(s) 



You will install the charts for each environment one at a time. The sequence in which you install the components matters. 

**Note:** Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run` at the end of the command. See `helm install --h` to list supported commands, options, and usage. **Caution:** If you are installing the charts on a cluster you have migrated from `apigeectl` management to Helm management with the [Apigee Helm migration tool](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration), omit the `--atomic` flag from all of the following commands.

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 

Dry run:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade operator apigee-operator/ \
           --install \
           --create-namespace \
           --namespace apigee-system \
           --atomic \
           -f overrides.yaml
         

Verify Apigee Operator installation:
         
         helm ls -n apigee-system
         
         
         NAME           NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
         operator    apigee-system   3               2023-06-26 00:42:44.492009 -0800 PST    deployed        apigee-operator-1.11.2   1.11.2

Verify it is up and running by checking its availability:
         
         kubectl -n apigee-system get deploy apigee-controller-manager
         
         
         NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-controller-manager   1/1     1            1           7d20h

  3. Install Apigee datastore:

Dry run:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Verify `apigeedatastore` is up and running by checking its state before proceding to the next step:
         
         kubectl -n apigee get apigeedatastore default
         
         
         NAME      STATE       AGE
         default   running    2d

  4. Install Apigee telemetry:

Dry run:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade telemetry apigee-telemetry/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeetelemetry apigee-telemetry
         
         
         NAME               STATE     AGE
         apigee-telemetry   running   2d

  5. Install Apigee Redis:

Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Verify it is up and running by checking its state:
         
         kubectl -n apigee get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   2d

  6. Install Apigee ingress manager:

Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Verify it is up and running by checking its availability:
         
         kubectl -n apigee get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           2d

  7. Install Apigee organization:

Dry run:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml \
           --dry-run
         

Install the chart:
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f overrides.yaml
         

Verify it is up and running by checking the state of the respective org:
         
         kubectl -n apigee get apigeeorg
         
         
         NAME                      STATE     AGE
         apigee-org1-xxxxx          running   2d

  8. Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME:

Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f overrides.yaml \
           --dry-run
         

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts ](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

Install the chart:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f overrides.yaml
         

Verify it is up and running by checking the state of the respective env:
         
         kubectl -n apigee get apigeeenv
         
         
         NAME                          STATE       AGE   GATEWAYTYPE
         apigee-org1-dev-xxx            running     2d

  9. Install the environment groups (`virtualhosts`). 
     1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP_NAME. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace apigee \
              --atomic \
              --set envgroup=ENV_GROUP_NAME \
              -f overrides.yaml \
              --dry-run
            

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

Install the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace apigee \
              --atomic \
              --set envgroup=ENV_GROUP_NAME \
              -f overrides.yaml
            

**Note:** ENV_GROUP_NAME must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
     2. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n apigee get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2d
            
            kubectl -n apigee get ar
            
            
            NAME                                        STATE     AGE
            apigee-org1-dev-egroup-xxxxxx                running   2d


**Congratulations!**

You've successfully installed and configured the Apigee hybrid runtime plane.

## GKE with Workload Identity

If you are installing Apigee hybrid on GKE and you are configuring Workload Identity to authenticate service accounts, in the next step, you will configure the associations between the Kubernetes service accounts and the Google service accounts for your cluster.

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-check-cluster) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-helm-charts) [(NEXT) Step 12: Set up Workload Identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-workload-identity)

## All other installations

In the next step, you will configure the Apigee ingress gateway and deploy a proxy to test your installation.

[(NEXT) Step 1: Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-expose-apigee-ingress) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
