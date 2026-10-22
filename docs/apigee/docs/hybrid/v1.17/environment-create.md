---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-create/
title: Create environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:24.352335+00:00
---

# Create environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create environments Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-create.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environment-create.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/environment-create.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/environment-create.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/environment-create.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/environment-create.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/environment-create.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/environment-create.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/environment-create.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/environment-create.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/environment-create.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/environment-create.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/environment-create.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/environment-create.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/environment-create.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/environment-create.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/environment-create.html)



This topic explains how to create new environments for Apigee hybrid. For an introduction, see [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview). 

## About environment creation

Environment creation includes the following tasks: 

  * Create the environment in the management plane using either the [Apigee UI](https://apigee.google.com) or the [Create environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create), and attach it to an environment group.
  * Add the environment to your overrides file and install the environment's runtime components in your cluster with the `apigee-env` Helm chart.



For the first environment of a new installation, these tasks are explained in [Step 3: Add an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment) and [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-copy-overrides#specify-configuration-overrides). To remove an environment, see [Delete environments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-delete). 

##  How to create an environment 

The following steps add a **prod** environment to an installation that already has a **test** environment.

  1. Create the environment in the management plane with the [Apigee UI](https://apigee.google.com) or the [Create environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create). For the detailed steps, see [Step 3: Add an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment). 
  2. Attach the environment to an environment group. Apigee routes API traffic to an environment only through an environment group. You can attach the environment to an existing environment group in the [Apigee UI](https://apigee.google.com), or with the [Environment group attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments) as follows: 
     1. On the command line, get your `gcloud` authentication credentials using the following command:

###  Linux / MacOS 
            
            TOKEN=$(gcloud auth print-access-token)

###  Windows 
            
            for /f "tokens=*" %a in ('gcloud auth print-access-token') do set TOKEN=%a

     2. Attach the environment to the environment group: 

### No data residency
            
            curl -X POST -H "Authorization: Bearer $TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"environment": "prod"}' \
              "https://apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments"

### Data residency
            
            curl -X POST -H "Authorization: Bearer $TOKEN" \
              -H "Content-Type: application/json" \
              -d '{"environment": "prod"}' \
              "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/ORG_NAME/envgroups/ENV_GROUP/attachments"

Where:

        * ORG_NAME is the name of your Apigee organization.
        * ENV_GROUP is the name of the environment group.
        * CONTROL_PLANE_LOCATION is the control plane location of your organization if you use [data residency](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/using-data-residency-with-apigee-hybrid).

The output is similar to the following:
    
    {
      "name": "organizations/ORG_NAME/operations/d4ce8118-6355-451e-bbe9-460e58d9d268",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "INSERT",
        "targetResourceName": "organizations/ORG_NAME/envgroups/ENV_GROUP/attachments/ca81c6ec-e49a-49cd-8f97-63b402deee76",
        "state": "FINISHED"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.EnvironmentGroupAttachment",
        "name": "ca81c6ec-e49a-49cd-8f97-63b402deee76",
        "environment": "prod"
      }
    }

**Note:** If you attach the environment to a new environment group, you must also add the environment group to `virtualhosts` in your overrides file and install the `apigee-virtualhost` chart for it. See [Step 3: Add an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment) and [Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/base-path-routing).
  3. Add a new environment definition to the `envs[]` property in your overrides file. The property is an array, so you can add more than one environment definition to it. Give the new environment the same name as the environment you created in the management plane. For example, the following configuration defines two environments, **test** and **prod** :
         
         namespace: my-namespace
         org: my-organization
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/PROJECT_ID-apigee-synchronizer.json"
               runtime: "your_keypath/PROJECT_ID-apigee-runtime.json"
         
           - name: prod
             serviceAccountPaths:
               synchronizer: "your_keypath/PROJECT_ID-apigee-synchronizer.json"
               runtime: "your_keypath/PROJECT_ID-apigee-runtime.json"
         ...

  4. Install the `apigee-env` chart for the new environment. You must install one environment at a time, specified with `--set env=`ENV_NAME.

     1. Dry run:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=ENV_NAME \
              -f OVERRIDES_FILE \
              --dry-run=server
            

Where:

        * ENV_RELEASE_NAME is a name used to keep track of installation and upgrades of the `apigee-env` chart. Helm release names must be unique within your Apigee hybrid installation. If your environment name is unique, this can be the same as ENV_NAME. However, if your environment and environment group have the same name, use a different Helm release name for each. For example, if both are named `dev`, you could use `dev-env-release` and `dev-envgroup-release`. For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation.
        * APIGEE_NAMESPACE is the namespace where you installed Apigee hybrid, `apigee` by default.
        * ENV_NAME is the name of the new environment.
        * OVERRIDES_FILE is the path to your overrides file.

If ENV_NAME doesn't match an entry in `envs[]`, the command fails with an error similar to `Environment 'prod' not found in the provided environments`.

     2. Install the chart:
            
            helm upgrade ENV_RELEASE_NAME apigee-env/ \
              --install \
              --namespace APIGEE_NAMESPACE \
              --atomic \
              --set env=ENV_NAME \
              -f OVERRIDES_FILE
            

For example, to install the **prod** environment:
            
            helm upgrade prod apigee-env/ --install --namespace apigee --atomic --set env=prod -f overrides.yaml
            Release "prod" does not exist. Installing it now.
            NAME: prod
            ...
            STATUS: deployed
            REVISION: 1

**Note:** Don't omit `--install`. Without it, the command fails for a new environment with `Error: UPGRADE FAILED: "ENV_RELEASE_NAME" has no deployed releases`. 

If you use Workload Identity, grant the new environment's Kubernetes service accounts access to the IAM service accounts. The environment-scoped Kubernetes service account names include a hash of the environment name, so the bindings that you created for other environments don't apply to the new environment. For Workload Identity on GKE, run the commands in the **NOTES** section of the `helm upgrade` output. For more information, see [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation).

     3. Verify that the environment is running:
            
            kubectl -n APIGEE_NAMESPACE get apigeeenv
            

The output is similar to the following:
            
            NAME                          STATE     AGE   GATEWAYTYPE
            apigee-my-org-prod-e8d4a16    running   3m
            apigee-my-org-test-f86941d    running   22d
            




For more information about virtual host configuration, see [Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/base-path-routing). For a complete list of environment configuration elements, see [envs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs) in the Configuration property reference. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
