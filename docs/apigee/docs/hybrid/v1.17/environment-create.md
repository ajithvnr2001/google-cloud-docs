---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/environment-create/
title: Create environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:05.624602+00:00
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

Environment creation is a two-step process:

  * Create an environment in the management plane using either the UI or an Apigee API.
  * Add configuration for that environment to your overrides file and apply it to the cluster.



The steps for adding an environment are described in adding and configuring an environment are explained in [Step 5: Add an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment) and [ Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-copy-overrides#specify-configuration-overrides). 

##  How to create an environment 

  1. Create one or more new environments in the [Apigee UI](https://apigee.google.com) or with the [Create environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create). For the basic steps, see [Step 5: Add an environment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-add-environment). 
  2. Add a new environment definition to the `envs[]` property in your overrides file. Note that the property is an array; therefore, you can add more than one environment definition to it. Give the new environment the same name as the environment you created in the UI. For example, the following configuration defines two environments: **test** and **prod** :
         
         namespace: my-namespace
         org: my-organization
         ...
         envs:
           - name: test
             serviceAccountPaths:
               synchronizer: "your_keypath/synchronizer-manager-service-account.json
               udca: "your_keypath/analytic-agent-service-account.json
         
           - name: prod
             serviceAccountPaths:
               synchronizer: "your_keypath/synchronizer-manager-service-account.json
               udca: "your_keypath/analytic-agent-service-account.json
         ...

  3. Apply any changes to the cluster. Apply the changes to each environment in sequence. 
         
         helm upgrade ENV_RELEASE_NAME apigee-env/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           -f OVERRIDES_FILE \
           --dry-run=server
         

ENV_RELEASE_NAME is a name used track installation and upgrades of the `apigee-env` chart. Helm release names must be unique within your Apigee hybrid installation. If you environment name is unique, this can be the same as `ENV_NAME`. However, if you have the same name for your environment and environment group, make sure to enter a unique Helm release name for each. For example, if both are named `dev` you could use something like `dev-env-release` and `dev-envgroup-release`. 

For more information on releases in Helm, see [Three big concepts](https://helm.sh/docs/intro/using_helm/#three-big-concepts) in the Helm documentation. 

The `test` environment:
         
         helm upgrade test-release apigee-env/ \
           --namespace apigee \
           --atomic \
           --set env=test \
           -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_test_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.

The `prod` environment:
         
         helm upgrade prod-release apigee-env/ \
           --namespace apigee \
           --set env=prod \
           --atomic \
           -f OVERRIDES_FILE.yaml
         




For more information about virtual host configuration see [Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/base-path-routing). For a complete list of environment configuration elements, see [envs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs) in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
