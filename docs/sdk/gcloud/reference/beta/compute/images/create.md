---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/create/
title: gcloud beta compute images create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:47:42.436614+00:00
---

# gcloud beta compute images create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute images create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute images create - create Compute Engine images 
SYNOPSIS
    

`gcloud beta compute images create` `IMAGE_NAME` (`--source-disk`=`SOURCE_DISK` | `--source-image`=`SOURCE_IMAGE` | `--source-image-family`=`SOURCE_IMAGE_FAMILY` | `--source-snapshot`=`SOURCE_SNAPSHOT` | `--source-uri`=`SOURCE_URI`) [`--architecture`=`ARCHITECTURE`] [`--csek-key-file`=`FILE`] [`--description`=`DESCRIPTION`] [`--family`=`FAMILY`] [`--forbidden-database-file`=[`DBX_VALUE`,…]] [`--force`] [`--force-create`] [`--guest-os-features`=[`GUEST_OS_FEATURE`,…]] [`--key-exchange-key-file`=[`KEK_VALUE`,…]] [`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`] [`--labels`=[`KEY`=`VALUE`,…]] [`--licenses`=[`LICENSES`,…]] [`--platform-key-file`=`PLATFORM_KEY_FILE`] [`--no-require-csek-key-create`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--signature-database-file`=[`DB_VALUE`,…]] [`--source-disk-project`=`SOURCE_DISK_PROJECT`] [`--source-disk-zone`=`SOURCE_DISK_ZONE`] [`--source-image-project`=`SOURCE_IMAGE_PROJECT`] [`--storage-location`=`LOCATION`] [`--user-licenses`=[`LICENSE`,…]] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute images create` is used to create custom disk images. The resulting image can be provided during instance or disk creation so that the instance attached to the resulting disks has access to a known set of software or files from the image. 

Images can be created from gzipped compressed tarball containing raw disk data, existing disks in any zone, existing images, and existing snapshots inside the same project. 

Images are global resources, so they can be used across zones and projects. 

To learn more about creating image tarballs, visit <https://cloud.google.com/compute/docs/creating-custom-image>. 

EXAMPLES
     To create an image 'my-image' from a disk 'my-disk' in zone 'us-east1-a', run: 
    
    
    gcloud beta compute images create my-image --source-disk=my-disk --source-disk-zone=us-east1-a

To create an image 'my-image' from a disk 'my-disk' in zone 'us-east1-a' with source disk project 'source-disk-project' run: 
    
    
    gcloud beta compute images create my-image --source-disk=my-disk --source-disk-zone=us-east1-a --source-disk-project=source-disk-project

To create an image 'my-image' from another image 'source-image' with source image project 'source-image-project', run: 
    
    
    gcloud beta compute images create my-image --source-image=source-image --source-image-project=source-image-project

To create an image 'my-image' from the latest non-deprecated image in the family 'source-image-family' with source image project 'source-image-project', run: 
    
    
    gcloud beta compute images create my-image --source-image-family=source-image-family --source-image-project=source-image-project

To create an image 'my-image' from a snapshot 'source-snapshot', run: 
    
    
    gcloud beta compute images create my-image --source-snapshot=source-snapshot

POSITIONAL ARGUMENTS
    

`IMAGE_NAME`
     Name of the disk image to create. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--source-disk`=`SOURCE_DISK`
     A source disk to create the image from. The value for this option can be the name of a disk with the zone specified via ``\--source-disk-zone`` flag. 
`--source-image`=`SOURCE_IMAGE`
     The name of an image to clone. May be used with ``\--source-image-project`` to clone an image in a different project. 
`--source-image-family`=`SOURCE_IMAGE_FAMILY`
     The family of the source image. This will cause the latest non- deprecated image in the family to be used as the source image. May be used with ``\--source-image-project`` to refer to an image family in a different project. 
`--source-snapshot`=`SOURCE_SNAPSHOT`
     A source snapshot to create the image from. The value for this option can be the name of a snapshot within the same project as the destination image. 
`--source-uri`=`SOURCE_URI`
     The full Cloud Storage URI or Artifact Registry path where the raw disk image archive is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or a valid Artifact Registry generic repository path. For more information about Cloud Storage URIs, see <https://cloud.google.com/storage/docs/request-endpoints#json-api>. If an Artifact Registry path is provided, it must be a valid Artifact Registry generic repository path in the format: projects/<project>/locations/<locations>/repositories/<repo>/packages/<package>/versions/<version_id> or projects/<project>/locations/<locations>/repositories/<repo>/packages/<package>/versions/<version_id>@dirsum_sha256:<hex_value>
OPTIONAL FLAGS
    

`--architecture`=`ARCHITECTURE`
     Specifies the architecture or processor type that this image can support. For available processor types on Compute Engine, see <https://cloud.google.com/compute/docs/cpu-platforms>. `ARCHITECTURE` must be one of: `ARM64`, `X86_64`. 
`--csek-key-file`=`FILE`
     (DEPRECATED) Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute Engine images to user managed keys to be used when creating, mounting, or taking snapshots of disks. 
    
    
    If you pass `-` as value of the flag, the CSEK is read from stdin.
    See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details.

The --csek-key-file flag is deprecated. 

`--description`=`DESCRIPTION`
     An optional, textual description for the image being created. 
`--family`=`FAMILY`
     The family of the image. When creating an instance or disk, specifying a family will cause the latest non-deprecated image in the family to be used. 
`--forbidden-database-file`=[`DBX_VALUE`,…]
     Comma-separated list of file paths that point to revoked X.509 certificates in DER format or raw binary files. When you create a Shielded VM instance from this image, these certificates or files are added to the forbidden signature database (dbx). 
`--force`
     By default, image creation fails when it is created from a disk that is attached to a running instance. When this flag is used, image creation from disk will proceed even if the disk is in use. 
`--force-create`
     (DEPRECATED) DEPRECATED, use --force instead. By default, image creation fails when it is created from a disk that is attached to a running instance. When this flag is used, image creation from disk will proceed even if the disk is in use. 

Flag force-create is deprecated. Use --force instead. 

`--guest-os-features`=[`GUEST_OS_FEATURE`,…]
     Enables one or more features for VM instances that use the image for their boot disks. See the descriptions of supported features at: <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features>. `GUEST_OS_FEATURE` must be one of: `BARE_METAL_LINUX_COMPATIBLE`, `BMSAI_CAPABLE`, `CCA_CAPABLE`, `GVNIC`, `IDPF`, `MULTI_IP_SUBNET`, `SEV_CAPABLE`, `SEV_LIVE_MIGRATABLE`, `SEV_LIVE_MIGRATABLE_V2`, `SEV_SNP_CAPABLE`, `SNP_SVSM_CAPABLE`, `SUSPEND_SAFE_FPR`, `TDX_CAPABLE`, `UEFI_COMPATIBLE`, `VIRTIO_SCSI_MULTIQUEUE`, `WINDOWS`. 
`--key-exchange-key-file`=[`KEK_VALUE`,…]
     Comma-separated list of file paths that point to X.509 certificates in DER format or raw binary files. When you create a Shielded VM instance from this image, these certificates or files are used as key exchange keys (KEK). 
`--kms-key-service-account`=`KMS_KEY_SERVICE_ACCOUNT`
     Service account being used for the encryption request for the given KMS key. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--licenses`=[`LICENSES`,…]
     Comma-separated list of URIs to license resources. 
`--platform-key-file`=`PLATFORM_KEY_FILE`
     File path that points to an X.509 certificate in DER format or raw binary file. When you create a Shielded VM instance from this image, this certificate or raw binary file is used as the platform key (PK). 
`--require-csek-key-create`
     (DEPRECATED) Refuse to create images not protected by a user managed key in the key file when --csek-key-file is given. This behavior is enabled by default to prevent incorrect gcloud invocations from accidentally creating images with no user managed key. Disabling the check allows creation of some images without a matching Customer-Supplied Encryption Key in the supplied --csek-key-file. See <https://cloud.google.com/compute/docs/disks/customer-supplied-encryption> for more details. 

The --require-csek-key-create flag is deprecated. Enabled by default, use `--no-require-csek-key-create` to disable. 

`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the image. 
`--signature-database-file`=[`DB_VALUE`,…]
     Comma-separated list of file paths that point to valid X.509 certificates in DER format or raw binary files. When you create a Shielded VM instance from this image, these certificates or files are added to the signature database (db). 
`--source-disk-project`=`SOURCE_DISK_PROJECT`
     Project name of the source disk. Must also specify --source-disk when using this flag. 
`--source-disk-zone`=`SOURCE_DISK_ZONE`
     Zone of the source disk to operate on. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--source-image-project`=`SOURCE_IMAGE_PROJECT`
     The project name of the source image. Must also specify either ``\--source-image`` or ``\--source-image-family`` when using this flag. 
`--storage-location`=`LOCATION`
     Specifies a Cloud Storage location, either regional or multi-regional, where image content is to be stored. If not specified, the multi-region location closest to the source is chosen automatically. 
`--user-licenses`=[`LICENSE`,…]
     (REMOVED) URI for the license resource. For multiple licenses, you can provide a comma-separated list of URIs. 

The --user-licenses flag has been removed. Use --licenses instead. 

Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the image. The 'Compute Engine Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute images create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create)
    
    
    [gcloud alpha compute images create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images/create)
    
    
    [gcloud preview compute images create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
