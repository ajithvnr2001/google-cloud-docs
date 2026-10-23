---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/using-container-image-digests-in-kubernetes-manifests/
title: Using container image digests in Kubernetes manifests \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:23.921018+00:00
---

# Using container image digests in Kubernetes manifests  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/using-container-image-digests-in-kubernetes-manifests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Using container image digests in Kubernetes manifests Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2023-07-21 UTC

Autopilot  Standard 

This tutorial shows developers and operators who deploy containers to Kubernetes how to use container image digests to identify container images. A container image digest uniquely and immutably identifies a container image.

Deploying containers images by using the image digest provides several benefits compared to using image tags. For more information on image digests, see the accompanying document on [using container image digests](https://docs.cloud.google.com/architecture/using-container-images) before you continue this tutorial.

The `image` argument for containers in a Kubernetes Pod specification accepts images with digests. This argument applies everywhere you use a Pod specification, such as in the `template` section of Deployment, StatefulSet, DaemonSet, ReplicaSet, CronJob, and Job resources.

To deploy an image by using the digest, you use the image name, followed by `@sha256:` and the digest value. The following is an example of a Deployment resource that uses an image with a digest. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster..
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: echo-deployment
    spec:
      selector:
        matchLabels:
          app: echo
      template:
        metadata:
          labels:
            app: echo
        spec:
          containers:
          - name: echoserver
            image: gcr.io/google-containers/echoserver@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
            ports:
            - containerPort: 8080

One downside of using image digests is that you don't know the digest value until after you have published your image to a registry. As you build new images, the digest value changes, and you need a way to update your Kubernetes manifests each time you deploy.

This tutorial shows how you can use tools such as [Skaffold](https://skaffold.dev/), [kpt](https://kpt.dev/), [digester](https://github.com/google/k8s-digester), [kustomize](https://kustomize.io/), [`gke-deploy`](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke), and [`ko`](https://ko.build/) to use image digests in your manifests.

## Recommendations

This document presents several ways to use image digests in Kubernetes deployments. The tools described in this document are complementary. For example, you can use the output of a kpt function with kustomize to create variants for different environments. Skaffold can [build images using `ko`](https://skaffold.dev/docs/builders/builder-types/ko/) and deploy the images to your Kubernetes clusters using `kubectl` or kpt.

The reason the tools are complementary is that they perform [structured edits](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/declarative-application-management.md) based on the [Kubernetes resource model (KRM)](https://kubernetes.io/docs/reference/using-api/api-concepts/). This model makes the tools pluggable, and you can evolve your use of the tools to create processes and pipelines that help you deploy your apps and services.

To get started, we recommend the approach that works best with your existing tools and processes:

  * Skaffold can add digests to image references. You enable this function with a small configuration change. Adopting Skaffold provides additional benefits, such as abstracting away how different tools build and deploy container images.

  * By using the digester tool as a mutating admission webhook in your Kubernetes clusters, you can add digests to all your deployments with minimal impact on your current processes for building and deployment container images. The digester webhook also simplifies adoption of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs), because it only requires a label to be added to a namespace.

  * kpt is a great option if you need a flexible tool to manipulate Kubernetes manifests. The digester tool can be used as a client-side [KRM function](https://kpt.dev/book/02-concepts/03-functions) in a [kpt pipeline](https://kpt.dev/book/04-using-functions/01-declarative-function-execution).

  * If you already use kustomize to manage Kubernetes manifests across environments, we recommend that you take advantage of its image transformers to deploy images by digest.

  * `ko` is a great way to build and publish images for Go apps, and it is used by open source projects such as [Knative](https://knative.dev/), [Tekton](https://tekton.dev/), and [sigstore](https://sigstore.dev/).




If you don't use any of the tools described in this document, we recommend that you start with Skaffold and the digester webhook. Skaffold is a common tool used by both developers and release teams, and it integrates with the other tools described in this tutorial. You can take advantage of these integration options as your requirements evolve. The digester Kubernetes webhook complements Skaffold by enabling digest-based deployments for an entire cluster.

## Objectives

  * Use Skaffold to build and push an image, and to insert the image name and digest in a Kubernetes manifest.
  * Use the digester client-side function and mutating admission webhook to add digests to images in Kubernetes Pods and Pod templates.
  * Use kpt setters to replace an image tag in a Kubernetes manifest with an image digest.
  * Use kustomize to generate a Kubernetes manifest with an image digest.
  * Use `gke-deploy` to resolve an image tag to a digest in a Kubernetes manifest.
  * Use `ko` to build and push an image, and to insert the image name and digest in a Kubernetes manifest. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. In Cloud Shell, set the default project for Google Cloud CLI:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your [project ID].

  6. Create a container image repository in Artifact Registry:
         
         gcloud artifacts repositories create REPOSITORY \
             --location=LOCATION \
             --repository-format=docker
         

Replace the following:

     * `REPOSITORY`: the name you want to use for your repository, for instance `digest-tutorial`.
     * `LOCATION`: an [Artifact Registry location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations), for instance `us-central1`.
  7. Configure authentication to the Artifact Registry location for the CLI tools used in this tutorial:
         
         gcloud auth configure-docker LOCATION-docker.pkg.dev
         




## Using Skaffold

[Skaffold](https://skaffold.dev/) is a command-line tool for continuous development and deployment of applications to Kubernetes clusters.

Use Skaffold to build an image, push the image to Artifact Registry, and replace the `image` placeholder value in a Kubernetes manifest template with the name, tag, and digest of the pushed image:

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/skaffold
         cd ~/container-image-digests-tutorial/skaffold
         

  2. Clone the Skaffold Git repository:
         
         git clone https://github.com/GoogleContainerTools/skaffold.git
         

  3. Go to the directory of the `getting-started` example:
         
         cd skaffold/examples/getting-started
         

  4. Checkout the Git tag that matches your version of Skaffold:
         
         git checkout $(skaffold version)
         

  5. View the `skaffold.yaml` configuration file:
         
         cat skaffold.yaml
         

The file resembles the following:
         
         apiVersion: skaffold/v4beta6
         kind: Config
         build:
           artifacts:
           - image: skaffold-example
         manifests:
           rawYaml:
           - k8s-pod.yaml

The `build.artifacts` section contains a placeholder image name. Skaffold looks for this placeholder in the input manifest files.

The `manifests` section tells Skaffold to read an input manifest from the current directory with the name `k8s-pod.yaml`.

For an overview of all available options, see the [`skaffold.yaml` reference documentation](https://skaffold.dev/docs/references/yaml/).

  6. View the Kubernetes manifest template:
         
         cat k8s-pod.yaml
         

The file is the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: getting-started
         spec:
           containers:
           - name: getting-started
             image: skaffold-example

The `skaffold-example` placeholder value in the `image` field matches the value of the `image` field in the `skaffold.yaml` file. Skaffold replaces this placeholder value with the full image name and digest in the rendered output.

  7. Build and push the image to Artifact Registry:
         
         skaffold build \
             --default-repo=LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY \
             --file-output=artifacts.json \
             --interactive=false \
             --push=true \
             --update-check=false
         

This command uses the following flags:

     * The `--file-output` flag specifies the file where Skaffold saves information about the built image, including the digest value.
     * The `--push` flag instructs Skaffold to push the built image to the container image registry specified by the `--default-repo` flag.
     * The `--interactive` and `--update-check` flags are both set to `false`. Set these flags to `false` in non-interactive environments, such as build pipelines, but leave them as their default values (`true` for both flags) for local development.

If you use Cloud Deploy to deploy to GKE, use the file from the `--file-output` flag as the value of the `--build-artifacts` flag when you [create a release](https://docs.cloud.google.com/deploy/docs/integrating-ci#build_artifacts_versus_images).

  8. Render the expanded Kubernetes manifest with the name, tag, and digest of the container image from the previous step:
         
         skaffold render \
             --build-artifacts=artifacts.json \
             --digest-source=none \
             --interactive=false \
             --offline=true \
             --output=rendered.yaml \
             --update-check=false
         

This command uses the following flags:

     * The `--build-artifacts` flag references the output file from the `skaffold build` command in the previous step.
     * The `--digest-source=none` flag means that Skaffold uses the digest value from the file provided in the `--build-artifacts` flag, instead of resolving the digest from the container image registry.
     * The `--offline=true` flag means that you can run the command without requiring access to a Kubernetes cluster.
     * The `--output` flag specifies the output file for the rendered manifest.
  9. View the rendered manifest:
         
         cat rendered.yaml
         

The output resembles the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: getting-started
         spec:
           containers:
           - image: LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/skaffold-example:TAG@sha256:DIGEST
             name: getting-started

In this output, you see the following values:

     * `TAG`: the tag that Skaffold assigned to the image.
     * `DIGEST`: the image digest value



## Using digester

[Digester](https://github.com/google/k8s-digester) adds digests to container and init container images in Kubernetes Pod and Pod template specifications. Digester replaces container image references that use tags:
    
    
    spec:
      containers:
      - image: gcr.io/google-containers/echoserver:1.10
    

With references that use the image digest:
    
    
    spec:
      containers:
      - image: gcr.io/google-containers/echoserver:1.10@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
    

Digester can run either as a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) in a Kubernetes cluster, or as a client-side [KRM function](https://kpt.dev/book/02-concepts/03-functions) with the kpt or kustomize command-line tools.

### Using the digester KRM function

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/digester-fn
         cd ~/container-image-digests-tutorial/digester-fn
         

  2. Download the digester binary:
         
         mkdir -p ${HOME}/bin
         export PATH=${HOME}/bin:${PATH}
         DIGESTER_VERSION=$(curl -sL https://api.github.com/repos/google/k8s-digester/releases/latest | jq -r .tag_name)
         curl -L "https://github.com/google/k8s-digester/releases/download/${DIGESTER_VERSION}/digester_$(uname -s)_$(uname -m)" --output ${HOME}/bin/digester
         chmod +x ${HOME}/bin/digester
         

  3. Create a Kubernetes Pod manifest that references the image `gcr.io/google-containers/echoserver` using the tag `1.10`:
         
         cat << EOF > pod.yaml
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - name: echoserver
             image: gcr.io/google-containers/echoserver:1.10
             ports:
             - containerPort: 8080
         EOF
         

  4. Run the digester KRM function using kpt with the manifests in the current directory (`.`):
         
         kpt fn eval . --exec digester
         

When you run this command, kpt performs an in-place update of the manifests in the current directory. If you want kpt to show the updated manifest on the console and leave the manifest file unchanged, add the `--output unwrap` flag.

  5. View the updated manifest:
         
         cat pod.yaml
         

The file is the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
             - name: echoserver
               image: gcr.io/google-containers/echoserver:1.10@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
               ports:
                 - containerPort: 8080




### Using the digester admission webhook

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/digester-webhook
         cd ~/container-image-digests-tutorial/digester-webhook
         

  2. Create a local Kubernetes cluster using [kind](https://kind.sigs.k8s.io/):
         
         kind create cluster
         

kind is a command-line tool to run local Kubernetes clusters using Docker.

  3. Deploy the digester webhook:
         
         DIGESTER_VERSION=$(curl -sL https://api.github.com/repos/google/k8s-digester/releases/latest | jq -r .tag_name)
         kustomize build "https://github.com/google/k8s-digester.git/manifests?ref=${DIGESTER_VERSION}" | kubectl apply -f -
         

  4. Create a Kubernetes namespace called `digester-demo` in the kind cluster:
         
         kubectl create namespace digester-demo
         

  5. Add the `digest-resolution: enabled` label to the `digester-demo` namespace:
         
         kubectl label namespace digester-demo digest-resolution=enabled
         

The digester webhook adds digests to Pods in namespaces with this label.

  6. Create a Kubernetes Deployment manifest that references the image `gcr.io/google-containers/echoserver` using the tag `1.10`:
         
         cat << EOF > deployment.yaml
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: echo-deployment
         spec:
           selector:
             matchLabels:
               app: echo
           template:
             metadata:
               labels:
                 app: echo
             spec:
               containers:
               - name: echoserver
                 image: gcr.io/google-containers/echoserver:1.10
                 ports:
                 - containerPort: 8080
         EOF
         

  7. Apply the manifest in the `digester-demo` namespace:
         
         kubectl apply --filename deployment.yaml --namespace digester-demo \
             --output jsonpath='{.spec.template.spec.containers[].image}{"\n"}'
         

The `--output` flag instructs `kubectl` to output the image name to the console, followed by a newline character. The output is the following:
         
         gcr.io/google-containers/echoserver:1.10@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229

This output shows that the digester webhook added the image digest to the Pod template specification in the Deployment resource.

  8. Delete the kind cluster to free up resources in your Cloud Shell session:
         
         kind delete cluster
         




## Using kpt setters

[kpt](https://kpt.dev/) is a command-line tool to manage, manipulate, customize, and apply Kubernetes resource manifests.

You can use the `create-setters` and `apply-setters` KRM functions from the [kpt Functions Catalog](https://catalog.kpt.dev/) to update image digests in your Kubernetes manifests when you build new images.

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/kpt
         cd ~/container-image-digests-tutorial/kpt
         

  2. Create a kpt package in the current directory:
         
         kpt pkg init --description "Container image digest tutorial"
         

  3. Create a Kubernetes Pod manifest that references the image `gcr.io/google-containers/echoserver` using the tag `1.10`:
         
         cat << EOF > pod.yaml
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - name: echoserver
             image: gcr.io/google-containers/echoserver:1.10
             ports:
             - containerPort: 8080
         EOF
         

  4. Use kpt to create a setter called `echoimage` for the manifest field, where the existing value is `gcr.io/google-containers/echoserver:1.10`:
         
         kpt fn eval . \
             --image gcr.io/kpt-fn/create-setters@sha256:0220cc87f29ff9abfa3a3b5643aa50f18d355d5e9dc9e1f518119633ddc4895c \
             -- "echoimage=gcr.io/google-containers/echoserver:1.10"
         

  5. View the manifest:
         
         cat pod.yaml
         

The file is the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - name: echoserver
             image: gcr.io/google-containers/echoserver:1.10 # kpt-set: ${echoimage}
             ports:
             - containerPort: 8080

  6. Get the digest value of the container image:
         
         DIGEST=$(gcloud container images describe \
             gcr.io/google-containers/echoserver:1.10 \
             --format='value(image_summary.digest)')
         

  7. Set the new field value:
         
         kpt fn eval . \
             --image gcr.io/kpt-fn/apply-setters@sha256:4d4295727183396f0c3c6a75d2560254c2f9041a39e95dc1e5beffeb49cc1a12 \
             -- "echoimage=gcr.io/google-containers/echoserver:1.10@$DIGEST"
         

When you run this command, kpt performs an in-place replacement of the `image` field value in the manifest.

  8. View the updated manifest:
         
         cat pod.yaml
         

The file is the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - name: echoserver
             image: gcr.io/google-containers/echoserver:1.10@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229 # kpt-set: ${echoimage}
             ports:
             - containerPort: 8080




## Using kustomize image transformers

[kustomize](https://kustomize.io/) is a command-line tool that lets you customize Kubernetes manifests by using overlays, patches, and transformers.

You can use the kustomize [image transformer](https://github.com/kubernetes-sigs/kustomize/blob/master/examples/transformerconfigs/README.md#images-transformer) to update the image name, tag, and digest in your existing manifest.

The following `kustomization.yaml` snippet shows you how to configure the image transformer to use the transformer `digest` value for images where the Pod specification `image` value matches the transformer `name` value:
    
    
    images:
    - name: gcr.io/google-containers/echoserver
      digest: sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229

To use a kustomize image transformer with an image digest, do the following:

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/kustomize
         cd ~/container-image-digests-tutorial/kustomize
         

  2. Create a `kustomization.yaml` file:
         
         kustomize init
         

  3. Create a Kubernetes manifest with a Pod specification that references the image `gcr.io/google-containers/echoserver` using the tag `1.10`:
         
         cat << EOF > pod.yaml
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - name: echoserver
             image: gcr.io/google-containers/echoserver:1.10
             ports:
             - containerPort: 8080
         EOF
         

  4. Add the manifest as a resource in the `kustomization.yaml` file:
         
         kustomize edit add resource pod.yaml
         

  5. Use an image transformer to update the digest of the image:
         
         kustomize edit set image \
             gcr.io/google-containers/echoserver@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
         

  6. View the image transformer in the `kustomization.yaml` file:
         
         cat kustomization.yaml
         

The file is the following:
         
         apiVersion: kustomize.config.k8s.io/v1beta1
         kind: Kustomization
         resources:
         - pod.yaml
         images:
         - digest: sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
           name: gcr.io/google-containers/echoserver

  7. View the resulting manifest:
         
         kustomize build .
         

The output is the following:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: echo
         spec:
           containers:
           - image: gcr.io/google-containers/echoserver@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
             name: echoserver
             ports:
             - containerPort: 8080

  8. To run the kustomize transformer and apply the resulting manifest to a Kubernetes cluster in one step, you can use the `kubectl apply` command with the `--kustomize` flag:
         
         kubectl apply --kustomize .
         

If you want to apply the output later, you can redirect the output of the `kustomize build` command to a file.




## Using `gke-deploy`

[`gke-deploy`](https://github.com/GoogleCloudPlatform/cloud-builders/blob/master/gke-deploy/README.md) is a command-line tool that you use with [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine). `gke-deploy` wraps the `kubectl` command-line tool and can modify the resources that you create following Google's recommended practices.

If you use the `gke-deploy` sub-commands `prepare` or `run`, `gke-deploy` resolves your image tags to digests and saves the expanded manifests with the image digests in the file `output/expanded/aggregated-resources.yaml` by default.

You can use `gke-deploy run` to both substitute the image tag for a digest and apply the expanded manifest to your GKE cluster. Although this command is convenient, there is a downside: the image tag is substituted at deployment time. The image associated with the tag might have changed in the time between when you decided to deploy, and when you deployed, resulting in deploying an unexpected image. For production deployments, we recommend separate steps for generating and applying manifests.

To replace an image tag in a Kubernetes deployment manifest with the image digest, do the following:

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/gke-deploy
         cd ~/container-image-digests-tutorial/gke-deploy
         

  2. Install `gke-deploy`:
         
         go install github.com/GoogleCloudPlatform/cloud-builders/gke-deploy@latest
         

  3. Create a Kubernetes Deployment manifest that references the image `gcr.io/google-containers/echoserver` using the tag `1.10`:
         
         cat << EOF > deployment.yaml
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: echo-deployment
         spec:
           selector:
             matchLabels:
               app: echo
           template:
             metadata:
               labels:
                 app: echo
             spec:
               containers:
               - name: echoserver
                 image: gcr.io/google-containers/echoserver:1.10
                 ports:
                 - containerPort: 8080
         EOF
         

  4. Generate an expanded manifest based on the `deployment.yaml` manifest:
         
         gke-deploy prepare \
             --filename deployment.yaml \
             --image gcr.io/google-containers/echoserver:1.10 \
             --version 1.10
         

  5. View the expanded manifest:
         
         cat output/expanded/aggregated-resources.yaml
         

The output is the following:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             app.kubernetes.io/managed-by: gcp-cloud-build-deploy
             app.kubernetes.io/version: "1.10"
           name: echo-deployment
           namespace: default
         spec:
           selector:
             matchLabels:
               app: echo
           template:
             metadata:
               labels:
                 app: echo
                 app.kubernetes.io/managed-by: gcp-cloud-build-deploy
                 app.kubernetes.io/version: "1.10"
             spec:
               containers:
               - image: gcr.io/google-containers/echoserver@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
                 name: echoserver
                 ports:
                 - containerPort: 8080

In the expanded manifest, the image tag is replaced by the digest.

The `--version` argument you used with the `gke-deploy` command sets the value of [the `app.kubernetes.io/version` label](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/) in the deployment and the Pod template metadata of the expanded manifest.

To learn how to use `gke-deploy` with Cloud Build, see the [Cloud Build documentation for `gke-deploy`](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-gke).




## Using `ko`

[`ko`](https://ko.build/) is a command-line tool and library for building [Go](https://golang.org/) container images and deploying them to Kubernetes clusters. `ko` builds images without using the Docker daemon, so you can use it in environments where you can't install Docker.

The `ko` sub-command [`build`](https://ko.build/reference/ko_build/) builds images and publishes them to a container image registry or loads them into your local Docker daemon.

The `ko` sub-command [`resolve`](https://ko.build/reference/ko_resolve/) does the following:

  * Identifies the images to build by finding placeholders in the `image` fields of the Kubernetes manifests that you provide by using the `--filename` argument.
  * Builds and publishes your images.
  * Replaces the `image` value placeholders with the names and digests of the images it built.
  * Prints the expanded manifests.



The `ko` sub-commands [`apply`](https://ko.build/reference/ko_apply/), [`create`](https://ko.build/reference/ko_create/), and [`run`](https://ko.build/reference/ko_run/) perform the same steps as `resolve`, and then execute `kubectl apply`, `create`, or `run` with the expanded manifests.

To build an image from Go source code, and add the digest of the image to a Kubernetes deployment manifest, do the following

  1. In Cloud Shell, create and go to a directory to store the files that you create in this section:
         
         mkdir -p ~/container-image-digests-tutorial/ko
         cd ~/container-image-digests-tutorial/ko
         

  2. Download `ko` and add it to your `PATH`:
         
         mkdir -p ${HOME}/bin
         export PATH=${HOME}/bin:${PATH}
         KO_VERSION=$(curl -sL https://api.github.com/repos/ko-build/ko/releases/latest | jq -r .tag_name | cut -c2-)
         curl -L "https://github.com/ko-build/ko/releases/download/v${KO_VERSION}/ko_${KO_VERSION}_$(uname -s)_$(uname -m).tar.gz" | tar -zxC ${HOME}/bin ko
         

  3. Create a Go app with the module name `example.com/hello-world` in a new directory called `app`:
         
         mkdir -p app/cmd/ko-example
         
         cd app
         
         go mod init example.com/hello-world
         
         cat << EOF > cmd/ko-example/main.go
         package main
         
         import "fmt"
         
         func main() {
             fmt.Println("hello world")
         }
         EOF
         

  4. Define the image repository that `ko` uses to publish images:
         
         export KO_DOCKER_REPO=LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY
         

This example uses Artifact Registry, but you can use `ko` with a different container image registry.

  5. To build and publish an image for your app, do one of the following steps:

     * Build and publish an image for your app by providing the path to your Go [main package](https://golang.org/ref/spec#Program_execution):
           
           ko build --base-import-paths ./cmd/ko-example
           

The optional argument `--base-import-paths` means that `ko` uses the short name of the main package directory as the image name.

`ko` prints the image name and digest to `stdout` in the following format:
           
           LOCATION-docker.pkg.dev/PROJECT_ID/ko-example@sha256:DIGEST

In this output, `DIGEST` is the image digest value.

**Note:** All other `ko` output goes to `stderr`. If you want to capture the image name and digest, you can capture `stdout` in an environment variable: 
           
           IMAGE_AND_DIGEST=$(ko build --base-import-paths ./cmd/ko-example)
           

     * Use `ko` to replace a manifest placeholder with the name and digest of the image it builds and publishes:

       1. Create a Kubernetes Pod manifest. The manifest uses the placeholder `ko://IMPORT_PATH_OF_YOUR_MAIN_PACKAGE` as the value of the `image` field:
              
              cat << EOF > ko-pod.yaml
              apiVersion: v1
              kind: Pod
              metadata:
                name: ko-example
              spec:
                containers:
                - name: hello-world
                  image: ko://example.com/hello-world/cmd/ko-example
              EOF
              

       2. Build and publish an image for your app, and replace the manifest placeholder with the image name and digest:
              
              ko resolve --base-import-paths --filename ko-pod.yaml
              

`ko` prints the manifest with the image name and digest to `stdout`:
              
              apiVersion: v1
              kind: Pod
              metadata:
                name: ko-example
              spec:
                containers:
                - name: hello-world
                  image: LOCATION-docker.pkg.dev/PROJECT_ID/ko-example@sha256:DIGEST

In this output, `DIGEST` is the image digest value.




## Clean up

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the tutorial. Alternatively, you can delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the resources

If you want to keep the Google Cloud project that you used in this tutorial, delete the individual resources:

  1. In Cloud Shell, delete the files you created in this tutorial:
         
         cd
         rm -rf ~/container-image-digests-tutorial
         

  2. Delete the container image repository in Artifact Registry:
         
         gcloud artifacts repositories delete REPOSITORY \
             --location=LOCATION --async --quiet
         




## What's next

  * Learn more about [container image digests](https://docs.cloud.google.com/architecture/using-container-images).
  * Learn more about the [digester client-side KRM function and Kubernetes mutating webhook](https://github.com/google/k8s-digester).
  * Explore [GitOps-style continuous delivery with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-07-21 UTC."],[],[]] 
