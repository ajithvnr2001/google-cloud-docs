---
url: https://docs.cloud.google.com/run/docs/using-smb/
title: Using the CIFS/SMB network file system \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:22.566837+00:00
---

# Using the CIFS/SMB network file system  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/using-smb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using the CIFS/SMB network file system Stay organized with collections  Save and categorize content based on your preferences. 

This page describes using the CIFS/SMB network file systems with Cloud Run.

If you are using NFS, Filestore, or Cloud Storage FUSE on Cloud Run, refer to the following pages:

  * NFS volume configuration for [services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/nfs-volume-mounts), or [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/nfs-volume-mounts).
  * Cloud Storage volume configuration for [services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts), or [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/cloud-storage-volume-mounts).



## Limitations

  * You must specify the [second generation execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments) when using `smbnetfs`.

  * Due to the Cloud Run execution environment restriction, CIFS/SMB can't be directly mounted inside Cloud Run. However, you can use SMB clients that don't rely on kernel mounting, like `smbnetfs` (FUSE-based) or `smbclient`.

  * Cloud Run is designed to scale rapidly to a large number of instances. However, most network file systems are not designed for concurrent use by a large number of clients. For Cloud Run services, consider using the [maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) feature to limit the number of Cloud Run instances.




## Using `smbnetfs`

`smbnetfs` is a FUSE-based file system that lets you mount SMB shares as part of the local file system hierarchy.

To use `smbnetfs` with Cloud Run, update your Dockerfile to install `smbnetfs` and its dependencies, and configure credentials.

### Configure `smbnetfs` in Dockerfile

Add the following instructions to your Dockerfile:

**Warning:** For production environments, we recommended using Secret Manager to handle credentials securely. The following example places credentials directly in the Dockerfile for simplicity. For production use, mount secrets as files or environment variables. Learn more about [configuring secrets in Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets).
    
    
    # Install smbnetfs, fuse and other dependencies
    RUN apt-get update && apt-get install -y smbnetfs fuse && rm -rf /var/lib/apt/lists/*
    
    # Setup smbnetfs configuration
    RUN mkdir -p ~/.smb
    # Check if files exist before copying, as strict locations might vary or be missing in minimal images
    RUN [ -f /etc/smbnetfs.conf ] && cp /etc/smbnetfs.conf ~/.smb/ || echo "smbnetfs.conf not found"
    
    # Create the auth file
    # In production, use mechanisms like [Secret Manager](/run/docs/configuring/services/secrets) to handle credentials
    # securely instead of placing them directly in the Dockerfile.
    RUN echo 'auth "<smb-server-ip>" "<smb-username>" "<smb-password>"' > ~/.smb/smbnetfs.auth
    RUN chmod 600 ~/.smb/smbnetfs.auth
    
    # Create the host file
    RUN echo 'host <smb-server-ip> visible=true' > ~/.smb/smbnetfs.host
    RUN chmod 600 ~/.smb/smbnetfs.host
    
    # Enable the includes in the main config if they exist
    RUN if [ -f ~/.smb/smbnetfs.conf ]; then \
        sed -i 's/^#include "smbnetfs.auth"/include "smbnetfs.auth"/' ~/.smb/smbnetfs.conf && \
        sed -i 's/^#include "smbnetfs.host"/include "smbnetfs.host"/' ~/.smb/smbnetfs.conf; \
        fi
    

Replace `<smb-server-ip>`, `<smb-username>`, and `<smb-password>` with connection details for your SMB server.

### Mount the SMB share during container startup

Run smbnetfs to mount the share when your container starts and before your application starts. If your container runs as a non-root user, you might need to adjust permissions or FUSE configuration.

  1. Create a mount point such as `/mnt/smb` as shown in the following command: 
         
         mkdir /mnt/smb

  2. Mount the SMB file system by using the `smbnetfs` command: 
         
         smbnetfs /mnt/smb

  3. Access your share under `/mnt/smb/<smb-server-ip>/<share-name>`, as shown in the following command: 
         
         ls /mnt/smb/smb-server-ip/share-name




### Troubleshooting

You might encounter input/output errors when writing to files using the `O_APPEND` flag with `smbnetfs`. Find more details in the [Stack Overflow discussion](https://stackoverflow.com/questions/73104395/smbnetfs-how-to-resolve-input-output-error-while-writing-file-to-windows-serve).

## Using smbclient

`smbclient` is a command-line tool that provides an FTP-like interface for accessing SMB shares. You can use it to transfer files or run commands on an SMB server.

  * To avoid providing credentials with each command, you can store them in a file.

**Warning:** In production, ensure that this file is managed securely, for example, by injecting it during container startup using [Secret Manager](https://docs.cloud.google.com/run/docs/configuring/services/secrets).
    1. Store your credentials in a file, for example, `smb-cred.txt`:
           
           username = <smb-username>
           password = <smb-password>
           

    2. As an alternative to a credentials file, you can provide credentials with each command using the `-U` or `--user` option, for example: `--user=[DOMAIN\]USERNAME[%PASSWORD]`.

    3. Use the `smbclient` tool with the `-A` flag to specify the credentials file. For example, to list files in a share, run the following command: 
           
           smbclient //smb-server-ip/share-name -A smb-cred.txt -c 'ls'

  * To modify files with the smbclient tool, download the file, modify it locally, and then upload it back to the share as shown in the following steps.

    1. Download a file by running the get command: 
           
           smbclient //smb-server-ip/share-name -A smb-cred.txt -c 'get remote local'

    2. Modify your file locally.

    3. Upload the file after the modification by running the put command: 
           
           smbclient //smb-server-ip/share-name -A smb-cred.txt -c 'put local remote'




When you use the `smbclient` tool, the SMB server identifies you by using the credentials you provide. This lets the server apply the correct file permissions. For a full list of `smbclient` commands, refer to the [official smbclient documentation](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
