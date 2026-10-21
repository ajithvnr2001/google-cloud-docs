---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling/
title: Push and pull images \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:20.457762+00:00
---

# Push and pull images  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Push and pull images Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store, version, and retrieve container images using Docker or Podman. You can also pull images using the `crictl` tool to troubleshoot Google Kubernetes Engine nodes. To run workloads, see [Deploy to Google Cloud](https://docs.cloud.google.com/artifact-registry/docs/deploy), or see [Managing images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images) to list, tag, and delete images.

## Before you begin

  1. If the target repository does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. You must have at least Artifact Registry Writer [access](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the repository.
  3. To push images with Docker, [install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it is not already installed.
  4. To push images with Podman, install [Podman](https://podman.io/)
  5. Install [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) if it is not already installed.



### Required roles

To get the permissions that you need to push and pull images, ask your administrator to grant you the following IAM roles on the repository: 

  * Pull images: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Tag and push images: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authenticating to a repository

You must authenticate to repositories whenever you use Docker or another third-party client with a Docker repository. This section provides a quick summary of what you'll need to authenticate successfully. For detailed instructions, see [Setting up authentication for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication).

### Using a credential helper

For the [gcloud CLI credential helper](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper) or [standalone credential helper](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#standalone-helper), the Artifact Registry hosts you use must be in your Docker configuration file.

Artifact Registry does not automatically add all registry hosts to the Docker configuration file. Docker response time is significantly slower when there is a large number of configured registries. To minimize the number of registries in the configuration file, you add the hosts that you need to the file.

To confirm which hosts are configured, run the following command to display the contents of the configuration file:

  * Linux: `cat ~/.docker/config.json`
  * Windows: `type %USERPROFILE%\.docker\config.json`



The `credHelpers` section lists configured Artifact Registry Docker hosts. Host names end in `-docker.pkg.dev`. The following example shows some hosts configured for the gcloud CLI credential helper.
    
    
    "credHelpers": {
      "asia.gcr.io": "gcloud",
      "eu.gcr.io": "gcloud",
      "gcr.io": "gcloud",
      "marketplace.gcr.io": "gcloud",
      "northamerica-northeast1-docker.pkg.dev": "gcloud",
      "us-central1-docker.pkg.dev": "gcloud",
      "us-east1-docker.pkg.dev": "gcloud",
      "us.gcr.io": "gcloud"
    }
    

If a host you want to use is not in the list, run the credential helper again to add the host. For example, the following command adds `us-west1-docker.pkg.dev`.

  * gcloud CLI credential helper:
        
        gcloud auth configure-docker us-west1-docker.pkg.dev
        

  * Standalone credential helper
        
        docker-credential-gcr configure-docker us-west1-docker.pkg.dev
        




### Using an access token

For access token authentication, you generate a token and use it as a password with the `docker login` command. Tokens are valid for 60 minutes, so you should authenticate shortly before you tag, push, or pull images.

The following example generates an access token using service account [impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) and then authenticates to Artifact Registry. You must have permissions in the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to generate a token this way.

### Linux
    
    
    gcloud auth print-access-token \
      --impersonate-service-account  ACCOUNT | docker login \
      -u oauth2accesstoken \
      --password-stdin https://LOCATION-docker.pkg.dev
    

### Windows
    
    
    gcloud auth print-access-token `
    --impersonate-service-account  ACCOUNT
    
    ya29.8QEQIfY_...
    
    docker login -u oauth2accesstoken -p "ya29.8QEQIfY_..." `
    https://LOCATION-docker.pkg.dev
    

If you don't have permissions to impersonate a service account, you can activate the service account in your gcloud CLI session and then obtain a token. For details, see the instructions to set up [access token](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#token) authentication.

### Using a service account key

For a service account key, you use the key as a password with the `docker login` command.

For example, the following command uses the base64-encoded service account key in the file `key.json` to authenticate to `us-west1-docker.pkg.dev`.

### Linux
    
    
    cat key.json | docker login -u _json_key_base64 --password-stdin \
    https://us-west1-docker.pkg.dev
    

### Windows
    
    
    docker login -u _json_key_base64 --password-stdin https://us-west1-docker.pkg.dev < key.json
    

For details, see the instructions to set up [service account key](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#json-key) authentication.

## Pushing an image with Docker

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

To push a local image to a standard Docker repository, you tag it with the repository name and then push the image.

If your Artifact Registry Docker repository has tag immutability enabled, a tag must always reference the same image digest in the repository. You cannot use the tag on another version of the same image that you push to the repository. For more information about image digests, tags, and tag immutability, see [Container image versions](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions).

For large images, the following limits apply:

Upload time
    If you authenticate to Artifact Registry using an access token, the token is only valid for 60 minutes. If you expect your upload time to exceed 60 minutes, use a different [authentication method](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#methods).
Image size
    The maximum artifact size is 5 TB.
    Artifact Registry does not support Docker [chunked uploads](https://docs.docker.com/registry/spec/api/#chunked-upload). Some tools support uploading large images with either chunked uploads or a single [monolithic upload](https://docs.docker.com/registry/spec/api/#monolithic-upload). You must use monolithic uploads to push images to Artifact Registry.

### Tagging the local image

  1. Make sure that you are authenticated to the repository.

  2. Determine the name of the image. The format of a full image name is:
         
         LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE
         

Replace the following values:

     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository where the image is stored.
     * `PROJECT-ID` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
     * `REPOSITORY` is the name of the repository where the image is stored.
     * `IMAGE` is the image's name. It can be different than the image's local name.

For example, consider an image with the following characteristics:

     * Repository location: `us-west1`
     * Repository name: `my-repo`
     * Project ID: `my-project`
     * Local image name: `my-image`
     * Target image name: `test-image`

This image name for this example is:
    
    us-west1-docker.pkg.dev/my-project/my-repo/test-image
    

**Note:** The name for the image that you will store in the repository can be different from the image name on your local machine.

For details about the image name format, including handling domain-scoped projects, see [Repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names). 

  3. Tag the local image with the repository name.
         
         docker tag SOURCE-IMAGE LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
         

Replace SOURCE-IMAGE with the local image name or image ID and TAG with the tag. If you don't specify a tag, Docker applies the default `latest` tag.

If the immutable image tags setting is enabled, tags must be unique for each image version, including the `latest` tag. You cannot push an image to the repository if the tag is already used by another version of the same image in the repository. To verify if the setting is enabled for the repository, run the command:
         
         gcloud artifacts repositories describe REPOSITORY \
             --project=PROJECT-ID \
             --location=LOCATION
         

For the example image from the previous step, you would use the following command if the local image `my-image` is in the current directory:
         
         docker tag my-image us-west1-docker.pkg.dev/my-project/my-repo/test-image
         

If you want to apply a specific tag, use the command:
         
         docker tag SOURCE-IMAGE LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
         

To use the tag `staging` with the example image, you add `:staging` to the command:
         
         docker tag my-image us-west1-docker.pkg.dev/my-project/my-repo/test-image:staging
         




### Push the tagged image to Artifact Registry

**Note:** Artifact Registry does not support Docker [chunked uploads](https://docs.docker.com/registry/spec/api/#chunked-upload). Some container image tools support uploading large container images with either chunked uploads or a single [monolithic upload](https://docs.docker.com/registry/spec/api/#monolithic-upload). You must use monolithic uploads when you push container images to Artifact Registry.

  1. Make sure that you are authenticated to the repository.

If you used `gcloud auth configure-docker` or `docker-credential-gcr configure-docker` to configure your Docker client, verify that the target hostname is in your Docker configuration file.

  2. Push the tagged image with the command:
         
         docker push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE
         

This command pushes the image that has the tag `latest`. If you want to push an image that has a different tag, use the command:
         
         docker push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
         




When you push an image, it is stored in the specified repository.

After pushing your image, you can:

  * Go to the [Google Cloud console](https://console.cloud.google.com/artifacts) to view the image.

  * Run the `gcloud` command to view the image's tags and automatically-generated digest:
        
        gcloud artifacts docker images list \
        LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE [--include-tags]
        

The following example output shows truncated image digests, but the command always returns the full image digest.
        
        IMAGE                                                 DIGEST         CREATE_TIME          UPDATE_TIME
          us-west1-docker.pkg.dev/my-project/my-repo/my-image  sha256:85f...  2019-04-10T15:08:45  2019-04-10T15:08:45
          us-west1-docker.pkg.dev/my-project/my-repo/my-image  sha256:238...  2019-04-10T17:23:53  2019-04-10T17:23:53
          us-west1-docker.pkg.dev/my-project/my-repo/my-image  sha256:85f...  2019-04-10T15:08:46  2019-04-10T15:08:46
        




## Pushing an image with Podman

You can push a container image from Podman to Artifact Registry.

  1. Build your image with Podman using the following command: 
         
         podman build -t IMAGE:latest .
         

  2. Tag your local Podman image for Artifact Registry.

Use the full Artifact Registry path for the tag. The format is the same as for Docker: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/IMAGE:TAG`

Run the following command:
         
         podman tag IMAGE-NAME LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY_NAME/PODMAN-IMAGE:TAG
         

  3. Authenticate Podman with Artifact Registry. To use it with the credential helper, run the following command:
         
         gcloud auth configure-docker LOCATION-docker.pkg.dev
         

**Note:** By default, Podman looks for credentials in `~/.config/containers/auth.json` and falls back to `~/.docker/config.json` if the Podman default file doesn't exist or contain the necessary credentials. If you encounter issues, copy the `auths` section from `~/.docker/config.json` to `~/.config/containers/auth.json`, or use the `podman login` command.

If Podman can't obtain credentials automatically, you can also authenticate with an access token. Run the following command:
         
         gcloud auth print-access-token | podman login -u oauth2accesstoken --password-stdin LOCATION-docker.pkg.dev
         

  4. Push the tagged image to Artifact Registry:
         
         podman push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY_NAME/IMAGE:TAG
         

Ensure that the tag exactly matches the one you used to tag the local Podman image.




## Pulling images with Docker

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual 

  1. Make sure that you are authenticated to the repository.

If you used `gcloud auth configure-docker` or `docker-credential-gcr configure-docker` to configure your Docker client, verify that the target hostname is in your Docker configuration file.

  2. To pull from a repository, use the command:

### ghcr.io
         
         docker pull LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/OWNER/IMAGE:TAG
         

or
         
         docker pull LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/OWNER/IMAGE@IMAGE-DIGEST
         

Replace the following values:

     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository where the image is stored.
     * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
     * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `REPOSITORY` is the name of the repository where the image is stored.
     * `OWNER` is the GitHub user account or organization name of the repository owner.
     * `IMAGE` is the image's name in the repository.
     * `TAG` is the tag for the image version that you want to pull.
     * `IMAGE-DIGEST` is the sha256 hash value of the image contents. Each version of an image has a unique image digest. In Google Cloud console, click the specific image to see its metadata. The digest is listed as the **Image digest**.

For example, consider an image with the following characteristics:

     * Repository location: `us-west1`
     * Repository name: `my-repo`
     * Project ID: `my-project`
     * Repository owner: `owner-name`
     * Image name: `test-image`
     * Tag: `staging`

This command to pull the image is:
    
    docker pull us-west1-docker.pkg.dev/my-project/my-repo/owner-name/test-image:staging
    

### Other repositories
    
    docker pull LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
    

or
    
    docker pull LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE@IMAGE-DIGEST
    

Replace the following values:

     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository where the image is stored.
     * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
     * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `REPOSITORY` is the name of the repository where the image is stored.
     * `IMAGE` is the image's name in the repository.
     * `TAG` is the tag for the image version that you want to pull.
     * `IMAGE-DIGEST` is the sha256 hash value of the image contents. Each version of an image has a unique image digest. In Google Cloud console, click the specific image to see its metadata. The digest is listed as the **Image digest**.

For example, consider an image with the following characteristics:

     * Repository location: `us-west1`
     * Repository name: `my-repo`
     * Project ID: `my-project`
     * Image name: `test-image`
     * Tag: `staging`

This command to pull the image is:
    
    docker pull us-west1-docker.pkg.dev/my-project/my-repo/test-image:staging
    




Docker downloads the specified image.

If you request an image from a remote repository, the remote repository downloads and caches the image from the upstream source if a cached copy doesn't exist.

If you request an image from a virtual repository, Artifact Registry searches upstream repositories for the requested image. If you request a version that is available in more than one upstream repository, Artifact Registry chooses an upstream repository to use based on the priority settings configured for the virtual repository.

For example, consider a virtual repository with the following priority settings for upstream repositories:

  * `main-repo`: Priority set to `100`
  * `secondary-repo1`: Priority set to `80`.
  * `secondary-repo2`: Priority set to `80`.
  * `test-repo`: Priority set to `20`.



`main-repo` has the highest priority value, so the virtual repository always searches it first.

Both `secondary-repo1` and `secondary-repo2` have priority set to `80`. If a requested image is not available in `main-repo`, Artifact Registry searches these repositories next. Since they both have the same priority value, Artifact Registry can choose to serve an image from either repository if the version is available in both of them.

`test-repo` has is lowest priority value and will serve a stored artifact if none of the other upstream repositories has it.

## Pulling images with `crictl`

`crictl` is a useful command-line tool for CRI runtime developers to debug their runtime without needing to set up Kubernetes components. If your Google Kubernetes Engine nodes use a [containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd "containerd node images on GKE") runtime, you can pull images from Artifact Registry using [`crictl`](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md "`crictl` usage and installation").

Since `crictl` is primarily a troubleshooting tool, some docker commands such as pushing or tagging images are not available.

To pull an image from Artifact Registry:

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. [SSH into](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connecting_to_vms) the node you are troubleshooting.

  3. Obtain an access token for authentication with the repository.
         
         curl -s "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

  4. Pull the image using `crictl pull --creds` and the `access_token` value
         
         crictl pull --creds "oauth2accesstoken:ACCESS_TOKEN" LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG

or
         
         crictl pull --creds "oauth2accesstoken:ACCESS_TOKEN" LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE@IMAGE-DIGEST

The output looks like the following:
         
         Image is up to date for sha256:0f25067aa9c180176967b4b50ed49eed096d43fa8c17be9a5fa9bff05933bee5




## What's next

  * Learn about [managing tags and deleting images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images).
  * If you want to run containers on Compute Engine, learn about [containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers).
  * Use `crictl` to [debug Kubernetes nodes](https://kubernetes.io/docs/tasks/debug-application-cluster/crictl "debug kubernetes nodes using crictl")
  * Learn to use `crictl` to pull images from [private Artifact Registry repositories](https://docs.cloud.google.com/artifact-registry/docs/integrate-gke#pulling_from_a_private_repository_with_crictl)
  * Learn more about configuring `crictl` [image registries](https://github.com/containerd/cri/blob/master/docs/registry.md "containerd image registry")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
