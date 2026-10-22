---
url: https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images/
title: Pull cached Docker Hub images \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:43.670909+00:00
---

# Pull cached Docker Hub images  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Pull cached Docker Hub images Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry caches frequently-accessed public Docker Hub images on `mirror.gcr.io`. You can configure the Docker daemon to use a cached public image if one is available, or pull the image from Docker Hub if a cached copy is unavailable.

Google Cloud services such as Cloud Build and Google Kubernetes Engine automatically check for cached images before attempting to pull an image from Docker Hub. 

Cached images at `mirror.gcr.io` are:

  * Stored in a repository managed by Google Cloud.
  * More insulated from Docker Hub outages.
  * Integrated with the Google Cloud ecosystem.
  * Kept in sync with Docker Hub.



## Configure the Docker daemon

To configure your Docker daemon to pull images from the Artifact Registry cache:

### CLI

  1. Configure the daemon in one of the following ways:

     * To configure the Docker daemon automatically on startup, set the following value in `/etc/docker/daemon.json`
           
           {
             "registry-mirrors": ["https://mirror.gcr.io"]
           }
           

     * When you start the daemon, pass in the Artifact Registry hostname:
           
           dockerd --registry-mirror=https://mirror.gcr.io
           

     * Add the following line to your `/etc/default/docker` file:
           
           DOCKER_OPTS="${DOCKER_OPTS} --registry-mirror=https://mirror.gcr.io"
           

  2. Restart the Docker daemon.

     * On Linux, run one of the following commands:
           
           sudo service docker restart
           

or
           
           sudo service docker stop && sudo service docker start
           

     * On macOS or Windows, run the following command:
           
           docker-machine restart
           




### Docker UI

  1. Open Docker's **Preferences** menu.
  2. Click **Daemon**.
  3. Click **Advanced**. In the JSON field, add a `registry-mirrors` key with `https://mirror.gcr.io` as a value:
         
         {
           "registry-mirrors" : [
             "https://mirror.gcr.io"
           ]
         }
         

  4. Click **Apply & Restart**.




To verify that the cache is correctly configured, run:
    
    
    docker system info
    

The output should include `Registry Mirrors`, and should look similar to the following:
    
    
    Containers: 2
     Running: 0
     Paused: 0
     Stopped: 2
    Images: 2
    Server Version: 17.03.1-ce
    Storage Driver: overlay2
     Backing Filesystem: extfs
     Supports d_type: true
     Native Overlay Diff: true
    Logging Driver: json-file
    ...
    Registry Mirrors:
     https://mirror.gcr.io
    

## Pull cached images

Artifact Registry adds frequently requested images to the cache so they are available for future requests. It also periodically removes images that are no longer requested.

After you configure the Docker daemon to use the Artifact Registry cache, Docker performs the following steps when you pull a public Docker Hub image with a `docker pull` command:

  1. The Docker daemon checks the Artifact Registry cache and fetches the images if it exists. If your daemon configuration includes other Docker mirrors, the daemon checks each one in order for a cached copy of the image.
  2. If the image still isn't found, the Docker daemon fetches the image from the canonical repository on Docker Hub.



Pulling cached images does not count against Docker Hub rate limits. However, there is no guarantee that a particular image will remain cached for an extended period of time. Only obtain cached images on `mirror.gcr.io` by configuring the Docker daemon.

To authenticate to Docker Hub for images that aren't cached on `mirror.gcr.io`, use Artifact Registry [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview). Remote repositories support authentication to Docker Hub. We recommend authenticating to Docker Hub even if you are only using public images, as it will increase your download rate limit. For more information on Docker Hub download rate limits, see [Docker Hub rate limit](https://docs.docker.com/docker-hub/download-rate-limit/).

## Considerations

When you use the Artifact Registry Docker Hub cache, consider the following:

  * Artifact Registry acts only as a cache for the images you store on Docker Hub. Google Cloud doesn't validate, scan, or repair vulnerabilities in images cached from Docker Hub. You are responsible for ensuring that the images you store on Docker Hub meet the security and compliance requirements of your organization. If you need active vulnerability scanning, then consider using [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis).

  * The Artifact Registry cache is designed to improve stability, and doesn't immediately purge images when they are removed from Docker Hub. Images deleted from Docker Hub may remain available in the Artifact Registry cache for up to several days before they are removed from the cache. Google Cloud services that preconfigure cache usage, such as Cloud Build and Google Kubernetes Engine, may continue to automatically use unpurged images from the Artifact Registry cache.




## What's next

  * You can create Artifact Registry [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview) to cache Docker Hub images.
  * You can create your own local Docker mirrors to cache images. For details, see the [Docker documentation](https://docs.docker.com/registry/recipes/mirror/).
  * Read the [Docker Hub documentation](https://docs.docker.com/docker-hub/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
