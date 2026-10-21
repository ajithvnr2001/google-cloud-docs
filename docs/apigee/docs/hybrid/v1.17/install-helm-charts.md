---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts/
title: Step 11: Install Apigee hybrid Using Helm \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:03:41.780753+00:00
---

# Step 11: Install Apigee hybrid Using Helm  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 11: Install Apigee hybrid Using Helm Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-helm-charts.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-helm-charts.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-helm-charts.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-helm-charts.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-helm-charts.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-helm-charts.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-helm-charts.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-helm-charts.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-helm-charts.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-helm-charts.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-helm-charts.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-helm-charts.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-helm-charts.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-helm-charts.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-helm-charts.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-helm-charts.html)



## Install the Apigee hybrid runtime components

In this step, you will use Helm to install the following Apigee hybrid components: 

  * Apigee operator 
  * Apigee datastore 
  * Apigee telemetry 
  * Apigee Redis 
  * Apigee ingress manager 
  * Apigee organization 
  * Your Apigee environment(s) 



You will install the charts for each environment one at a time. The sequence in which you install the components matters. 

### Pre-installation Notes

  1. If you have not already installed Helm v3.14.2+, follow the instructions in [Installing Helm](https://helm.sh/docs/intro/install/).
  2. Apigee hybrid uses Helm guardrails to verify the configuration before installing or upgrading a chart. You may see guardrail-specific information in the output of each of the commands in this section, for example: 
         
         # Source: apigee-operator/templates/apigee-operators-guardrails.yaml
         apiVersion: v1
         kind: Pod
         metadata:
           name: apigee-hybrid-helm-guardrail-operator
           namespace:  APIGEE_NAMESPACE
           annotations:
             helm.sh/hook: pre-install,pre-upgrade
             helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
           labels:
             app: apigee-hybrid-helm-guardrail
         

If any of the `helm upgrade` commands fail, you can use the guardrails output to help diagnose the cause. See [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails). 

  3. Before executing any of the Helm upgrade/install commands, use the Helm dry-run feature by adding `--dry-run=server` at the end of the command. See `helm install --h` to list supported commands, options, and usage.



### Installation steps

Select the installation instructions for the service account authentication type in your hybrid installation:

### Kubernetes Secrets

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 
     1. Dry run: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify Apigee Operator installation:
            
            helm ls -n APIGEE_NAMESPACE
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                                       APP VERSION
            operator   apigee   3          2025-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.17.1   1.17.1
            

     4. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           34s
            

  3. Install Apigee datastore:

     1. Dry run: 
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify `apigeedatastore` is up and running by checking its state before proceeding to the next step:
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore default
            
            
            NAME      STATE       AGE
            default   running    51s
            

  4. Install Apigee telemetry:

     1. Dry run: 
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   55s
            

  5. Install Apigee Redis:

     1. Dry run:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   79s
            

  6. Install Apigee ingress manager:

     1. Dry run:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           16s
            

  7. Install Apigee organization. If you have set the $ORG_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective org:
            
            kubectl -n APIGEE_NAMESPACE get apigeeorg
            
            
            NAME                      STATE     AGE
            my-project-123abcd        running   4m18s
            

  8. Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml \
              --dry-run=server
            

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective env:
            
            kubectl -n APIGEE_NAMESPACE get apigeeenv
            
            
            NAME                       STATE     AGE   GATEWAYTYPE
            apigee-my-project-my-env   running   3m1s
            

  9. Install the environment groups (`virtualhosts`). 
     1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml
            

**Note:** ENV_GROUP must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
     3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2m
            
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                                        STATE     AGE
            apigee-ingressgateway-internal-chaining-my-project-123abcd   running   19m
            my-project-myenvgroup-000-321dcba                            running   2m30s
            




### JSON files

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 
     1. Dry run: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify Apigee Operator installation:
            
            helm ls -n APIGEE_NAMESPACE
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                                       APP VERSION
            operator   apigee   3          2025-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.17.1   1.17.1
            

     4. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           34s
            

  3. Install Apigee datastore:

     1. Dry run: 
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify `apigeedatastore` is up and running by checking its state before proceeding to the next step:
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore default
            
            
            NAME      STATE       AGE
            default   running    51s
            

  4. Install Apigee telemetry:

     1. Dry run: 
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   55s
            

  5. Install Apigee Redis:

     1. Dry run:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   79s
            

  6. Install Apigee ingress manager:

     1. Dry run:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           16s
            

  7. Install Apigee organization. If you have set the $ORG_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective org:
            
            kubectl -n APIGEE_NAMESPACE get apigeeorg
            
            
            NAME                      STATE     AGE
            my-project-123abcd        running   4m18s
            

  8. Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml \
              --dry-run=server
            

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective env:
            
            kubectl -n APIGEE_NAMESPACE get apigeeenv
            
            
            NAME                       STATE     AGE   GATEWAYTYPE
            apigee-my-project-my-env   running   3m1s
            

  9. Install the environment groups (`virtualhosts`). 
     1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml
            

**Note:** ENV_GROUP must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
     3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2m
            
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                                        STATE     AGE
            apigee-ingressgateway-internal-chaining-my-project-123abcd   running   19m
            my-project-myenvgroup-000-321dcba                            running   2m30s
            




### Vault

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 
     1. Dry run: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify Apigee Operator installation:
            
            helm ls -n APIGEE_NAMESPACE
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                                       APP VERSION
            operator   apigee   3          2025-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.17.1   1.17.1
            

     4. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           34s
            

  3. Install Apigee datastore:

     1. Dry run: 
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify `apigeedatastore` is up and running by checking its state before proceeding to the next step:
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore default
            
            
            NAME      STATE       AGE
            default   running    51s
            

  4. Install Apigee telemetry:

     1. Dry run: 
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   55s
            

  5. Install Apigee Redis:

     1. Dry run:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   79s
            

  6. Install Apigee ingress manager:

     1. Dry run:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           16s
            

  7. Install Apigee organization. If you have set the $ORG_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective org:
            
            kubectl -n APIGEE_NAMESPACE get apigeeorg
            
            
            NAME                      STATE     AGE
            my-project-123abcd        running   4m18s
            

  8. Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml \
              --dry-run=server
            

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml
            

     3. Verify it is up and running by checking the state of the respective env:
            
            kubectl -n APIGEE_NAMESPACE get apigeeenv
            
            
            NAME                       STATE     AGE   GATEWAYTYPE
            apigee-my-project-my-env   running   3m1s
            

  9. Install the environment groups (`virtualhosts`). 
     1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml
            

**Note:** ENV_GROUP must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
     3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2m
            
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                                        STATE     AGE
            apigee-ingressgateway-internal-chaining-my-project-123abcd   running   19m
            my-project-myenvgroup-000-321dcba                            running   2m30s
            




### WIF for GKE

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 
     1. Dry run: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify Apigee Operator installation:
            
            helm ls -n APIGEE_NAMESPACE
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                                       APP VERSION
            operator   apigee   3          2025-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.17.1   1.17.1
            

     4. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           34s
            

  3. Install Apigee datastore:

     1. Dry run: 
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Set up the service account bindings for Cassandra for Workload Identity Federation for GKE:

The output from the `helm upgrade` command should have contained commands in the **NOTES** section. Follow those commands to set up the service account bindings. There should be two commands in the form of:

### Production
            
            gcloud iam service-accounts add-iam-policy-binding CASSANDRA_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-cassandra-default]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-cassandra-default]" \
              --project PROJECT_ID
            

And:

### Production
            
            kubectl annotate serviceaccount apigee-cassandra-default \
              iam.gke.io/gcp-service-account=CASSANDRA_SERVICE_ACCOUNT_EMAIL \
              --namespace APIGEE_NAMESPACE
            

### Non-prod
            
            kubectl annotate serviceaccount apigee-cassandra-default \
              iam.gke.io/gcp-service-account=NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --namespace APIGEE_NAMESPACE
            

For example:

### Production
            
            NOTES:
            For Cassandra backup GKE Workload Identity, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
              gcloud iam service-accounts add-iam-policy-binding apigee-cassandra@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-cassandra-default]" \
                    --project my-project
            
              kubectl annotate serviceaccount apigee-cassandra-default \
                    iam.gke.io/gcp-service-account=apigee-cassandra@my-project.iam.gserviceaccount.com \
                    --namespace apigee
            

### Non-prod
            
            NOTES:
            For Cassandra backup GKE Workload Identity, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-cassandra-default]" \
                    --project my-project
            
              kubectl annotate serviceaccount apigee-cassandra-default \
                    iam.gke.io/gcp-service-account=apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --namespace apigee
            

**Optional:** If you do not want to set up Cassandra backup at this time, edit your overrides file to remove or comment out the `cassandra.backup` stanza before running the `helm upgrade` command without the `--dry-run` flag. See [Cassandra backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview) for more information about configuring Cassandra backup.

     3. Install the chart:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     4. Verify `apigeedatastore` is up and running by checking its state before proceeding to the next step:
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore default
            
            
            NAME      STATE       AGE
            default   running    51s
            

  4. Install Apigee telemetry:

     1. Dry run: 
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Set up the service account bindings for Loggeer and Metrics for Workload Identity Federation for GKE:

The output from the `helm upgrade` command should have contained commands in the **NOTES** section. Follow those commands to set up the service account bindings. There should be two commands in the form of:

**Logger KSA:** `apigee-logger-apigee-telemetry`
            
            gcloud iam service-accounts add-iam-policy-binding LOGGER_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-logger-apigee-telemetry]" \
              --project PROJECT_ID
            

**Metrics KSA:** `apigee-metrics-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding METRICS_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-metrics-sa]" \
              --project PROJECT_ID

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-metrics-sa]" \
              --project PROJECT_ID

For example:

### Production
            
            NOTES:
            For GKE Workload Identity, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
              Logger KSA: apigee-logger-apigee-telemetry
              gcloud iam service-accounts add-iam-policy-binding apigee-logger@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-logger-apigee-telemetry]" \
                    --project my-project
            
              Metrics KSA: apigee-metrics-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-metrics@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-metrics-sa]" \
                    --project my-project
            

### Non-prod
            
            NOTES:
            For GKE Workload Identity, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
              Logger KSA: apigee-logger-apigee-telemetry
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-logger-apigee-telemetry]" \
                    --project my-project
            
              Metrics KSA: apigee-metrics-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-metrics-sa]" \
                    --project my-project
            

     3. Install the chart:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     4. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   55s
            

  5. Install Apigee Redis:

     1. Dry run:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade redis apigee-redis/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeeredis default
            
            
            NAME      STATE     AGE
            default   running   79s
            

  6. Install Apigee ingress manager:

     1. Dry run:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade ingress-manager apigee-ingress-manager/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
            
            
            NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-ingressgateway-manager   2/2     2            2           16s
            

  7. Install Apigee organization. If you have set the $ORG_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Set up the service account bindings for org-scoped components for Workload Identity Federation for GKE, MART, Apigee Connect, UDCA, and Watcher.

The output from the `helm upgrade` command should have contained commands in the **NOTES** section. Follow those commands to set up the service account bindings. There should be four commands.

**Note:** The KSA names include a unique hash id for your organization, for example, `apigee-mart-my-project-_123abcd_ -sa`.

**MART KSA:** `apigee-mart-PROJECT_ID-ORG_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding MART_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-mart-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-mart-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

**Connect Agent KSA:** `apigee-connect-agent-PROJECT_ID-ORG_HASH_ID-sa`

**Note:** Apigee Connect uses the MART Google service account.

### Production
            
            gcloud iam service-accounts add-iam-policy-binding MART_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-connect-agent-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-connect-agent-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

**Mint Task Scheduler KSA:** (If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid)) `apigee-mint-task-scheduler-PROJECT_ID-ORG_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding MINT_TASK_SCHEDULER_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-mint-task-scheduler-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-mint-task-scheduler-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

**UDCA KSA:** `apigee-udca-PROJECT_ID-ORG_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding UDCA_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-udca-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-udca-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

**Watcher KSA:** `apigee-watcher-PROJECT_ID-ORG_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding WATCHER_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-watcher-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-watcher-PROJECT_ID-ORG_HASH_ID-sa]" \
              --project PROJECT_ID
            

For example:

### Production
            
            NOTES:
            For Apigee Organization GKE Workload Identity, my-project, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
            
            
              MART KSA: apigee-mart-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-mart@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-mart-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              Connect Agent KSA: apigee-connect-agent-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-mart@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-connect-agent-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              Mint task scheduler KSA: apigee-mint-task-scheduler-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-mint-task-scheduler@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-mint-task-scheduler-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              UDCA KSA: apigee-udca-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-udca@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-udca-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              Watcher KSA: apigee-watcher-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-watcher@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-watcher-my-project-1a2b3c4-sa]" \
                    --project my-project
            

### Non-prod
            
            NOTES:
            For Apigee Organization GKE Workload Identity, my-project, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
            
              MART KSA: apigee-mart-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-mart-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              Connect Agent KSA: apigee-connect-agent-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-connect-agent-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              UDCA KSA: apigee-udca-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-udca-my-project-1a2b3c4-sa]" \
                    --project my-project
            
            
              Watcher KSA: apigee-watcher-my-project-1a2b3c4-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-non-prod@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-watcher-my-project-1a2b3c4-sa]" \
                    --project my-project
            

     3. Install the chart:
            
            helm upgrade $ORG_NAME apigee-org/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     4. Verify it is up and running by checking the state of the respective org:
            
            kubectl -n APIGEE_NAMESPACE get apigeeorg
            
            
            NAME                      STATE     AGE
            my-project-123abcd        running   4m18s
            

  8. Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

     1. Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml \
              --dry-run=server
            

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Set up the service account bindings for env-scoped components for Workload Identity Federation for GKE, Runtime, Synchronizer, and UDCA.

The output from the `helm upgrade` command should have contained commands in the **NOTES** section. Follow those commands to set up the service account bindings. There should be four commands.

**Note:** The KSA names include a unique hash id for your environment, for example, `apigee-mart-my-project--myenv-abc1234-sa`.

**Runtime KSA:** `apigee-runtime-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding RUNTIME_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-runtime-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-runtime-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

**Synchronizer KSA:** `apigee-synchronizer-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding SYNCHRONIZER_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-synchronizer-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-synchronizer-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

**UDCA KSA:** `apigee-udca-PROJECT_ID-ORG_HASH_ID-ENV_NAME-ENV_HASH_ID-sa`

### Production
            
            gcloud iam service-accounts add-iam-policy-binding UDCA_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-udca-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

### Non-prod
            
            gcloud iam service-accounts add-iam-policy-binding NON_PROD_SERVICE_ACCOUNT_EMAIL \
              --role roles/iam.workloadIdentityUser \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[apigee/apigee-udca-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa]" \
              --project PROJECT_ID
            

For example:
            
            NOTES:
            For Apigee Environment GKE Workload Identity, my-env, please make sure to add the following membership to the IAM policy binding using the respective kubernetes SA (KSA).
            
            
              Runtime KSA: apigee-runtime-my-project-my-env-b2c3d4e-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-runtime@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-runtime-my-project-my-env-b2c3d4e-sa]" \
                    --project my-project
            
            
              Synchronizer KSA: apigee-synchronizer-my-project-my-env-b2c3d4e-sa
              gcloud iam service-accounts add-iam-policy-binding apigee-synchronizer@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-synchronizer-my-project-my-env-b2c3d4e-sa]" \
                    --project my-project
            
            
              UDCA KSA: apigee-udca-my-project-my-env-b2c3d4e-sa:
              gcloud iam service-accounts add-iam-policy-binding apigee-udca@my-project.iam.gserviceaccount.com \
                    --role roles/iam.workloadIdentityUser \
                    --member "serviceAccount:my-project.svc.id.goog[apigee/apigee-udca-my-project-my-env-b2c3d4e-sa]" \
                    --project my-project
            

     3. Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=$ENV_NAME \
              -f overrides.yaml
            

     4. Verify it is up and running by checking the state of the respective env:
            
            kubectl -n APIGEE_NAMESPACE get apigeeenv
            
            
            NAME                       STATE     AGE   GATEWAYTYPE
            apigee-my-project-my-env   running   3m1s
            

  9. Install the environment groups (`virtualhosts`). 
     1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml \
              --dry-run=server
            

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

     2. Install the chart:
            
            helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set envgroup=$ENV_GROUP \
              -f overrides.yaml
            

**Note:** ENV_GROUP must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
     3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
            
            kubectl -n APIGEE_NAMESPACE get arc
            
            
            NAME                                STATE   AGE
            apigee-org1-dev-egroup                       2m
            
            
            kubectl -n APIGEE_NAMESPACE get ar
            
            
            NAME                                                        STATE     AGE
            apigee-ingressgateway-internal-chaining-my-project-123abcd   running   19m
            my-project-myenvgroup-000-321dcba                            running   2m30s
            

  10. (Optional) You can see the status of your Kubernetes service accounts in the **Kubernetes: Workloads Overview** page in the Google Cloud console. 

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

**Note:** You may see an error status for the `apigee-cassandra-backup` service account. This is because you are not currently running backup or restore, and these processes have not been fully configured yet. For more information on Cassandra backup and restore, see [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview).



### WIF on other platforms

  1. If you have not, navigate into your `APIGEE_HELM_CHARTS_HOME` directory. Run the following commands from that directory.
  2. Install Apigee Operator/Controller: **Note:** This step requires elevated cluster permissions. Run `helm -h` or `helm install -h` for details 
     1. Dry run: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart: 
            
            helm upgrade operator apigee-operator/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify Apigee Operator installation:
            
            helm ls -n APIGEE_NAMESPACE
            
            
            NAME       NAMESPACE       REVISION   UPDATED                                STATUS     CHART                                       APP VERSION
            operator   apigee   3          2025-06-26 00:42:44.492009 -0800 PST   deployed   apigee-operator-1.17.1   1.17.1
            

     4. Verify it is up and running by checking its availability:
            
            kubectl -n APIGEE_NAMESPACE get deploy apigee-controller-manager
            
            
            NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
            apigee-controller-manager   1/1     1            1           34s
            

  3. Install Apigee datastore:

     1. Dry run: 
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade datastore apigee-datastore/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. If you have enabled Cassandra backup or Cassandra restore, grant the Cassandra Kubernetes service accounts access to impersonate the associated `apigee-cassandra`IAM service account. 
        1. List the email addresses of the IAM service account for Cassandra: 

### Production
               
               gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-cassandra"

### Non-prod
               
               gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-non-prod"

The output should look similar to the following:

### Production
               
               apigee-cassandra      apigee-cassandra@my-project.iam.gserviceaccount.com      False
                                 

### Non-prod
               
               apigee-non-prod       apigee-non-prod@my-project.iam.gserviceaccount.com      False
                                 

        2. List the Cassandra Kubernetes service accounts: 
               
               kubectl get serviceaccount -n APIGEE_NAMESPACE | grep "apigee-cassandra"

The output should look similar to the following:
               
               **apigee-cassandra-backup-sa                       0   7m37s**
               apigee-cassandra-default                         0   7m12s
               apigee-cassandra-guardrails-sa                   0   6m43s
               **apigee-cassandra-restore-sa                      0   7m37s**
               apigee-cassandra-schema-setup-my-project-1a2b2c4 0   7m30s
               apigee-cassandra-schema-val-my-project-1a2b2c4   0   7m29s
               apigee-cassandra-user-setup-my-project-1a2b2c4   0   7m22s
                             

        3. If you have created the `apigee-cassandra-backup-sa` or `apigee-cassandra-restore-sa` Kubernetes service accounts, grant each of them access to impersonate the `apigee-cassandra` IAM service account with the following command: 

### Production

### Template
               
               gcloud iam service-accounts add-iam-policy-binding \
                 CASSANDRA_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-cassandra@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-cassandra-backup-sa" \
                   --role=roles/iam.workloadIdentityUser

### Non-prod

### Template
               
               gcloud iam service-accounts add-iam-policy-binding \
                 NON_PROD_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-non-prod@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-cassandra-backup-sa" \
                   --role=roles/iam.workloadIdentityUser

Where:

           * `CASSANDRA_IAM_SA_EMAIL`: the email address of the Cassandra IAM service account.
           * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the project where you created the workload identity pool. **Note:** You must use the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in the member identifier. Using the project ID is not supported. You can find the project number with the following command: 
                 
                 gcloud projects describe PROJECT_ID --format="value(projectNumber)"

           * `POOL_ID`: the workload identity pool ID.
           * `MAPPED_SUBJECT`: the Kubernetes ServiceAccount from the claim in your ID token. In most hybrid installations, this will have the format: `system:serviceaccount:APIGEE_NAMESPACE:K8S_SA_NAME`. 
             * For `apigee-cassandra-backup-sa`, this will be something similar to `system:serviceaccount:apigee:apigee-cassandra-backup-sa`.
             * For `apigee-cassandra-restore-sa`, this will be something similar to `system:serviceaccount:apigee:apigee-cassandra-restore-sa`.
**Tip:** In the step [Add the cluster as a workload identity pool provider](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-sa-authentication#add-pool-provider) in **Step 5: Set up service account authentication** , you mapped `google.subject=assertions.sub`. Therefore the value of `MAPPED_SUBJECT` will be the value in the ID token following `"sub": `. You can find the mapped subject for a Kubernetes service account by searching the ID token for `sub` followed by the name of the service account. 

For example: pipe the contents of the ID token through `grep -E 'sub.*_apigee-cassandra-backup-sa_ '`

     4. Verify `apigeedatastore` is up and running by checking its state before proceeding to the next step:
            
            kubectl -n APIGEE_NAMESPACE get apigeedatastore default
            
            
            NAME      STATE       AGE
            default   running    51s
            

  4. Install Apigee telemetry:

     1. Dry run: 
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml \
              --dry-run=server
            

     2. Install the chart:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              -f overrides.yaml
            

     3. Verify it is up and running by checking its state:
            
            kubectl -n APIGEE_NAMESPACE get apigeetelemetry apigee-telemetry
            
            
            NAME               STATE     AGE
            apigee-telemetry   running   55s
            

     4. Grant the telemetry Kubernetes service accounts access to impersonate the associated `apigee-metrics`IAM service account. 
        1. List the email address of the IAM service account for metrics: 

### Production
               
               gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-metrics"

The output should look similar to the following:
               
               apigee-metrics   apigee-metrics@my-project.iam.gserviceaccount.com   False

### Non-prod
               
               gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-non-prod"

The output should look similar to the following:
               
               apigee-non-prod   apigee-non-prod@my-project.iam.gserviceaccount.com   False

        2. List the telemetry Kubernetes service accounts: 
               
               kubectl get serviceaccount -n APIGEE_NAMESPACE | grep "telemetry"

The output should look similar to the following:
               
               **apigee-metrics-apigee-telemetry                    0   42m**
               **apigee-open-telemetry-collector-apigee-telemetry   0   37m**

        3. Grant each of the telemetry Kubernetes service accounts access to impersonate the `apigee-metrics` IAM service account with the following command: 

### Production

**Apigee Metrics KSA:** `apigee-metrics-apigee-telemetry` to `apigee-metrics` Google IAM service account

### Code
               
               gcloud iam service-accounts add-iam-policy-binding \
                 METRICS_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-metrics@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-metrics-apigee-telemetry" \
                   --role=roles/iam.workloadIdentityUser

**Apigee OpenTelemetry Collector KSA:** `apigee-open-telemetry-collector-apigee-telemetry` to `apigee-metrics` Google IAM service account

### Code
               
               gcloud iam service-accounts add-iam-policy-binding \
                 METRICS_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-metrics@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-open-telemetry-collector-apigee-telemetry" \
                   --role=roles/iam.workloadIdentityUser

### Non-prod

**Apigee Metrics KSA:** `apigee-metrics-apigee-telemetry` to `apigee-non-prod` Google IAM service account

### Code
               
               gcloud iam service-accounts add-iam-policy-binding \
                 NON_PROD_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-non-prod@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-metrics-apigee-telemetry" \
                   --role=roles/iam.workloadIdentityUser

**Apigee OpenTelemetry Collector KSA:** `apigee-open-telemetry-collector-apigee-telemetry` to `apigee-non-prod` Google IAM service account

### Code
               
               gcloud iam service-accounts add-iam-policy-binding \
                 NON_PROD_IAM_SA_EMAIL \
                   --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                   --role=roles/iam.workloadIdentityUser

### Example
               
               gcloud iam service-accounts add-iam-policy-binding \
                 apigee-non-prod@my-project.iam.gserviceaccount.com \
                   --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-open-telemetry-collector-apigee-telemetry" \
                   --role=roles/iam.workloadIdentityUser



* Install Apigee Redis:

  1. Dry run:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml \
           --dry-run=server
         

  2. Install the chart:
         
         helm upgrade redis apigee-redis/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

  3. Verify it is up and running by checking its state:
         
         kubectl -n APIGEE_NAMESPACE get apigeeredis default
         
         
         NAME      STATE     AGE
         default   running   79s
         



* Install Apigee ingress manager:

  1. Dry run:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml \
           --dry-run=server
         

  2. Install the chart:
         
         helm upgrade ingress-manager apigee-ingress-manager/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

  3. Verify it is up and running by checking its availability:
         
         kubectl -n APIGEE_NAMESPACE get deployment apigee-ingressgateway-manager
         
         
         NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
         apigee-ingressgateway-manager   2/2     2            2           16s
         



* Install Apigee organization. If you have set the $ORG_NAME environment variable in your shell, you can use that in the following commands:

  1. Dry run:
         
         helm upgrade $ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml \
           --dry-run=server
         

  2. Install the chart:
         
         helm upgrade $ORG_NAME apigee-org/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         

  3. Verify it is up and running by checking the state of the respective org:
         
         kubectl -n APIGEE_NAMESPACE get apigeeorg
         
         
         NAME                      STATE     AGE
         my-project-123abcd        running   4m18s
         

  4. Grant the org-scoped Kubernetes service accounts access to impersonate the associated IAM service accounts. 
     1. List the email addresses of the IAM service accounts used by the `apigee-mart`, `apigee-udca`, and `apigee-watcher` components: 

### Production
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-mart\|apigee-udca\|apigee-watcher"

The output should look similar to the following:
            
            apigee-mart      apigee-mart@my-project.iam.gserviceaccount.com      False
            apigee-udca      apigee-udca@my-project.iam.gserviceaccount.com      False
            apigee-watcher   apigee-watcher@my-project.iam.gserviceaccount.com   False
            

If you are using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid), also get the email address of the `apigee-mint-task-scheduler` service account.
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-mint-task-scheduler"

The output should look similar to the following:
            
            apigee-mint-task-scheduler   apigee-mint-task-scheduler@my-project.iam.gserviceaccount.com   False
            

### Non-prod
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-non-prod"

The output should look similar to the following:
            
            apigee-non-prod     apigee-non-prod@my-project.iam.gserviceaccount.com         False
                              

     2. List the org-scoped Kubernetes service accounts: 
            
            kubectl get serviceaccount -n APIGEE_NAMESPACE | grep "apigee-connect-agent\|apigee-mart\|apigee-udca\|apigee-watcher"

The output should look similar to the following:
            
            apigee-connect-agent-my-project-123abcd         0   1h4m
            apigee-mart-my-project-123abcd                  0   1h4m
            apigee-mint-task-scheduler-my-project-123abcd   0   1h3m
            apigee-udca-my-project-123abcd                  0   1h2m
            apigee-watcher-my-project-123abcd               0   1h1m
                          

     3. Use the following commands to grant the org-scoped Kubernetes service accounts access to impersonate the associated IAM service accounts as follows: 

### Production

**Connect agent KSA:** `apigee-connect-agent-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-mart` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              APIGEE_MART_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-mart@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-connect-agent-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**MART KSA:** `apigee-mart-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-mart` IAM service account. MART and Connect agent use the same IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              APIGEE_MART_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-mart@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-mart-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Mint task scheduler KSA:** (if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid))

`apigee-mint-task-scheduler-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-mint-task-scheduler` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              APIGEE_MINT_TASK_SCHEDULER_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-mint-task-scheduler@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-mint-task-scheduler-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Org-scoped UDCA KSA:** `apigee-udca-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-udca` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              APIGEE_UDCA_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-udca-task-scheduler@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-udca-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Watcher KSA:** `apigee-watcher-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-watcher` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              APIGEE_WATCHER_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-watcher@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-watcher-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

### Non-prod

**Connect agent KSA:** `apigee-connect-agent-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-non-prod` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-connect-agent-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**MART KSA:** `apigee-mart-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-non-prod` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-mart-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Mint task scheduler KSA:** (if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/monetization-for-hybrid))

`apigee-mint-task-scheduler-ORG_NAME-UUIORG_HASH_IDD` Kubernetes service account to `apigee-non-prod` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-mint-task-scheduler-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Org-scoped UDCA KSA:** `apigee-udca-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-non-prod` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-udca-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser

**Watcher KSA:** `apigee-watcher-ORG_NAME-ORG_HASH_ID` Kubernetes service account to `apigee-non-prod` IAM service account.

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-watcher-my-org-123abcd" \
                --role=roles/iam.workloadIdentityUser



* Install the environment.

You must install one environment at a time. Specify the environment with `--set env=`ENV_NAME. If you have set the $ENV_NAME environment variable in your shell, you can use that in the following commands:

  1. Dry run:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml \
           --dry-run=server
         

ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_NAME`. However, if your environment has the same name as your environment group, you must use different release names for the environment and environment group, for example `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

  2. Install the chart:
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set env=$ENV_NAME \
           -f overrides.yaml
         

  3. Verify it is up and running by checking the state of the respective env:
         
         kubectl -n APIGEE_NAMESPACE get apigeeenv
         
         
         NAME                       STATE     AGE   GATEWAYTYPE
         apigee-my-project-my-env   running   3m1s
         

  4. Grant the environment-scoped Kubernetes service accounts access to impersonate the associated IAM service accounts. 
     1. List the email address of the IAM service accounts used by the `apigee-runtime`, `apigee-synchronizer`, and `apigee-udca` components: 

### Production
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-runtime\|apigee-synchronizer\|apigee-udca"

### Non-prod
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-non-prod"
            
            gcloud iam service-accounts list --project PROJECT_ID | grep "apigee-mart\|apigee-udca\|apigee-watcher"

The output should look similar to the following:

### Production
            
            apigee-runtime         apigee-runtime@my-project.iam.gserviceaccount.com         False
            apigee-synchronizer    apigee-synchronizer@my-project.iam.gserviceaccount.com      False
            apigee-udca            apigee-udca@my-project.iam.gserviceaccount.com         False
                              

### Non-prod
            
            apigee-non-prod     apigee-non-prod@my-project.iam.gserviceaccount.com         False
                              

     2. List the environment-scoped Kubernetes service accounts: 
            
            kubectl get serviceaccount -n APIGEE_NAMESPACE | grep "apigee-runtime\|apigee-synchronizer\|apigee-udca"

The output should look similar to the following:
            
            apigee-runtime-my-project--my-env-cdef123          0   19m
            apigee-synchronizer-my-project-my-env-cdef123      0   17m
            apigee-udca-my-project-123abcd                     0   1h29m
            apigee-udca-my-project-my-env-cdef123              0   22m
                          

**Note:** You may see both org-scoped and environment-scoped `apigee-udca` Kubernetes service accounts. In this step, grant access to the environment-scoped `apigee-udca` service account.
     3. Use the following command to grant the environment-scoped Kubernetes service accounts access to impersonate the associated IAM service accounts as follows: 

### Production

**Runtime KSA:** `apigee-runtime-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-runtime` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              RUNTIME_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-runtime@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-runtime-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser

**Synchronizer KSA:** `apigee-synchronizer-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-synchronizer` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              SYNCHRONIZER_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-synchronizer@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-synchronizer-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser

**UDCA KSA:** `apigee-udca-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-udca` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              UDCA_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-udca@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-udca-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser

### Non-prod

**Runtime KSA:** `apigee-runtime-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-non-prod` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-runtime-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser

### Non-prod

**Synchronizer KSA:** `apigee-synchronizer-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-non-prod` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-synchronizer-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser

### Non-prod

**UDCA KSA:** `apigee-udca-PROJECT_ID-ENV_NAME-ENV_HASH_ID-sa` KSA to `apigee-non-prod` Google IAM SA

### Code
            
            gcloud iam service-accounts add-iam-policy-binding \
              NON_PROD_IAM_SA_EMAIL \
                --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/MAPPED_SUBJECT" \
                --role=roles/iam.workloadIdentityUser

### Example
            
            gcloud iam service-accounts add-iam-policy-binding \
              apigee-non-prod@my-project.iam.gserviceaccount.com \
                --member="principal://iam.googleapis.com/projects/1234567890/locations/global/workloadIdentityPools/my-pool/subject/system:serviceaccount:apigee:apigee-udca-my-project-my-env-cdef123" \
                --role=roles/iam.workloadIdentityUser



* Install the environment groups (`virtualhosts`). 

  1. You must install one environment group (virtualhost) at a time. Specify the environment group with `--set envgroup=`ENV_GROUP. If you have set the $ENV_GROUP environment variable in your shell, you can use that in the following commands. Repeat the following commands for each env group mentioned in your `overrides.yaml` file: 

Dry run:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set envgroup=$ENV_GROUP \
           -f overrides.yaml \
           --dry-run=server
         

ENV_GROUP_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-virtualhosts` chart. This name must be unique from the other Helm release names in your installation. Usually this is the same as `ENV_GROUP`. However, if your environment group has the same name as an environment in your installation, you must use different release names for the environment group and environment, for example `dev-envgroup-release` and `dev-env-release`. For more information on releases in Helm, see [ Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.

  2. Install the chart:
         
         helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           --set envgroup=$ENV_GROUP \
           -f overrides.yaml
         

**Note:** ENV_GROUP must be unique within the `apigee` namespace. For example, if you have a `prod` env and envgroup, you should set this name to `prod-envgroup`. The later env group name should still be `prod`.
  3. Check the state of the ApigeeRoute (AR). 

Installing the `virtualhosts` creates ApigeeRouteConfig (ARC) which internally creates ApigeeRoute (AR) once the Apigee watcher pulls env group related details from the control plane. Therefore, check that the corresponding AR's state is running: 
         
         kubectl -n APIGEE_NAMESPACE get arc
         
         
         NAME                                STATE   AGE
         apigee-org1-dev-egroup                       2m
         
         
         kubectl -n APIGEE_NAMESPACE get ar
         
         
         NAME                                                        STATE     AGE
         apigee-ingressgateway-internal-chaining-my-project-123abcd   running   19m
         my-project-myenvgroup-000-321dcba                            running   2m30s
         



**Congratulations!**

You've successfully installed and configured the Apigee hybrid runtime plane.

## Next step

In the next step, you will configure the Apigee ingress gateway and deploy a proxy to test your installation.

[(NEXT) Step 1: Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-expose-apigee-ingress) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
