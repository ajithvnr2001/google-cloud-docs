---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-container-images/
title: About container image digests \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:36.743924+00:00
---

# About container image digests  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About container image digests Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes image digests, including what image digests are, how to find them, and how to enforce their use in Kubernetes clusters. This page is intended for developers and operators who build and deploy container images.

A [container image digest](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests) uniquely and immutably identifies a container image. When you deploy images by digest, you avoid the downsides of deploying by [image tags](https://github.com/opencontainers/distribution-spec/blob/main/spec.md).

The commands on this page assume that you have access to a Linux or macOS shell environment with tools such as the [Google Cloud CLI](https://docs.cloud.google.com/sdk), Docker, cURL, [`jq`](https://jqlang.github.io/jq/), and [`pack`](https://buildpacks.io/docs/tools/pack/) already installed. Or, you can use [Cloud Shell](https://docs.cloud.google.com/shell), which has these tools pre-installed.

## Container images and image tags

When working with container images, you need a way to refer to the images that you use. [Image tags](https://github.com/opencontainers/distribution-spec/blob/main/spec.md) are a common way of referring to different revisions of an image. A common approach is to tag images with a version identifier at build time. For example, `v1.0.1` could refer to a version that you call `1.0.1`.

Tags make image revisions easy to look up by human-readable strings. However, tags are mutable references, which means the image referenced by a tag can change, as illustrated in the following diagram:

![Image tag pointing to an outdated image.](https://docs.cloud.google.com/static/architecture/images/using-container-images-1-tags.svg)

As the previous diagram shows, if you publish a new image using the same tag as an existing image, the tag stops pointing to the existing image and starts pointing to your new image.

### Disadvantages of image tags

Because tags are mutable, they have the following disadvantages when you use them to deploy an image:

  * In Kubernetes, deploying by tag can result in unexpected results. For example, assume that you have an existing Deployment resource that references a container image by tag `v1.0.1`. To fix a bug or make a small change, your build process creates a new image with the same tag `v1.0.1`. New Pods that are created from your Deployment resource can end up using either the old or the new image, even if you don't change your Deployment resource specification. This problem also applies to other Kubernetes resources such as StatefulSets, DaemonSets, ReplicaSets, and Jobs.

  * If you use tools to scan or analyze images, results from these tools are only valid for the image that was scanned. To ensure that you deploy the image that was scanned, you cannot rely on the tag because the image referred by the tag might have changed.

  * If you use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) with [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs), tag-based deployment is disallowed because it's impossible to determine the exact image that is used when a Pod is created.




When you deploy your images, you can use an image digest to avoid the disadvantages of using tags. You can still add tags to your images if you like, but you don't have to do so.

## Structure of an image

An image consists of the following components:

  * An [image manifest](https://github.com/opencontainers/image-spec/blob/main/manifest.md#oci-image-manifest-specification)
  * A [configuration object](https://github.com/opencontainers/image-spec/blob/main/manifest.md#image-manifest-property-descriptions)
  * An array of one or more [file system layers](https://github.com/opencontainers/image-spec/blob/main/layer.md#image-layer-filesystem-changeset)
  * An optional [image index](https://github.com/opencontainers/image-spec/blob/main/image-index.md#oci-image-index-specification)



These components are illustrated in the following diagram:

![Components of an image showing details for an image manifest, a configuration object, file system layers, and an image index.](https://docs.cloud.google.com/static/architecture/images/using-container-images-2-structure.svg)

The preceding image shows additional detail about image components:

  * The image manifest is a JSON document that contains a reference to the configuration object, the file system layers, and optional metadata.
  * The image manifest references the configuration object and each of the file system layers using their `digest` attributes. The value of a `digest` attribute is a cryptographic hash of the contents that the digest refers to, typically calculated using the [SHA-256](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#sha-256) algorithm.
  * The digest values are used to construct immutable addresses to the objects. This process is called [content-addressable storage](https://wikipedia.org/wiki/Content-addressable_storage), and it means that you can retrieve image manifests, image indexes, configuration objects, and layers based on their digests.
  * The image digest is the hash of the image index or image manifest JSON document.
  * The configuration object is a JSON document that defines [properties of the image](https://github.com/opencontainers/image-spec/blob/main/config.md#properties), such as the CPU architecture, entrypoint, exposed ports, and environment variables.
  * The file system layer array defines the order that the container runtime uses to stack the layers. The layers are distributed as [tar files](https://wikipedia.org/wiki/Tar_\(computing\)), typically compressed using the [`gzip`](https://www.gzip.org/) utility.
  * The optional image index, sometimes referred to as the [manifest list](https://docs.docker.com/registry/spec/manifest-v2-2/#manifest-list), refers to one or more image manifests. The reference is the digest of the image manifest. An image index is useful when you produce multiple related images for different [platforms](https://github.com/opencontainers/image-spec/blob/main/image-index.md#image-index-property-descriptions), such as `amd64` and `arm64` architectures.



For more information, see the section Exploring image manifests, digests, and tags.

## Finding image digests

To use image digests for deployment, you must first find the digest. Then, you can use the digest with your deployment command or include it in your Kubernetes manifests.

You can get the digest of an image in various ways, depending on your current situation. The following sections contain examples for different products and tools.

In the following sections, run the commands in Cloud Shell or in a shell environment with tools such as the gcloud CLI, Docker, cURL, and `jq` already installed.

### Artifact Registry

  * For images stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs), you can use the [`gcloud artifacts docker images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/describe).
        
        gcloud artifacts docker images describe \
            LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE:TAG \
            --format 'value(image_summary.digest)'
        

Replace the following:

    * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of your repository
    * `PROJECT`: your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `REPOSITORY`: your repository name
    * `IMAGE`: your image name
    * `TAG`: your image tag



### Container Registry

**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

  * For images stored in [Container Registry](https://docs.cloud.google.com/container-registry/docs), you can use the [`gcloud container images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/images/describe) to get the digest for an image by providing the name and a tag. Use the [`--format` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats) to only display the digest:
        
        gcloud container images describe \
            gcr.io/google-containers/pause-amd64:3.2 \
            --format 'value(image_summary.digest)'
        

The output looks similar to the following, though your digest value might differ:
        
        sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108
        




### Cloud Build

For images built using [Cloud Build](https://docs.cloud.google.com/build/docs), you can get the image digest by using the [`gcloud builds describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/describe) with the `--format` flag. This approach works regardless of which registry you used to publish your image.

  * For an already completed build, do the following:

    1. Get a list of builds for your project:
           
           gcloud builds list
           

Make a note of a `BUILD_ID`.

    2. Get the image digest:
           
           gcloud builds describe BUILD_ID \
               --format 'value(results.images[0].digest)'
           

Replace `BUILD_ID` with the unique ID that Cloud Build assigned to your build.

  * Get the image name and digest for the latest build from Cloud Build for your current project:
        
        gcloud builds describe \
            $(gcloud builds list --limit 1 --format 'value(id)') \
            --format 'value[separator="@"](results.images[0].name,results.images[0].digest)'
        

  * If your build produced multiple images, filter the output and get the digest of one of the images:
        
        gcloud builds describe BUILD_ID --format json \
            | jq -r '.results.images[] | select(.name=="YOUR_IMAGE_NAME") | .digest'
        

Replace `YOUR_IMAGE_NAME` with the name of one of the images from your [`cloudbuild.yaml` file](https://docs.cloud.google.com/build/docs/build-config#images).

  * If you submit a build to Cloud Build using the [`gcloud builds submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit), you can capture the image digest from the output in an environment variable:
        
        IMAGE_DIGEST=$(gcloud builds submit \
            --format 'value(results.images[0].digest)' | tail -n1)
        




### Cloud Native Buildpacks

  * If you use [Cloud Native Buildpacks](https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks) and the Google Cloud builder to build and publish images, you can capture the image name and digest by using the `--quiet` flag with the `pack` command:
        
        pack build --builder gcr.io/buildpacks/builder:v1 --publish --quiet \
            LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE \
            > image-with-digest.txt
        

Replace the following:

    * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of your repository
    * `PROJECT_ID`: your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `REPOSITORY`: your repository name
    * `IMAGE`: your image name

The file `image-with-digest.txt` contains the image name and digest.

Use the `--tag` flag if you want to add tags to the image.




### Docker client

  * The [`manifest` subcommand](https://docs.docker.com/engine/reference/commandline/manifest/) of the `docker` command line client can fetch image manifests and manifest lists from container image registries.

Get the digest from the manifest list of the image `registry.k8s.io/pause:3.9`, for the `amd64` CPU architecture and the `linux` operating system:
        
        docker manifest inspect --verbose registry.k8s.io/pause:3.9 | \
            jq -r 'if type=="object"
                then .Descriptor.digest
                else .[] | select(.Descriptor.platform.architecture=="amd64" and
                .Descriptor.platform.os=="linux") | .Descriptor.digest
                end'
        

The output looks similar to the following:
        
        sha256:8d4106c88ec0bd28001e34c975d65175d994072d65341f62a8ab0754b0fafe10
        

  * For images that are stored in your local [Docker daemon](https://docs.docker.com/config/daemon/), and that have been either pulled from or pushed to an image registry, you can use the Docker command line tool to get the image digest:

    1. Pull the image to your local [Docker daemon](https://docs.docker.com/config/daemon/):
           
           docker pull docker.io/library/debian:bookworm
           

    2. Get the image digest:
           
           docker inspect docker.io/library/debian:bookworm \
               | jq -r '.[0].RepoDigests[0]' \
               | cut -d'@' -f2
           

The output looks similar to the following, though your digest value may differ:
           
           sha256:3d868b5eb908155f3784317b3dda2941df87bbbbaa4608f84881de66d9bb297b
           

  * List all images and digests in your local Docker daemon:
        
        docker images --digests
        

The output shows digests for images that have a digest value. Images only have a digest value if they were pulled from or pushed to an image registry.




### `crane` and `gcrane`

You can use the open source [`crane`](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md) and [`gcrane`](https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md) command-line tools to get the digest of an image without pulling the image to a local Docker daemon.

  1. Download `crane` and `gcrane` to your current directory:
         
         VERSION=$(curl -sL https://api.github.com/repos/google/go-containerregistry/releases/latest | jq -r .tag_name)
         curl -L "https://github.com/google/go-containerregistry/releases/download/${VERSION}/go-containerregistry_$(uname -s)_$(uname -m).tar.gz" | tar -zxf - crane gcrane
         

  2. Get image digests:
         
         ./gcrane digest gcr.io/distroless/static-debian11:nonroot
         

`crane` and `gcrane` have other features that are outside the scope of this page. For more information, see the documentation for [`crane`](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md#crane) and [`gcrane`](https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md#gcrane).




## Enforcing the use of image digests in Kubernetes deployments

If you want to enforce using digests for images that you deploy to your Kubernetes clusters, you can use [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) or [Open Policy Agent (OPA) Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/). Policy Controller is built from the OPA Gatekeeper open source project.

Policy Controller and OPA Gatekeeper both build on the [OPA policy engine](https://www.openpolicyagent.org/). Policy Controller and OPA Gatekeeper provide a [Kubernetes validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) to enforce policies, and [custom resource definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) for [constraint templates](https://github.com/open-policy-agent/frameworks/tree/master/constraint#what-is-a-constraint-template) and [constraints](https://github.com/open-policy-agent/frameworks/tree/master/constraint#what-is-a-constraint).

Constraint templates contain policy logic that is expressed using a high-level declarative language called [Rego](https://www.openpolicyagent.org/docs/latest/#rego). The following is a constraint template that validates that containers, [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/), and [ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) in a Kubernetes resource specification use images with digests:
    
    
    apiVersion: templates.gatekeeper.sh/v1
    kind: ConstraintTemplate
    metadata:
      name: k8simagedigests
      annotations:
        metadata.gatekeeper.sh/title: "Image Digests"
        metadata.gatekeeper.sh/version: 1.0.1
        description: >-
          Requires container images to contain a digest.
    
          https://kubernetes.io/docs/concepts/containers/images/
    spec:
      crd:
        spec:
          names:
            kind: K8sImageDigests
          validation:
            openAPIV3Schema:
              type: object
              description: >-
                Requires container images to contain a digest.
    
                https://kubernetes.io/docs/concepts/containers/images/
              properties:
                exemptImages:
                  description: >-
                    Any container that uses an image that matches an entry in this list will be excluded
                    from enforcement. Prefix-matching can be signified with `*`. For example: `my-image-*`.
    
                    It is recommended that users use the fully-qualified Docker image name (e.g. start with a domain name)
                    in order to avoid unexpectedly exempting images from an untrusted repository.
                  type: array
                  items:
                    type: string
      targets:
        - target: admission.k8s.gatekeeper.sh
          rego: |
            package k8simagedigests
    
            import data.lib.exempt_container.is_exempt
    
            violation[{"msg": msg}] {
              container := input.review.object.spec.containers[_]
              not is_exempt(container)
              not regex.match("@[a-z0-9]+([+._-][a-z0-9]+)*:[a-zA-Z0-9=_-]+", container.image)
              msg := sprintf("container <%v> uses an image without a digest <%v>", [container.name, container.image])
            }
    
            violation[{"msg": msg}] {
              container := input.review.object.spec.initContainers[_]
              not is_exempt(container)
              not regex.match("@[a-z0-9]+([+._-][a-z0-9]+)*:[a-zA-Z0-9=_-]+", container.image)
              msg := sprintf("initContainer <%v> uses an image without a digest <%v>", [container.name, container.image])
            }
    
            violation[{"msg": msg}] {
              container := input.review.object.spec.ephemeralContainers[_]
              not is_exempt(container)
              not regex.match("@[a-z0-9]+([+._-][a-z0-9]+)*:[a-zA-Z0-9=_-]+", container.image)
              msg := sprintf("ephemeralContainer <%v> uses an image without a digest <%v>", [container.name, container.image])
            }
          libs:
            - |
              package lib.exempt_container
    
              is_exempt(container) {
                  exempt_images := object.get(object.get(input, "parameters", {}), "exemptImages", [])
                  img := container.image
                  exemption := exempt_images[_]
                  _matches_exemption(img, exemption)
              }
    
              _matches_exemption(img, exemption) {
                  not endswith(exemption, "*")
                  exemption == img
              }
    
              _matches_exemption(img, exemption) {
                  endswith(exemption, "*")
                  prefix := trim_suffix(exemption, "*")
                  startswith(img, prefix)
              }
    

The preceding policy contains a regular expression as input to the [`re_match` function](https://www.openpolicyagent.org/docs/v0.22.0/policy-reference/#regex). This regular expression matches the container image digest, and it is based on the [digest format in the Open Container Initiative Image Specification](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests).

Constraints apply the policy to Kubernetes resources by matching against attributes such as `kind` and `namespace`. The following example constraint applies the policy from the constraint template to all `Pod` resources in the `default` namespace.
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sImageDigests
    metadata:
      name: container-image-must-have-digest
    spec:
      match:
        kinds:
          - apiGroups: [""]
            kinds: ["Pod"]
        namespaces:
          - "default"
    

After you create the constraint template and the constraint, any new pods in the `default` namespace must use image digests to reference container images.

For the full example, see the [`imagedigests` policy](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/imagedigests) in the Gatekeeper policy library.

## About image manifests, digests, and tags

In this section, you learn how to explore existing images in registries using command-line tools such as `curl` and `docker`. Run the commands in Cloud Shell or in a shell environment with tools such as the gcloud CLI, Docker, cURL, and `jq` already installed. The following commands use public images in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

  * Get the manifest of the image `gcr.io/google-containers/pause-amd64:3.2` by using cURL and the [manifest URL](https://github.com/opencontainers/distribution-spec/blob/main/spec.md):
        
        curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/3.2
        

The output is similar to the following:
        
        {
           "schemaVersion": 2,
           "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
           "config": {
              "mediaType": "application/vnd.docker.container.image.v1+json",
              "size": 759,
              "digest": "sha256:80d28bedfe5dec59da9ebf8e6260224ac9008ab5c11dbbe16ee3ba3e4439ac2c"
           },
           "layers": [
              {
                 "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip",
                 "size": 296534,
                 "digest": "sha256:c74f8866df097496217c9f15efe8f8d3db05d19d678a02d01cc7eaed520bb136"
              }
           ]
        }
        

The `config` section has a digest attribute, and you can use this value to retrieve the configuration object. Similarly, each layer has a `digest` attribute that you can use to retrieve the tar file for that layer.

  * If the image includes the optional image index, an HTTP `GET` request to the manifest URL using a tag returns the image index instead of the image manifest.

Get the image index of the image `gcr.io/google-containers/pause:3.2`:
        
        curl -s https://gcr.io/v2/google-containers/pause/manifests/3.2
        

The output is similar to the following:
        
        {
           "schemaVersion": 2,
           "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
           "manifests": [
              {
                 "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                 "size": 526,
                 "digest": "sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108",
                 "platform": {
                    "architecture": "amd64",
                    "os": "linux"
                 }
              },
              {
                 "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                 "size": 526,
                 "digest": "sha256:bbb7780ca6592cfc98e601f2a5e94bbf748a232f9116518643905aa30fc01642",
                 "platform": {
                    "architecture": "arm",
                    "os": "linux",
                    "variant": "v7"
                 }
              },
              {
                 "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                 "size": 526,
                 "digest": "sha256:31d3efd12022ffeffb3146bc10ae8beb890c80ed2f07363515580add7ed47636",
                 "platform": {
                    "architecture": "arm64",
                    "os": "linux"
                 }
              },
              {
                 "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                 "size": 526,
                 "digest": "sha256:7f82fecd72730a6aeb70713476fb6f7545ed1bbf32cadd7414a77d25e235aaca",
                 "platform": {
                    "architecture": "ppc64le",
                    "os": "linux"
                 }
              },
              {
                 "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
                 "size": 526,
                 "digest": "sha256:1175fd4d728641115e2802be80abab108b8d9306442ce35425a4e8707ca60521",
                 "platform": {
                    "architecture": "s390x",
                    "os": "linux"
                 }
              }
           ]
        }
        

  * Filter the result to extract the image digest for the platform that you want. Get the digest of the image manifest for the `amd64` CPU architecture and the `linux` operating system:
        
        curl -s https://gcr.io/v2/google-containers/pause/manifests/3.2 | \
            jq -r '.manifests[] | select(.platform.architecture=="amd64" and .platform.os=="linux") | .digest'
        

The filtering in this command mimics how container runtimes, such as [containerd](https://github.com/containerd/containerd/blob/main/docs/content-flow.md#image-format), select the image that matches the target platform from the image index.

The output is similar to the following:
        
        sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108
        

The [image digest](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests) is the result of applying a [collision-resistant hash](https://wikipedia.org/wiki/Collision_resistance) to the image index or image manifest, typically the [SHA-256](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#sha-256) algorithm.

  * Get the digest of the image `gcr.io/google-containers/pause-amd64:3.2`:
        
        curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/3.2 \
            | shasum -a 256 \
            | cut -d' ' -f1
        

The output is similar to the following:
        
        4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108
        

You can reference this image using the image digest value as follows:
        
        gcr.io/google-containers/pause-amd64@sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108
        

  * Using the [content-addressable storage](https://wikipedia.org/wiki/Content-addressable_storage) concept, get the image manifest by using the digest as a reference:
        
        curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/sha256:4a1c4b21597c1b4415bdbecb28a3296c6b5e23ca4f9feeb599860a1dac6a0108
        

  * Many container image registries return the digest of manifests, image indexes, configuration objects, and file system layers in the `Docker-Content-Digest` header in response to HTTP `HEAD` requests. Get the digest of the image index of the image `gcr.io/google-containers/pause-amd64:3.2`:
        
        curl -s --head https://gcr.io/v2/google-containers/pause/manifests/3.2 \
            | grep -i Docker-Content-Digest \
            | cut -d' ' -f2
        

The output is similar to the following:
        
        sha256:927d98197ec1141a368550822d18fa1c60bdae27b78b0c004f705f548c07814f
        

The `Docker-Content-Digest` header is [not mandated by the Open Container Initiative Distribution specifications](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#checking-if-content-exists-in-the-registry), so this approach might not work with all container image registries. You can use it with [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) and [Container Registry](https://docs.cloud.google.com/container-registry/docs).

  * To retrieve an image configuration object using the digest value from the image manifest, do the following:

    1. Get the configuration digest:
           
           CONFIG_DIGEST=$(curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/3.2 \
               | jq -r '.config.digest')
           

    2. Use the configuration digest to retrieve the configuration object, and use `jq` to format the output to make it easier to read:
           
           curl -sL https://gcr.io/v2/google-containers/pause-amd64/blobs/$CONFIG_DIGEST \
               | jq
           

The output is similar to the following:
           
           {
             "architecture": "amd64",
             "config": {
               "Env": [
                 "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
               ],
               "Entrypoint": [
                 "/pause"
               ],
               "WorkingDir": "/",
               "OnBuild": null
             },
             "created": "2020-02-14T10:51:50.60182885-08:00",
             "history": [
               {
                 "created": "2020-02-14T10:51:50.60182885-08:00",
                 "created_by": "ARG ARCH",
                 "comment": "buildkit.dockerfile.v0",
                 "empty_layer": true
               },
               {
                 "created": "2020-02-14T10:51:50.60182885-08:00",
                 "created_by": "ADD bin/pause-amd64 /pause # buildkit",
                 "comment": "buildkit.dockerfile.v0"
               },
               {
                 "created": "2020-02-14T10:51:50.60182885-08:00",
                 "created_by": "ENTRYPOINT [\"/pause\"]",
                 "comment": "buildkit.dockerfile.v0",
                 "empty_layer": true
               }
             ],
             "os": "linux",
             "rootfs": {
               "type": "layers",
               "diff_ids": [
                 "sha256:ba0dae6243cc9fa2890df40a625721fdbea5c94ca6da897acdd814d710149770"
               ]
             }
           }
           

  * To retrieve file system layers using digest values from the image manifest, do the following:

    1. Get the digest of the layer that you want to retrieve:
           
           LAYER_DIGEST=$(curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/3.2 \
               | jq -r '.layers[0].digest')
           

    2. Use the layer digest to retrieve the layer tar file, and list the contents:
           
           curl -sL https://gcr.io/v2/google-containers/pause-amd64/blobs/$LAYER_DIGEST \
               | tar --list
           

This layer has only one file, called `pause`.

  * To look up tags associated with an image digest, do the following:

    1. Define the digest that you want to look up:
           
           IMAGE_DIGEST=$(curl -s https://gcr.io/v2/google-containers/pause-amd64/manifests/3.2 \
               | shasum -a 256 \
               | cut -d' ' -f1)
           

The `IMAGE_DIGEST` environment variable contains the digest of the image referenced by the tag `3.2`.

    2. Use the [image tags list endpoint, `/tags/list`](https://github.com/opencontainers/distribution-spec/blob/main/spec.md), to list tag information, and extract the tags for the digest value:
           
           curl -s "https://gcr.io/v2/google-containers/pause-amd64/tags/list?n=1" \
               | jq ".manifest.\"sha256:$IMAGE_DIGEST\".tag"
           

The output is similar to the following:
           
           [
             "3.2"
           ]
           

  * To get the manifest of an image from a Artifact Registry container image repository by using cURL, include an [access token](https://developers.google.com/identity/protocols/oauth2) in the `Authorization` request header:
        
        curl -s -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            https://LOCATION-docker.pkg.dev/v2/PROJECT_ID/REPOSITORY/IMAGE/manifests/DIGEST
        

Replace the following:

    * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of your repository
    * `PROJECT_ID`: your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `REPOSITORY`: your repository name
    * `IMAGE`: your image name
    * `DIGEST`: your image digest in the format `sha256:DIGEST_VALUE`



## What's next

  * To learn more about images, see the Open Container Initiative [Image Format](https://github.com/opencontainers/image-spec/blob/main/spec.md#image-format-specification) and [Distribution](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#distribution-specification) specifications.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
