---
url: https://docs.cloud.google.com/workstations/docs/customize-container-images/
title: Customize container images \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:52.205337+00:00
---

# Customize container images  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/customize-container-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Customize container images Stay organized with collections  Save and categorize content based on your preferences. 

The [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) provided by Cloud Workstations contain only a minimal environment with IDE, basic Linux terminal and language tools and a `sshd` server. To expedite the environment setup of specific development use cases, you can create custom container images that extend these base images to pre-install tools and dependencies and that run automation scripts.

For custom container images, we recommend setting up a pipeline to automatically rebuild these images when the Cloud Workstations base image is updated, in addition to running a container scanning tool such as [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/automated-scanning-howto) to inspect any additional dependencies you added. You're responsible for maintaining and updating custom packages and dependencies added to custom images.

## Before you begin

  1. You need a machine with tooling for building container images such as Docker, and for pushing images to [Artifact Registry](https://docs.cloud.google.com/artifact-registry) using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). You can use Cloud Workstations or Cloud Shell Editor for performing these steps, which have this tooling pre-installed.

  2. Select which base image you want to use from our [list of supported base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images), such as `us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest`.

Alternatively, you can use your own container image or use external container images by following the instructions to [Use your own container image](https://docs.cloud.google.com/workstations/docs/customize-container-images#use_your_own_container_image).

  3. Create a folder such as `CUSTOM_IMAGE_FOLDER` and a Dockerfile inside this folder extending the base image selected, as shown in the examples that follow.




## Cloud Workstations base image structure

Cloud Workstations base images share the following defined structure:

  * The base image entrypoint file is set to `/google/scripts/entrypoint.sh`.
  * On startup, base images run files under `/etc/workstation-startup.d/*` in lexicographical order to initialize the workstation environment.

The files and their behavior are as follows:

    * `000_configure-docker.sh`: Configures and runs Docker inside the workstation.
    * `010_add-user.sh`: Creates the default user in Cloud Workstations.

Because the persistent disk is dynamically attached to the container, users must be added on workstation startup, **not** in the Dockerfile.

    * `020_start-sshd.sh`: Starts the `sshd` service in the container.

    * `030_customize-environment.sh`: Executes `/home/user/.workstation/customize_environment` as `user`.

    * `110_start-$IDE.sh`: Starts the IDE for the image.

  * Cloud Workstations stores Docker images in the home directory at `/home/.docker_data` so that the images are preserved between sessions.




To add additional functionality during workstation startup, add your scripts in the `/etc/workstation-startup.d/` directory:

  * Scripts in this directory run as root by default. To execute the scripts as a different user, use the `runuser` command.

  * Because scripts execute in lexicographical order, we recommended that you prefix the scripts with a three digit number that is greater than 200.




Alternatively, if you don't want to extend a workstations image, you can create a customize_environment script in your home directory.

### Home directory modifications

When the workstation configuration specifies a persistent home directory (which is the default behavior), a persistent disk backing the home directory is dynamically attached to the container at runtime. This process overwrites modifications made to the `/home` directory at container image build time.

To preserve updates, modify the `/home` directory at container runtime by adding a script in the in the `/etc/workstation-startup.d` directory, or by adding per-user configuration in the `/etc/profile.d` directory. To speed up the process, consider running the setup script as a background process (add an ampersand, `&`, to the end of the command) to avoid blocking container startup.

Some examples of build time configuration that should be moved to container runtime:

  * Per-user `git` configuration
  * `git` repositories cloned in the home directory
  * Direct user configuration, such as placing files in a `$HOME/.config` directory
  * User creation



### User creation and modification

Because the persistent disk dynamically attaches to the container at runtime, users must be added on workstation startup, _not_ in the Dockerfile. To modify or create additional users, we recommended that you update `/etc/workstation-startup.d/010_add-user.sh`, or create your own script that executes on startup.

Additionally, you can modify the default bash profile for the users by updating the files in `/etc/profile.d`.

### Update preconfigured Secure APT keys

Cloud Workstations base images come preinstalled with a number of tools obtained from various third-party repositories using Secure APT. As part of the install process, public keys provided by the repository owners are imported using `gpg` and placed into individual files under `/usr/share/keyrings/`. These files are referenced from corresponding `list` files under `/etc/apt/sources.list.d/`. This enables `apt` to verify the integrity of the a given repository when interacting with it.

On occasion, third-party repository owners may decide to change the public key used to validate the integrity of their repository, which causes `apt` to display an error when interacting with it. To resolve this potential problem, you can use `/google/scripts/refresh-preinstalled-apt-keys.sh`, which obtains the latest versions of preinstalled public keys and re-imports them.

You can also run this script directly in your custom `Dockerfile` before you run `apt-get update`:
    
    
    # Refresh the preinstalled APT keys
    RUN /google/scripts/refresh-preinstalled-apt-keys.sh
    
    RUN apt-get update
    

### List installed IDE versions

Several Cloud Workstations base images come preinstalled with an IDE. For convenience, see the included `/google/scripts/preinstalled-ide-versions.sh` script, which lists the name and version information of IDEs installed in the image.

### Turn off `sudo` root privileges

The default workstation user has `sudo` root access privileges in these containers. To turn off root access to the Docker container, set the `CLOUD_WORKSTATIONS_CONFIG_DISABLE_SUDO` environment variable to `true` when creating the workstation configuration.

To set this environment variable through the Google Cloud console when creating your workstation configuration, follow these steps:

  1. When creating your workstation configuration, complete the configuration for Basic information and the Machine configuration.
  2. On the **Environment customization** dialog, expand the **Advanced container options** section and select **Environment variables**.
  3. Click add**Add variable**.
  4. Enter `CLOUD_WORKSTATIONS_CONFIG_DISABLE_SUDO` and `true` as the value.

**Note:** If a user is able to break out of the Docker container, they might be able to obtain root privileges on the underlying VM.

### Customize without extending an image

For convenience all Cloud Workstations base images check for the presence of an executable file located at `/home/user/.workstation/customize_environment` and, if it exists, run it in the background as `user`. This lets you run any script or binary at startup. Unlike `.profile` or `.bashrc` the script only runs once when the workstation starts, rather than once for each shell login.

Because the `customize_environment` script runs as `user`, be sure to update permissions as necessary when writing your script. For example, if you want to install Emacs everytime your workstation starts, the content of `customize_environment` might be similar to the following:
    
    
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y emacs
    

Execution logs for `customize_environment` can be found in the container at `/var/log/customize_environment` and are also written to the [container output logs](https://docs.cloud.google.com/workstations/docs/container-output-logging). On successful execution of `customize_environment`, a file is created in `/var/run/customize_environment_done`. Because `customize_environment` runs in parallel with Workstation startup, packages installed by the script can be available as early as a few moments after your workstation has started.

### Prevent idle timeouts

For convenience, all Cloud Workstations base images include a preinstalled script at `/google/scripts/keep_alive.sh`. This script sends regular keep-alive messages, which can prevent the workstation from shutting down due to idle timeouts when you are running background processes without direct interaction.

#### Prevent idle timeouts with AI agents

In addition, Cloud Workstations base images include sample agent configuration scripts under `/google/samples/agents/keepalive/`. These sample configurations let you configure AI coding agents (such as Claude Code and Antigravity CLI) inside the workstation to automatically keep the workstation alive while they are actively working on tasks. When the agent finishes its tasks or pauses to wait for user input, the script stops sending keep-alive messages, allowing the workstation to time out due to inactivity. These configurations work best when the workstation configuration is set to use workstation suspension (`idleAction` set to `SUSPEND`), allowing the workstation to save memory state and resume seamlessly when you return.

For more information on setting up agent-assisted workflows and keep-alive hooks, see [Agent-optimized development](https://docs.cloud.google.com/workstations/docs/agent-optimized-development).

## Use your own container image

You can also use your own container image or use external container images, as long as they are Linux-based and run a blocking process when the container starts up.

When setting up the Dockerfile, the `ENTRYPOINT` instruction must run a blocking process such as `sleep infinity` so that the container continues to run, rather than immediately exit. Alternatively, in the workstation configuration you can set the `config.container.args` field to specify a blocking process.

When using your own container image, note the following:

  * Cloud Workstations does not require additional scripts from the Cloud Workstations base image.

You can, however, look at the scripts in the `/etc/workstation-startup.d/` directory within a container running the Cloud Workstations base image. The filenames indicate what each script does.

  * We recommend that you run an SSH server in the container. Refer to `/etc/workstation-startup.d/020_start-sshd.sh` in the default [base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) to learn how Cloud Workstations sets this up by default.

  * We recommend that you run your default IDE or web server on port `80`.




Google Cloud provides [standard base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images) that you can use to build a fully custom container image.

## Extend Cloud Workstations base images

When extending a Cloud Workstations base image to create a custom image for your workstation environment, you can take three approaches:

  1. Update your `Dockerfile` to include any additional static assets that you want to add.
  2. Add additional executable files under `/etc/workstation-startup.d/` to customize the running container. Files under this directory automatically run in lexicographical order at container startup, so you can prefix your filename to run it at the appropriate time during workstation startup.
  3. Override the `ENTRYPOINT` in your Dockerfile to fully customize your container startup.

**Note:** Any user modification must be done at container runtime, not in the Dockerfile. This is because `/home` is dynamically mounted into the container at startup time.

## Sample custom Dockerfiles

This section provides example scenarios and instructions for creating your own Dockerfiles.

### Container image with `emacs` pre-installed

To create a container image with `emacs` pre-installed, run the following commands:
    
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
    
    RUN sudo apt update
    RUN sudo apt install -y emacs
    

### Container image with user customization

Follow these steps to customize a container image:

  1. Create a script in `/etc/workstation-startup.d/*` that runs after `010_add-user.sh`—for example, `011_customize-user.sh`:
         
         #!/bin/bash
         # Create new group
         groupadd $GROUP
         # Add the user to a new group
         usermod -a -G $GROUP $USERNAME
         

Replace `$GROUP` with the new group name and `$USERNAME` with the user's username.

  2. Assuming that you named your script, `011_customize-user.sh`, add the following to your image in your Dockerfile and make it executable:
         
         FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
         
         COPY 011_customize-user.sh /etc/workstation-startup.d/
         
         RUN chmod +x /etc/workstation-startup.d/011_customize-user.sh
         




### Container image that sets container environment variables in SSH sessions

Environment variables set at the workstation configuration or workstation level are passed to direct subprocesses using the entrypoint command. This includes the IDE in the preconfigured base images. However, SSH sessions are not child processes of the entrypoint, and don't have these custom environment variables set.

To set those environment variables in the SSH sessions, setup a custom container image that relays these environment variables from the container's entrypoint command to the `/etc/environment` file.

To accomplish that, follow these steps:

  1. Create a script in `/etc/workstation-startup.d/*` that runs after `010_add-user.sh`—for example, `011_add-ssh-env-variables.sh`:
         
         #!/bin/bash
         #
         echo "CUSTOM_ENV_VAR=$CUSTOM_ENV_VAR" >> /etc/environment
         

Replace `CUSTOM_ENV_VAR` with the intended environment variable name.

  2. Assuming that you named your script, `011_add-ssh-env-variables.sh`, add the following to your image in your Dockerfile and make it executable:
         
         FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
         
         COPY 011_add-ssh-env-variables.sh /etc/workstation-startup.d/
         
         RUN chmod +x /etc/workstation-startup.d/011_add-ssh-env-variables.sh
         




### Container image that enables X11 forwarding for SSH sessions

X11 forwarding lets you start remote applications and forward the application display to a local machine.

To create a container image that enables X11 forwarding, modify the OpenSSH daemon configuration file (`/etc/ssh/sshd_config`) provided by the Cloud Workstations base images by appending `X11Forwarding yes` (to permit X11 forwarding) and `AddressFamily inet` (to ensure that only IPv4 is used). For more information about these keywords, see the OpenBSD web pages about [`AddressFamily`](https://man.openbsd.org/sshd_config.5#AddressFamily) and [`X11Forwarding`](https://man.openbsd.org/sshd_config.5#X11Forwarding).

Here's a sample Dockerfile, which makes the necessary modifications:
    
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
    
    # Permit X11 forwarding using only IPv4
    RUN cat >> /etc/ssh/sshd_config <<-EOF
    
    AddressFamily inet
    X11Forwarding yes
    EOF
    

### Copy Code OSS for Cloud Workstations into another container image

A multi-stage build lets you use multiple `FROM` statements in your Dockerfile. Each `FROM` instruction can use a different base, and enables copying artifacts between build stages. To add Code OSS for Cloud Workstations to another container image use a multi-stage build to copy the application folder `/opt/code-oss` into your image. If you want to start Code OSS for Cloud Workstations at container startup time, additionally copy the script `/etc/workstation-startup.d/110_start-code-oss.sh` into your container.

Here's a sample Dockerfile which copies Code OSS into the JetBrains IntelliJ Ultimate image. You can then interact with either IDE:
    
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest as code-oss-image
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/jetbrains-intellij:latest
    
    # Copy Code OSS for Cloud Workstations and startup scripts into our custom image
    COPY --from=code-oss-image /opt/code-oss /opt/code-oss
    COPY --from=code-oss-image /etc/workstation-startup.d/110_start-code-oss.sh /etc/workstation-startup.d/110_start-code-oss.sh
    
    # Use the existing entrypoint script which will execute all scripts in /etc/workstation-startup.d/
    ENTRYPOINT ["/google/scripts/entrypoint.sh"]
    

### Container image that pre-installs IDE extensions in Code OSS for Cloud Workstations for Java development

To create a container image that pre-installs IDE extensions in Code OSS for Cloud Workstations for Java development at build time, run the following commands:
    
    
    FROM us-central1-docker.pkg.dev/cloud-workstations-images/predefined/code-oss:latest
    
    RUN wget https://open-vsx.org/api/vscjava/vscode-java-debug/0.40.1/file/vscjava.vscode-java-debug-0.40.1.vsix && \
    unzip vscjava.vscode-java-debug-0.40.1.vsix "extension/*" &&\
    mv extension /opt/code-oss/extensions/java-debug
    
    RUN wget https://open-vsx.org/api/vscjava/vscode-java-dependency/0.19.1/file/vscjava.vscode-java-dependency-0.19.1.vsix && \
    unzip vscjava.vscode-java-dependency-0.19.1.vsix "extension/*" &&\
    mv extension /opt/code-oss/extensions/java-dependency
    
    RUN wget https://open-vsx.org/api/redhat/java/1.6.0/file/redhat.java-1.6.0.vsix && \
    unzip redhat.java-1.6.0.vsix "extension/*" &&\
    mv extension /opt/code-oss/extensions/redhat-java
    
    RUN wget https://open-vsx.org/api/vscjava/vscode-maven/0.35.2/file/vscjava.vscode-maven-0.35.2.vsix && \
    unzip vscjava.vscode-maven-0.35.2.vsix "extension/*" &&\
    mv extension /opt/code-oss/extensions/java-maven
    
    RUN wget https://open-vsx.org/api/vscjava/vscode-java-test/0.35.0/file/vscjava.vscode-java-test-0.35.0.vsix && \
    unzip vscjava.vscode-java-test-0.35.0.vsix "extension/*" &&\
    mv extension /opt/code-oss/extensions/java-test
    
    RUN chmod a+rwx -R /opt/code-oss/extensions/
    

If you pre-install extensions, they are considered built-in extensions. You won't be able to update these extensions and they might not appear in the installed section on the ![](https://docs.cloud.google.com/static/workstations/images/extensions-icon.svg)[Extensions Marketplace](https://docs.cloud.google.com/workstations/docs/extensions-marketplace). However, you can find your built-in extensions by searching for `@builtin`.

Another way to install extensions at startup is to run a [startup script](https://docs.cloud.google.com/workstations/docs/customize-container-images#cloud-workstations-base-image-structure). For example, include the following startup script under `/etc/workstation-startup.d/120_install_extensions.sh`:
    
    
    sudo -u user /opt/code-oss/bin/codeoss-cloudworkstations --install-extension vscjava.vscode-java-debug@0.40.1 \
    --install-extension vscjava.vscode-java-dependency@0.19.1  \
    --install-extension redhat.java@1.6.0 \
    --install-extension vscjava.vscode-maven@0.35.2 \
    --install-extension vscjava.vscode-java-test@0.35.0
    

Using this method, the extension appears on ![](https://docs.cloud.google.com/static/workstations/images/extensions-icon.svg) the [Extensions Marketplace](https://docs.cloud.google.com/workstations/docs/extensions-marketplace) and you can update from there.

**Note:** You can also pre-download your VSIX files at build time and use them at runtime for added protection and to improve startup performance.

### Install JetBrains IDEs and plugins into base images

When customizing Docker images for workstation configurations, you can install JetBrains IDEs and plugins, such as [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/features), into the base image. Cloud Workstations base images for JetBrains products include the following scripts to help you:

  * `jetbrains-installer.sh`: install JetBrains IDEs
  * `plugin-installer.sh`: install plugins, such as Cloud Code for IntelliJ



Use these scripts as needed to customize the base image, to call them with a startup script, or to run them after starting the workstation.

#### Installer scripts

To view the source files for the `jetbrains-installer.sh` and `plugin-installer.sh` scripts, start a workstation using a workstation configuration that uses one of the JetBrains predefined images, connect to the workstation either through JetBrains Gateway or through SSH, and then browse the script files in the `installer-scripts` directory, which is located in the root directory.

We recommend that you run these scripts at container build time. Avoid running them in an already started workstation.

#### Use the plugin installer script

The `plugin-installer.sh` script uses the following syntax:
    
    
    plugin-installer.sh [-v VERSION] [-d DESTINATION-DIRECTORY] [-c CHECKSUM] [-f] PLUGIN_ID
    

Replace the following:

  * `VERSION`: optional version number of the plugin to install.
  * `DESTINATION-DIRECTORY`: optional directory into which the plugin should be installed. If unspecified, the working directory is used.
  * `CHECKSUM`: optional SHA-256 checksum of the requested plugin.
  * `-f`: if specified any existing plugin will be overwritten.
  * `PLUGIN_ID`: the required numeric plugin identifier from the JetBrains marketplace. For example, to add [Dart](https://plugins.jetbrains.com/plugin/6351-dart) use `6351` as the PLUGIN_ID. To add [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/features) use `8079` as the PLUGIN_ID.



For example, to install the latest version of the Dart plugin in IntelliJ run the following command:
    
    
    /installer-scripts/plugin-installer.sh -d /opt/ideaIU/plugins/ 6351
    

#### Use the JetBrains installer script

We recommended that you use the JetBrains installer script when extending a preconfigured base image for JetBrains IDEs.

The `jetbrains-installer.sh` script uses the following syntax:
    
    
    jetbrains-installer.sh IDE [ pinned|latest ]
    

Replace the following:

  * `IDE`: the JetBrains IDE to install. You must use one of the following IDE abbreviations:

IDE | Product Installed  
---|---  
`cl` | CLion  
`clion` | CLion  
`go` | GoLand  
`goland` | GoLand  
`iiu` | Intellij Ultimate  
`intellij` | Intellij Ultimate  
`pcp` | PyCharm Professional  
`pycharm` | PyCharm Professional  
`ps` | PHPStorm  
`phpstorm` | PHPStorm  
`rd` | Rider  
`rider` | Rider  
`rm` | RubyMine  
`rubymine` | RubyMine  
`ws` | WebStorm  
`webstorm` | WebStorm  
  * `pinned|latest`: Optional - Use either the pinned or latest version of the IDE. Defaults to `latest`.




For example, to install the latest version of the Clion, run the following command:
    
    
    /installer-scripts/jetbrains-installer.sh clion
    

#### Customize JetBrains IDE configuration files

If a persistent home directory is specified in the workstations configuration, Cloud Workstations base images with JetBrains IDEs automatically persist the `$IDE.vmoptions` and `$IDE.properties` configuration files. To override the default location of these files, specify the `CLOUD_WORKSTATIONS_JETBRAINS_PERISTED_CONFIG_DIR` environment variable.

For more information, Refer to `/etc/workstation-startup.d/120_persist-jetbrains-configs.sh` in any [JetBrains base image](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) to learn how Cloud Workstations sets this up by default.

#### Extend a base Docker image with Cloud Code for IntelliJ

The following Dockerfile snippet extends a base Docker image with Cloud Code for IntelliJ by including `8079` as the required plugin identifier. The example also optionally specifies `version 22.9.3-222` as the version number, `/opt/ideaIU/plugins/` as the destination directory, and `89628279ed9042c526a81facc09bf53f8fb8b83b4595b0d329d94c1611e0c379` as the checksum:
    
    
    ...
    # Install IDE and Plugins
    RUN bash /installer-scripts/jetbrains-installer.sh intellij pinned && \
      # Install Cloud Code - https://plugins.jetbrains.com/plugin/8079-cloud-code
      bash /installer-scripts/plugin-installer.sh \
          -v 22.9.3-222 \
          -d /opt/ideaIU/plugins/ \
          -c 89628279ed9042c526a81facc09bf53f8fb8b83b4595b0d329d94c1611e0c379 \
          8079
    
    # Register IDE with JetBrains Gateway
    RUN echo 'runuser user -c "/opt/ideaIU/bin/remote-dev-server.sh registerBackendLocationForGateway"' > /etc/workstation-startup.d/110_register-intellij-with-gateway.sh \
        echo 'echo "IntelliJ-Ultimate ready for incoming gateway connection"' >> /etc/workstation-startup.d/110_register-intellij-with-gateway.sh
    ...
    

## Install additional IDE extensions in Code OSS for Cloud Workstations

Find additional IDE extensions on the [Open VSX Registry](https://open-vsx.org). You can also find the URL of the `.vsix` file by copying the URL from the **Download** link for any extension.

![Open VSX page for the Go language extension that shows the Download button.](https://docs.cloud.google.com/static/workstations/images/open-vsx-go-ext-dark-mode.png)

If you open the ![](https://docs.cloud.google.com/static/workstations/images/extensions-icon.svg)[Extensions Marketplace](https://docs.cloud.google.com/workstations/docs/extensions-marketplace) from a workstation, **Install** appears instead of **Download**.

## Default Code OSS for Cloud Workstations settings

For detailed information about storage of settings in Code OSS for Cloud Workstations, see [Customize settings](https://docs.cloud.google.com/workstations/docs/base-editor-overview#customize_settings).

If you specify a persistent home directory in the workstations configuration, you can configure default settings for Code OSS for Cloud Workstations by adding a [startup script](https://docs.cloud.google.com/workstations/docs/customize-container-images#cloud-workstations-base-image-structure) that writes settings to `$HOME/.codeoss-cloudworkstations/data/Machine/settings.json`.

For example, if you want to set the default color theme to Dark, extend the base editor image to include the following script under `/etc/workstation-startup.d/150_default-ide-color-theme.sh`
    
    
    cat <<< $(jq '. += {"workbench.colorTheme": "Default Dark Modern"}' settings.json) > settings.json
    

## Build a custom container image

For detailed information about Docker commands, see the [Docker reference](https://docs.docker.com/engine/reference/commandline/build/). Enter the following command to build your container:
    
    
    docker build CUSTOM_IMAGE_FOLDER -t TARGET_IMAGE
    

Note that replacing the text that precedes the edit **Edit** icon updates the other examples on this page.

Replace the following:

  * `CUSTOM_IMAGE_FOLDER`: the path to the folder that you created to store your custom image.
  * `TARGET_IMAGE`: the path to your image in Artifact Registry.

For example, `TARGET_IMAGE` might point to a target image path similar the following path:
        
        *.pkg.dev/cloud-workstations-external/customimage:latest
        

Replace * as needed with the name of the region and any additional identifiers.




You can also update the `CLOUD_WORKSTATIONS_CUSTOM_IMAGE` environment variable to point to the repository.

For more information about storing Docker images in Artifact Registry, see the following sections:

  * How to [Create a Docker repository with Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create).
  * Naming conventions for [repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names).



## Host your custom container image

To host custom container images, we recommend and support Artifact Registry. If you use GitHub or any other public or private repository, Cloud Workstations might not work as expected. For more information, see the important note in the [Use a custom container image](https://docs.cloud.google.com/workstations/docs/customize-container-images#use_a_custom_container_image) section.

## Test your custom container image

After your container finishes building, you can test it with the following command:
    
    
    docker run --privileged -p LOCAL_PORT:CONTAINER_PORT TARGET_IMAGE
    

Replace the following:

  * `LOCAL_PORT`: the local port number
  * `CONTAINER_PORT`: the container port number



For example, replacing `LOCAL_PORT`:`CONTAINER_PORT` with `8080`:`80` assigns port `8080` for use locally and port `80` for use in the container.

If you're extending the Cloud Workstations base editor image, run the `docker` command and then test the workstation image by connecting to the workstation through your local browser or by running `ssh` to connect to your container:

  * If you connect through your browser, make sure that you pass `-p 8080:80` to your `docker run` command and then open [`localhost:8080`](http://localhost:8080/). 
  * If you prefer to connect through SSH, make sure that you pass `-p 2222:22` to your `docker run` command and then run `ssh user@localhost -p 2222`.



## Use a custom container image

To use your custom container image after you have built and tested it locally, push your container to Artifact Registry with the following command:
    
    
    docker push TARGET_IMAGE
    

You can now [create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-workstation) using the container image you just created and pushed.

**Important:** If your image is hosted in a private repository, be sure that your workstation configuration also specifies a [service account](https://docs.cloud.google.com/workstations/docs/customize-development-environment#gceinstance) that has pull permissions on the repository.

For more information, see [Create a Docker repository with Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images#create).

## Debug issues

To find and debug issues running your container image, review the [container output logs](https://docs.cloud.google.com/workstations/docs/container-output-logging) from your running workstations.

## Recommended: help secure your image pipeline

You're responsible for maintaining and updating custom packages and dependencies added on custom images.

If you're creating custom images, we recommend the following:

  * Run a container scanning tool such as [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) to inspect any additional dependencies you added.

  * [Schedule builds](https://docs.cloud.google.com/build/docs/schedule-builds) to rebuild images weekly, or learn how to [automate container image rebuilds](https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild).




## What's next

  * [Automate container image rebuilds](https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild) to synchronize base image updates using Cloud Build and Cloud Scheduler.
  * [Set up security best practices](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices).
  * Learn more about [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/automated-scanning-howto).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
