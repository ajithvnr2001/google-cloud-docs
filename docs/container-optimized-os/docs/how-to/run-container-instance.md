---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-container-instance/
title: Running containers on instances \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:11.021461+00:00
---

# Running containers on instances  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-container-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Running containers on instances Stay organized with collections  Save and categorize content based on your preferences. 

You can run a Docker container on a machine running Container-Optimized OS in much the same way as you would on most other node image distributions, by using the `docker run` command. For example:
    
    
    docker run --rm busybox echo "hello world"

The following output appears:
    
    
    Unable to find image 'busybox:latest' locally
    latest: Pulling from library/busybox
    . . .
    Status: Downloaded newer image for busybox:latest
    hello world
    

When managing SSH keys in metadata, all user accounts managed by Compute Engine on the `cos` image are added to the `docker` group by default. This lets any logged-in user run `docker` commands without root privileges. When managing SSH keys using OS Login, the user account needs to be added to the `docker` group manually. Or else, the user has to add `sudo` for each `docker` command. 

### Accessing public images in Container Registry or Artifact Registry

Container Registry support is built in to the `cos` node image. To start a container from Container Registry, run:
    
    
    docker run --rm gcr.io/google-containers/busybox echo "hello world"

The following output appears:
    
    
    Unable to find image 'gcr.io/google-containers/busybox:latest' locally
    Pulling repository gcr.io/google-containers/busybox
    . . .
    Status: Downloaded newer image for gcr.io/google-containers/busybox:latest
    hello world
    

### Accessing private images in Artifact Registry or Container Registry

Starting with milestone 60 releases, [`docker-credential-gcr`](https://github.com/GoogleCloudPlatform/docker-credential-gcr) is pre-installed in Container-Optimized OS images. It's the recommended way to access private images in Artifact Registry or Container Registry.

To use `docker-credential-gcr`, run the following command:

###  Artifact Registry 
    
    
    docker-credential-gcr configure-docker --registries LOCATION-docker.pkg.dev

Replace LOCATION with the [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository.

###  Container Registry 
    
    
    docker-credential-gcr configure-docker

The following output appears:
    
    
    /home/username/.docker/config.json configured to use this credential helper
    

To run an image from the registry, use the following command:

###  Artifact Registry 
    
    
    docker run --rm LOCATION-docker.pkg.dev/your-project/repository/your-image

Replace LOCATION with the [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository.

###  Container Registry 
    
    
    docker run --rm gcr.io/your-project/your-image

You can use the following Container Registry hostnames:

  * us.gcr.io
  * eu.gcr.io
  * asia.gcr.io



To use docker with `sudo`, run the following command. The `-E` command-line flag makes docker use the `.docker/config.json` file from a user's home directory instead of the root home directory.

###  Artifact Registry 
    
    
    sudo -E docker run --rm LOCATION-docker.pkg.dev/your-project/repository/your-image

Replace LOCATION with the [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository.

###  Container Registry 
    
    
    sudo -E docker run --rm gcr.io/your-project/your-image

Supported Container Registry hostnames are:

  * us.gcr.io
  * eu.gcr.io
  * asia.gcr.io



Alternately, you can fetch appropriate OAuth access tokens from Compute Engine metadata and use them with the `docker login` command manually, as shown in the following example:
    
    
    METADATA=http://metadata.google.internal/computeMetadata/v1
    SVC_ACCT=$METADATA/instance/service-accounts/default
    ACCESS_TOKEN=$(curl -H 'Metadata-Flavor: Google' $SVC_ACCT/token | cut -d'"' -f 4)
    docker login -u oauth2accesstoken -p $ACCESS_TOKEN https://gcr.io
    docker run … gcr.io/your-project/your-image

### Using cloud-init with Container Registry

[This cloud-init example](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init_with_the_cloud_config_format) uses the Cloud Config format to start a Docker container from an image stored in Docker's container registry called [DockerHub](https://hub.docker.com/). The example below uses the Cloud Config format to start a Docker container from an image stored in Container Registry:
    
    
    #cloud-config
    
    write_files:
    - path: /etc/systemd/system/cloudservice.service
      permissions: 0644
      owner: root
      content: |
        [Unit]
        Description=Start a simple docker container
        Wants=gcr-online.target
        After=gcr-online.target
    
        [Service]
        Environment="HOME=/home/cloudservice"
        ExecStartPre=/usr/bin/docker-credential-gcr configure-docker
        ExecStart=/usr/bin/docker run --rm --name=mycloudservice gcr.io/google-containers/busybox:latest /bin/sleep 3600
        ExecStop=/usr/bin/docker stop mycloudservice
        ExecStopPost=/usr/bin/docker rm mycloudservice
    
    runcmd:
    - systemctl daemon-reload
    - systemctl start cloudservice.service
    

**Note:** `docker-credential-gcr` writes credentials to `$HOME/.docker/config.json`. When running `/usr/bin/docker-credential-gcr configure-docker` in a unit file, you must set the environment variable `$HOME`, similar to the example above. Otherwise, `docker-credential-gcr` will try to write credentials to `/root/.docker/config.json`, which is not permitted on Container-Optimized OS.

## Configuring Docker daemon to pull images from registry cache

You can configure Docker daemon to pull images from a registry cache by using registry mirrors.

  1. Configure the daemon to use the `registry-mirror` option in one of the following ways:

     * In the `/etc/default/docker` file, add the `registry-mirror` option for the registry (for example, `https://mirror.gcr.io`):
    
    echo 'DOCKER_OPTS="--registry-mirror=https://mirror.gcr.io"' | tee /etc/default/docker

     * In the `/etc/default/docker` file, append `"--registry-mirror=https://mirror.gcr.io"` to the existing `DOCKER_OPTS`:
    
    sed -i -e 's|"$| --registry-mirror=https://mirror.gcr.io"|' /etc/default/docker

  2. After adding the registry mirror, restart the Docker daemon for the changes to take effect:
         
         sudo systemctl daemon-reload
         sudo systemctl restart docker




Adding a configuration to `/etc/default/docker` is non-persistent across reboot. To ensure that your docker configuration remains persistent across reboots, consider adding the commands either in the `cloud-init` script of the instance's metadata in the [`cloud-config` format](http://cloudinit.readthedocs.io/en/latest/topics/examples.html) or [`startup script`](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#running_startup_scripts).

The following example uses the `cloud-config` format to configure a `registry-mirror`:
    
    
    #cloud-config
    
    runcmd:
    - echo 'DOCKER_OPTS="--registry-mirror=https://mirror.gcr.io"' | tee /etc/default/docker
    - systemctl daemon-reload
    - systemctl restart docker
    

**Note:** For recommendations on handling DockerHub pull request limits in instances running as part of a GKE cluster, see the [Preparing Google Cloud deployments for Docker Hub pull request limits](https://cloud.google.com/blog/products/containers-kubernetes/mitigating-the-impact-of-new-docker-hub-pull-request-limits) blog post.

For more on configuring an instance with `cloud-init`, see [Using cloud-init with the Cloud config format](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init_with_the_cloud_config_format).

## Troubleshooting

### Resolving option conflicts between Docker `daemon.json` and flags

When configuring the Docker daemon, if the same option is set with a `daemon.json` file and with flags, Docker will fail to start with an error similar to:
    
    
    unable to configure the Docker daemon with file /etc/docker/daemon.json:
    the following directives are specified both as a flag and in the configuration file:
    

The recommended solution to resolve this conflict is to modify the default `daemon.json`, which is located at `/etc/docker/daemon.json`. Modifying this file allows for changing only the affected options, while maintaining the other default options. This can be done using `cloud-init`, for example using a `cloud-config` similar to:
    
    
    #cloud-config
    
    write_files:
    - path: /tmp/modify_docker_daemon_opts.py
      permissions: 0744
      owner: root
      content: |
        import json, sys, os, logging
    
        DAEMON_OPTS_FILE = '/etc/docker/daemon.json'
    
        opts = {}
        if os.path.exists(DAEMON_OPTS_FILE):
          with open(DAEMON_OPTS_FILE) as f:
              try:
                opts = json.load(f)
              except:
                logging.info("json parsing failed, starting with empty config.")
                pass
        # Add your daemon option modifications here
        # For example,
        # opts['log-opts']['max-size'] = '100m'
        with open(DAEMON_OPTS_FILE, 'w') as f:
            json.dump(opts, f)
    
    runcmd:
    - python /tmp/modify_docker_daemon_opts.py
    - rm -f /tmp/modify_docker_daemon_opts.py
    - systemctl restart docker.service
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
