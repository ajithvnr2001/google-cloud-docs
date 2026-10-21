---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-download-charts/
title: Step 2: Download the Apigee Helm charts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:30:58.193240+00:00
---

# Step 2: Download the Apigee Helm charts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-download-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Download the Apigee Helm charts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-install-download-charts.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-install-download-charts.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/helm-install-download-charts.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-install-download-charts.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/helm-install-download-charts.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-install-download-charts.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-download-charts.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/helm-install-download-charts.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/helm-install-download-charts.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/helm-install-download-charts.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/helm-install-download-charts.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/helm-install-download-charts.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/helm-install-download-charts.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/helm-install-download-charts.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/helm-install-download-charts.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/helm-install-download-charts.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/helm-install-download-charts.html)



This step explains how to download the Helm charts used to install and manage Apigee hybrid. Apigee hybrid charts are hosted in [Google Artifact Registry](https://docs.cloud.google.com/artifact-registry):

`oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts`

If you have not already installed Helm v3.10+, follow the instructions in [Installing Helm](https://helm.sh/docs/intro/install/). 

### Prepare the directory structure

These steps are optional but recommended. The procedures will refer to the `$APIGEE_HELM_CHARTS_HOME` environment variable for the directory where you download the Apigee Helm Charts.

  1. Create a base directory for your hybrid installation and within that a directory for the charts: 
         
         mkdir -p APIGEE_HYBRID_BASE/APIGEE_HELM_CHARTS_HOME

for example:
         
         mkdir -p apigee-hybrid/helm-charts

  2. Save the location of the Helm charts directory to an environmental variable for convenience: 
         
         cd APIGEE_HYBRID_BASE/APIGEE_HELM_CHARTS_HOME
         
         export APIGEE_HELM_CHARTS_HOME=$PWD




### Pull Apigee Helm charts

  1. In the `$APIGEE_HELM_CHARTS_HOME` directory, use the `pull` command to copy all of the Apigee hybrid Helm charts to your local storage: 
         
         export **CHART_REPO** =oci://us-docker.pkg.dev/apigee-release/apigee-hybrid-helm-charts
         export **CHART_VERSION** =1.11.2
         helm pull **$CHART_REPO** /apigee-operator --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-datastore --version **$CHART_VERSION** --untar
         helm pull **$CHART_REP** O/apigee-env --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-ingress-manager --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-org --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-redis --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-telemetry --version **$CHART_VERSION** --untar
         helm pull **$CHART_REPO** /apigee-virtualhost --version **$CHART_VERSION** --untar
         

  2. Optional: Verify that the charts expanded into the intended directory structure with the `tree` command. Your output should resemble the following. **Tip:** If your operating system does not have a `tree` command, you can try a recursive directory command (**UNIX/Linux:** `ls -R`, **Windows:** `dir /s /b`). 
         
         tree
         .
         ├── apigee-datastore
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── backup-cert.yaml
         │   │   ├── backup-cronjob.yaml
         │   │   ├── backup-gsa-secret.yaml
         │   │   ├── backup-key.yaml
         │   │   ├── backup-sa.yaml
         │   │   ├── datastore-secret.yaml
         │   │   ├── datastore.yaml
         │   │   ├── _helpers.tpl
         │   │   ├── NOTES.txt
         │   │   ├── restore-cert.yaml
         │   │   ├── restore-gsa-secret.yaml
         │   │   ├── restore-job.yaml
         │   │   ├── restore-key.yaml
         │   │   └── restore-sa.yaml
         │   └── values.yaml
         ├── apigee-env
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── encryption-keys-secret.yaml
         │   │   ├── environment.yaml
         │   │   ├── _helpers.tpl
         │   │   ├── NOTES.txt
         │   │   ├── runtime-gsa-secret.yaml
         │   │   ├── runtime-sa.yaml
         │   │   ├── synchronizer-gsa-secret.yaml
         │   │   ├── synchronizer-sa.yaml
         │   │   ├── udca-gsa-secret.yaml
         │   │   └── udca-sa.yaml
         │   └── values.yaml
         ├── apigee-ingress-manager
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── apigee-ca-issuer.yaml
         │   │   ├── apigee-istiod-certificate.yaml
         │   │   ├── _helpers.tpl
         │   │   ├── ingress-service-account.yaml
         │   │   ├── istio-config.yaml
         │   │   ├── istiod-deployment-with-apigee-controller.yaml
         │   │   ├── istiod-envoyfilters.yaml
         │   │   ├── istiod-hpa.yaml
         │   │   ├── istiod-service-account.yaml
         │   │   └── istiod-svc.yaml
         │   └── values.yaml
         ├── apigee-operator
         │   ├── Chart.yaml
         │   ├── etc
         │   │   ├── crds
         │   │   │   ├── crd
         │   │   │   │   ├── bases
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeedatastores.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeedeployments.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeeenvironments.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeeissues.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeeorganizations.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeeredis.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeerouteconfigs.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeeroutes.yaml
         │   │   │   │   │   ├── apigee.cloud.google.com_apigeetelemetries.yaml
         │   │   │   │   │   └── apigee.cloud.google.com_cassandradatareplications.yaml
         │   │   │   │   ├── kustomization.yaml
         │   │   │   │   ├── kustomizeconfig.yaml
         │   │   │   │   └── patches
         │   │   │   │       ├── cainjection_in_apigeedatastores.yaml
         │   │   │   │       ├── cainjection_in_apigeedeployments.yaml
         │   │   │   │       ├── cainjection_in_apigeeenvironments.yaml
         │   │   │   │       ├── cainjection_in_apigeeissues.yaml
         │   │   │   │       ├── cainjection_in_apigeeorganizations.yaml
         │   │   │   │       ├── cainjection_in_apigeeroutes.yaml
         │   │   │   │       ├── cainjection_in_apigeetelemetries.yaml
         │   │   │   │       ├── k8s_list_map_keys.yaml
         │   │   │   │       ├── nested_metadata_validation_properties.yaml
         │   │   │   │       ├── webhook_in_apigeedatastores.yaml
         │   │   │   │       ├── webhook_in_apigeedeployments.yaml
         │   │   │   │       ├── webhook_in_apigeeenvironments.yaml
         │   │   │   │       ├── webhook_in_apigeeissues.yaml
         │   │   │   │       ├── webhook_in_apigeeorganizations.yaml
         │   │   │   │       ├── webhook_in_apigeeroutes.yaml
         │   │   │   │       └── webhook_in_apigeetelemetries.yaml
         │   │   │   └── default
         │   │   │       └── kustomization.yaml
         │   │   ├── examples
         │   │   │   └── helmfiles
         │   │   │       ├── helmfile.yaml
         │   │   │       └── README.md
         │   │   └── tools
         │   │       ├── apigee-pull-push.sh
         │   │       ├── common.sh
         │   │       ├── create-service-account
         │   │       └── dump_kubernetes.sh
         │   ├── templates
         │   │   ├── apigee-operators-roles.yaml
         │   │   ├── apigee-operators.yaml
         │   │   ├── apigee-resources.yaml
         │   │   ├── cassandra-backup-clusterrolebinding.yaml
         │   │   ├── cassandra-backup-clusterrole.yaml
         │   │   ├── cassandra-restore-clusterrolebinding.yaml
         │   │   ├── cassandra-restore-clusterrole.yaml
         │   │   ├── _helpers.tpl
         │   │   ├── ingress-role-binding.yaml
         │   │   ├── ingress-role.yaml
         │   │   ├── istiod-cluster-role-binding.yaml
         │   │   ├── istiod-cluster-role.yaml
         │   │   ├── istiod-role-binding.yaml
         │   │   └── istiod-role.yaml
         │   └── values.yaml
         ├── apigee-org
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── ax-hash-salt-secret.yaml
         │   │   ├── connect-agent-gsa-secret.yaml
         │   │   ├── connect-agent-sa.yaml
         │   │   ├── data-encryption-secret.yaml
         │   │   ├── encryption-keys-secret.yaml
         │   │   ├── _helpers.tpl
         │   │   ├── mart-gsa-secret.yaml
         │   │   ├── mart-sa.yaml
         │   │   ├── NOTES.txt
         │   │   ├── organization.yaml
         │   │   ├── udca-gsa-secret.yaml
         │   │   ├── udca-sa.yaml
         │   │   ├── watcher-gsa-secret.yaml
         │   │   └── watcher-sa.yaml
         │   └── values.yaml
         ├── apigee-redis
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── _helpers.tpl
         │   │   ├── redis-creds-secret.yaml
         │   │   └── redis.yaml
         │   └── values.yaml
         ├── apigee-telemetry
         │   ├── Chart.yaml
         │   ├── templates
         │   │   ├── apigee-logger-gsa-secret.yaml
         │   │   ├── apigee-logger-sa.yaml
         │   │   ├── apigee-metrics-gsa-secret.yaml
         │   │   ├── apigee-metrics-sa.yaml
         │   │   ├── apigee-telemetry.yaml
         │   │   ├── _helpers.tpl
         │   │   └── NOTES.txt
         │   └── values.yaml
         └── apigee-virtualhost
             ├── Chart.yaml
             ├── templates
             │   ├── apigee-route-config.yaml
             │   ├── ca-cert.yaml
             │   ├── cert.yaml
             │   └── _helpers.tpl
             └── values.yaml
         




You now have a tools to configure, deploy, and manage Apigee hybrid in your Kubernetes cluster. Next, you will create the Kubernetes namespace in which most hybrid components operate. [1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-download-charts) [(NEXT) Step 3: Create the apigee namespace](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-check-cluster) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-helm-charts) [12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
