---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ContainerOrBuilder
title: Interface Runnable.ContainerOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:14.741997+00:00
---

# Interface Runnable.ContainerOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ContainerOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Runnable.ContainerOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface Runnable.ContainerOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBlockExternalNetwork()
    
    
    public abstract boolean getBlockExternalNetwork()

If set to true, external network access to and from container will be blocked, containers that are with block_external_network as true can still communicate with each other, network cannot be specified in the `container.options` field.

`bool block_external_network = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The blockExternalNetwork.  
  
### getCommands(int index)
    
    
    public abstract String getCommands(int index)

Required for some container images. Overrides the `CMD` specified in the container. If there is an `ENTRYPOINT` (either in the container image or with the `entrypoint` field below) then these commands are appended as arguments to the `ENTRYPOINT`.

`repeated string commands = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The commands at the given index.  
  
### getCommandsBytes(int index)
    
    
    public abstract ByteString getCommandsBytes(int index)

Required for some container images. Overrides the `CMD` specified in the container. If there is an `ENTRYPOINT` (either in the container image or with the `entrypoint` field below) then these commands are appended as arguments to the `ENTRYPOINT`.

`repeated string commands = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the commands at the given index.  
  
### getCommandsCount()
    
    
    public abstract int getCommandsCount()

Required for some container images. Overrides the `CMD` specified in the container. If there is an `ENTRYPOINT` (either in the container image or with the `entrypoint` field below) then these commands are appended as arguments to the `ENTRYPOINT`.

`repeated string commands = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of commands.  
  
### getCommandsList()
    
    
    public abstract List<String> getCommandsList()

Required for some container images. Overrides the `CMD` specified in the container. If there is an `ENTRYPOINT` (either in the container image or with the `entrypoint` field below) then these commands are appended as arguments to the `ENTRYPOINT`.

`repeated string commands = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the commands.  
  
### getEnableImageStreaming()
    
    
    public abstract boolean getEnableImageStreaming()

Optional. If set to true, this container runnable uses Image streaming.

Use Image streaming to allow the runnable to initialize without waiting for the entire container image to download, which can significantly reduce startup time for large container images.

When `enableImageStreaming` is set to true, the container runtime is [containerd](https://containerd.io/) instead of Docker. Additionally, this container runnable only supports the following `container` subfields: `imageUri`, `commands[]`, `entrypoint`, and `volumes[]`; any other `container` subfields are ignored.

For more information about the requirements and limitations for using Image streaming with Batch, see the [`image-streaming` sample on GitHub](https://github.com/GoogleCloudPlatform/batch-samples/tree/main/api-samples/image-streaming).

`bool enable_image_streaming = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableImageStreaming.  
  
### getEntrypoint()
    
    
    public abstract String getEntrypoint()

Required for some container images. Overrides the `ENTRYPOINT` specified in the container.

`string entrypoint = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The entrypoint.  
  
### getEntrypointBytes()
    
    
    public abstract ByteString getEntrypointBytes()

Required for some container images. Overrides the `ENTRYPOINT` specified in the container.

`string entrypoint = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for entrypoint.  
  
### getImageUri()
    
    
    public abstract String getImageUri()

Required. The URI to pull the container image from.

`string image_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imageUri.  
  
### getImageUriBytes()
    
    
    public abstract ByteString getImageUriBytes()

Required. The URI to pull the container image from.

`string image_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imageUri.  
  
### getOptions()
    
    
    public abstract String getOptions()

Required for some container images. Arbitrary additional options to include in the `docker run` command when running this container&mdash;for example, `--network host`. For the `--volume` option, use the `volumes` field for the container.

`string options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The options.  
  
### getOptionsBytes()
    
    
    public abstract ByteString getOptionsBytes()

Required for some container images. Arbitrary additional options to include in the `docker run` command when running this container&mdash;for example, `--network host`. For the `--volume` option, use the `volumes` field for the container.

`string options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for options.  
  
### getPassword()
    
    
    public abstract String getPassword()

Required if the container image is from a private Docker registry. The password to login to the Docker registry that contains the image.

For security, it is strongly recommended to specify an encrypted password by using a Secret Manager secret: `projects/*/secrets/*/versions/*`.

Warning: If you specify the password using plain text, you risk the password being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the password instead.

Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager).

`string password = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The password.  
  
### getPasswordBytes()
    
    
    public abstract ByteString getPasswordBytes()

Required if the container image is from a private Docker registry. The password to login to the Docker registry that contains the image.

For security, it is strongly recommended to specify an encrypted password by using a Secret Manager secret: `projects/*/secrets/*/versions/*`.

Warning: If you specify the password using plain text, you risk the password being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the password instead.

Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager).

`string password = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for password.  
  
### getUsername()
    
    
    public abstract String getUsername()

Required if the container image is from a private Docker registry. The username to login to the Docker registry that contains the image.

You can either specify the username directly by using plain text or specify an encrypted username by using a Secret Manager secret: `projects/*/secrets/*/versions/*`. However, using a secret is recommended for enhanced security.

Caution: If you specify the username using plain text, you risk the username being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the username instead.

Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager).

`string username = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The username.  
  
### getUsernameBytes()
    
    
    public abstract ByteString getUsernameBytes()

Required if the container image is from a private Docker registry. The username to login to the Docker registry that contains the image.

You can either specify the username directly by using plain text or specify an encrypted username by using a Secret Manager secret: `projects/*/secrets/*/versions/*`. However, using a secret is recommended for enhanced security.

Caution: If you specify the username using plain text, you risk the username being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the username instead.

Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager).

`string username = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for username.  
  
### getVolumes(int index)
    
    
    public abstract String getVolumes(int index)

Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match `--volume` option for the `docker run` command&mdash;for example, `/foo:/bar` or `/foo:/bar:ro`.

If the `TaskSpec.Volumes` field is specified but this field is not, Batch will mount each volume from the host machine to the container with the same mount path by default. In this case, the default mount option for containers will be read-only (`ro`) for existing persistent disks and read-write (`rw`) for other volume types, regardless of the original mount options specified in `TaskSpec.Volumes`. If you need different mount settings, you can explicitly configure them in this field.

`repeated string volumes = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The volumes at the given index.  
  
### getVolumesBytes(int index)
    
    
    public abstract ByteString getVolumesBytes(int index)

Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match `--volume` option for the `docker run` command&mdash;for example, `/foo:/bar` or `/foo:/bar:ro`.

If the `TaskSpec.Volumes` field is specified but this field is not, Batch will mount each volume from the host machine to the container with the same mount path by default. In this case, the default mount option for containers will be read-only (`ro`) for existing persistent disks and read-write (`rw`) for other volume types, regardless of the original mount options specified in `TaskSpec.Volumes`. If you need different mount settings, you can explicitly configure them in this field.

`repeated string volumes = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the volumes at the given index.  
  
### getVolumesCount()
    
    
    public abstract int getVolumesCount()

Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match `--volume` option for the `docker run` command&mdash;for example, `/foo:/bar` or `/foo:/bar:ro`.

If the `TaskSpec.Volumes` field is specified but this field is not, Batch will mount each volume from the host machine to the container with the same mount path by default. In this case, the default mount option for containers will be read-only (`ro`) for existing persistent disks and read-write (`rw`) for other volume types, regardless of the original mount options specified in `TaskSpec.Volumes`. If you need different mount settings, you can explicitly configure them in this field.

`repeated string volumes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of volumes.  
  
### getVolumesList()
    
    
    public abstract List<String> getVolumesList()

Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match `--volume` option for the `docker run` command&mdash;for example, `/foo:/bar` or `/foo:/bar:ro`.

If the `TaskSpec.Volumes` field is specified but this field is not, Batch will mount each volume from the host machine to the container with the same mount path by default. In this case, the default mount option for containers will be read-only (`ro`) for existing persistent disks and read-write (`rw`) for other volume types, regardless of the original mount options specified in `TaskSpec.Volumes`. If you need different mount settings, you can explicitly configure them in this field.

`repeated string volumes = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the volumes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
