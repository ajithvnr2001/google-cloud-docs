---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication/
title: Sign in to Docker and Helm \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:18.710116+00:00
---

# Sign in to Docker and Helm  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Sign in to Docker and Helm Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to sign in to Docker or Helm using the Managed Harbor Service (MHS) credential helper or CLI secrets.

Harbor registry instances in Google Distributed Cloud (GDC) air-gapped use Identity-Aware Proxy (IAP) for authentication. You can sign in to your Harbor registry instance from the Docker or Helm CLI using either of the following methods:

  * **MHS credential helper (`docker-credential-mhs`)**: uses your authenticated GDC identity to handle IAP authentication automatically. After you sign in with the gdcloud CLI, `docker-credential-mhs` fetches your authenticated user identity and verifies your access with Harbor. After verification, Harbor provides a short-lived token to Docker or Helm so you can perform registry operations without creating or managing separate CLI secrets.
  * **CLI secrets** : uses a static CLI secret from your Harbor user profile. After you sign in to the Harbor web interface using IAP for the first time, you can retrieve your CLI secret and use it as your password when signing in from the Docker or Helm CLI. This method is only available with the Harbor UI.



## Before you begin

To configure Docker and Helm authentication for Harbor registry instances, you must have the MHS credential helper (`docker-credential-mhs`) installed in your environment. The credential helper is included by default in the gdcloud CLI bundle. For more information, see [gdcloud CLI overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview).

### Required IAM roles

To configure authentication for Harbor registry instances, contact your Project IAM Admin to request the **Harbor Instance Viewer** (`harbor-instance-viewer`) role, which lets you get, list, and watch Harbor instances in the project namespace. This role includes the required permissions to view the details of existing Harbor instances so you can retrieve the registry URLs for authentication.

## Sign in with the MHS credential helper

How you authenticate with `docker-credential-mhs` depends on your CLI client: you can configure Docker to fetch credentials automatically, or retrieve temporary credentials directly to sign in to Docker.

### Sign in to Docker

To authenticate with Docker, follow these steps:

  1. Sign in to the Management API server with the gdcloud CLI by following the instructions in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).

  2. Configure Docker to use the MHS credential helper `docker-credential-mhs`:
         
         TENANT_PROJECT=PROJECT_NAME
         HARBOR_INSTANCE_NAME=HARBOR_INSTANCE_NAME
         REGISTRY=$(kubectl get harborinstance $HARBOR_INSTANCE_NAME -n $TENANT_PROJECT -o jsonpath='{.status.url}' | sed s#https://##)
         
         docker-credential-mhs configure-docker --registries=${REGISTRY}
         

Replace the following:

     * `PROJECT_NAME`: the name of your tenant project. This is the same project name you provided when [creating your Harbor instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances#create-a-harbor-registry-instance).
     * `HARBOR_INSTANCE_NAME`: the name of the Harbor instance that you created in [Create Harbor registry instances](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances).
  3. Follow the instructions in [Configure Docker to trust the Harbor root CA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-docker-trust#configure-docker-to-trust-harbor-root-ca).

  4. Optional: Verify that the credential helper is successfully configured by verifying the `mhs` entry is added to `~/.docker/config.json`:
         
         cat DOCKER_CONFIG_PATH
         

Replace `DOCKER_CONFIG_PATH` with the path to your Docker configuration file, such as `~/.docker/config.json`.

The output is similar to the following:
         
         {
             "auths": {
                 "10.200.0.1": {
                     "auth": "YWRtaW46YWRtaW4="
                 },
                 "10.200.16.5:10443": {
                     "auth": "YWRtaW46ZEROVVJCVWE1a1FBcE4xQQ=="
                 }
             },
             "credHelpers": {
                 "asia.gcr.io": "gcloud",
                 "eu.gcr.io": "gcloud",
                 "gcr.io": "gcloud",
                 "marketplace.gcr.io": "gcloud",
                 "myinstance-e2e-test-user.org-1.zone1.google.gdch.test": "mhs",
                 "staging-k8s.gcr.io": "gcloud",
                 "us-central1-docker.pkg.dev": "gcloud",
                 "us.gcr.io": "gcloud"
             }
         }
         

This example shows a successful output of `"myinstance-e2e-test-user.org-1.zone1.google.gdch.test": "mhs"`.

  5. Configure the tenant project in the gdcloud CLI:
         
         TENANT_PROJECT=PROJECT_NAME
         gdcloud config set project $TENANT_PROJECT
         

The following output is shown:
         
         Updated property [core/project].
         

  6. Identify a Harbor project that you have management access to. If one doesn't exist, [create a Harbor project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-projects).

  7. Perform Docker operations, such as an image push or pull:
         
         TENANT_PROJECT=PROJECT_NAME
         HARBOR_INSTANCE_NAME=HARBOR_INSTANCE_NAME
         REGISTRY=$(kubectl get harborinstance $HARBOR_INSTANCE_NAME -n $TENANT_PROJECT -o jsonpath='{.status.url}' | sed s#https://##)
         HARBOR_PROJECT=HARBOR_PROJECT_NAME
         
         # Push image
         docker pull nginx
         docker tag nginx ${REGISTRY}/${HARBOR_PROJECT}/nginx:latest
         docker push ${REGISTRY}/${HARBOR_PROJECT}/nginx:latest
         
         # Pull image
         docker pull ${REGISTRY}/${HARBOR_PROJECT}/nginx:latest
         

A successful output is similar to the following:
         
         # Push image
         root@gpc-adhoc-70846130vm-bootstrapper-zone1:~# docker push ${REGISTRY}/harbor-project/nginx:latest
         The push refers to repository [myinstance-e2e-test-user.org-1.zone1.google.gdch.test/harbor-project/nginx]
         e4e9e9ad93c2: Pushed
         6ac729401225: Pushed
         8ce189049cb5: Pushed
         296af1bd2844: Pushed
         63d7ce983cd5: Pushed
         b33db0c3c3a8: Pushed
         98b5f35ea9d3: Pushed
         latest: digest: sha256:7ba542bde95e6523a4b126f610553e3657b8108bc3175596ee7e911ae1219bfc size: 1778
         
         # Pull image
         root@gpc-adhoc-70846130vm-bootstrapper-zone1:~# docker pull ${REGISTRY}/library/nginx:latest
         latest: Pulling from library/nginx
         Digest: sha256:7ba542bde95e6523a4b126f610553e3657b8108bc3175596ee7e911ae1219bfc
         Status: Image is up to date for myinstance-e2e-test-user.org-1.zone1.google.gdch.test/harbor-project/nginx:latest
         

If the operation is unsuccessful, you might see the following output:
         
         E1025 19:21:39.322290 1273587 get.go:24] failed to get user name: user is not logged in or login expired, please login again
         

In this example, the GDC authentication session has expired, and you must sign in to GDC again. For more information, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).




### Sign in to Helm

To authenticate with Helm, follow these steps:

  1. After authenticating with GDC, retrieve your user credentials from the credential helper:
         
         echo $REGISTRY | docker-credential-mhs get
         

The output is similar to the following:
         
         {"Username":"tokenreview$fop-infrastructure-operator@example.com","Secret":"STS-Bearer-3q2o6mBKk44Gzi4105vyiSnXMuixtnm-RnyxSgJtnYkNbGV7drpwgIuftinAXVlo0Im9kgoGmc2WcZTSjE-vh2a71Su7YjB6qIAjAQ5ABkY03AHNfkHhRZzxthumDIVAd08wm2weit3_NpMPgOnf9qMblds_Q0PAWk2OhpodBpCfyl3LWZpIZBaNVgtg-TB_7fjpEDOm-_Q5VYABScOgZFP_bw"}
         

  2. Sign in to the Helm CLI with the credentials. When prompted to enter the credentials, use the credentials returned by the credential helper.
         
         helm registry login $REGISTRY
         Username: tokenreview$fop-infrastructure-operator@example.com
         Password: STS-Bearer-3q2o6mBKk44Gzi4105vyiSnXMuixtnm-RnyxSgJtnYkNbGV7drpwgIuftinAXVlo0Im9kgoGmc2WcZTSjE-vh2a71Su7YjB6qIAjAQ5ABkY03AHNfkHhRZzxthumDIVAd08wm2weit3_NpMPgOnf9qMblds_Q0PAWk2OhpodBpCfyl3LWZpIZBaNVgtg-TB_7fjpEDOm-_Q5VYABScOgZFP_bw
         

A successful output for this operation looks like the following:
         
         Login Succeeded
         




## Sign in with CLI secrets

To sign in to Docker or Helm with CLI secrets, follow these steps:

  1. Sign in to Harbor with an IAP user account.
  2. Click your username and select **User Profile**.
  3. To copy the CLI secret associated with your account, click content_copy **Copy**.
  4. Optional: To display buttons for automatically generating or manually creating a new CLI secret, click more_horiz **More** in your user profile.

**Note:** You can have only one CLI secret. When a new secret is generated or created, the old secret becomes invalid.
  5. If you generated a new CLI secret, click content_copy **Copy** to copy it.

  6. Use your CLI secret as the password when signing in to Harbor from the Docker or Helm CLI:
         
         docker login -u USERNAME -p CLI_SECRET HARBOR_INSTANCE_URL
         

Replace the following:

     * `USERNAME`: the Harbor account username.
     * `CLI_SECRET`: the generated CLI secret.
     * `HARBOR_INSTANCE_URL`: the URL of the Harbor instance.
**Note:** The CLI secret doesn't expire unless you manually rotate it. The CLI secret isn't associated with your user identity token. Signing out from Harbor or the GDC console doesn't revoke the CLI secret.



## What's next

After you sign in to Docker and Helm, your registry is connected and you can start using it:

  * [Push an image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/push-image)
  * [Pull an image with Docker](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/pull-image)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
