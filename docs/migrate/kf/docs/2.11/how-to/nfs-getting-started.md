---
url: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/nfs-getting-started/
title: Configure NFS volumes \u00a0|\u00a0 Kf 2.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:56.059854+00:00
---

# Configure NFS volumes  |  Kf 2.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/nfs-getting-started/

Version 2.11 - Latest version

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.11 ](https://docs.cloud.google.com/migrate/kf/docs/2.11)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.11/getting-started)



Send feedback 

#  Configure NFS volumes Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Kf supports mounting NFS volumes using the `kf marketplace`.

## Prerequisites

[Complete NFS platform setup](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/nfs-platform-setup).

## Create an NFS service instance

Run `kf marketplace` to see available services. The built-in NFS service appears on the list if NFS is enabled on the platform.
    
    
    Broker           Name  Namespace  Description
    nfsvolumebroker  nfs              mount nfs shares
    

## Mount an external filesystem

### Create a service instance

To mount to an existing NFS service:
    
    
    kf create-service nfs existing SERVICE-INSTANCE-NAME -c '{"share":"SERVER/SHARE", "capacity":"CAPACITY"}'

Replace variables with your values.

  * SERVICE-INSTANCE-NAME is the name you want for this NFS volume service instance.
  * SERVER/SHARE is the NFS address of your server and share.
  * CAPACITY uses the [Kubernetes quantity](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) format.



Confirm that the NFS volume service appears in your list of services. You can expect output similar to this example:
    
    
    $ kf services
    ...
    Listing services in Space: demo-space
    Name                Type      ClassName         PlanName  Age    Ready  Reason
    filestore-nfs       volume    nfs               existing  6s     True   <nil>
    ...
    

### Bind your service instance to an App

To bind an NFS service instance to an App, run:
    
    
    kf bind-service YOUR-APP-NAME SERVICE-NAME -c '{"uid":"2000","gid":"2000","mount":"MOUNT-PATH","readonly":true}'

Replace variables with your values.

  * YOUR-APP-NAME is the name of the App for which you want to use the volume service.

  * SERVICE-NAME is the name of the volume service instance you created in the previous step.

  * `uid`:UID and `gid`:GID specify the directory permissions of the mounting share.

**Note:** For buildpack Apps, the value for `uid` and `gid` is always 2000. Otherwise, the user specified by `uid` and `gid` should be the `uid` and `gid` of the running App process.
  * MOUNT-PATH is the path the volume should be mounted to within your App.

  * (Optional) `"readonly":true` is an optional JSON string that creates a read-only mount. By default, Volume Services mounts a read-write file system.

**Note:** Your App automatically restarts when the NFS binding changes.



You can list all bindings in a Space using the `kf bindings` command. You will see output similar to this example:
    
    
    $ kf bindings
    ...
    Listing bindings in Space: demo-space
    Name                                     App           Service             Age  Ready
    binding-spring-music-filestore-nfs       spring-music  filestore-nfs       71s  True
    ...
    

### Access the volume service from your App

To access the volume service from your App, you must know which file path to use in your code. You can view the file path in the details of the service binding, which are visible in the environment variables for your App.

View environment variables for your App:
    
    
    kf vcap-services YOUR-APP-NAME

Replace YOUR-APP-NAME with the name of your App.

The following is example output of the `kf vcap-services` command:
    
    
    kf vcap-services *YOUR-APP-NAME*
    {
      "nfs": [
        {
          "instance_name": "nfs-instance",
          "name": "nfs-instance",
          "label": "nfs",
          "tags": [],
          "plan": "existing",
          "credentials": {
            "capacity": "1Gi",
            "gid": 2000,
            "mount": "/test/mount",
            "share": "10.91.208.210/test",
            "uid": 2000
          },
          "volume_mounts": [
            {
              "container_dir": "/test/mount",
              "device_type": "shared",
              "mode": "rw"
            }
          ]
        }
      ]
    }

Use the properties under `volume_mounts` for any information required by your App.

Property | Description  
---|---  
`container_dir` | String containing the path to the mounted volume that you bound to your App.  
`device_type` | The NFS volume release. This currently only supports shared devices. A shared device represents a distributed file system that can mount on all App instances simultaneously.  
`mode` | String that informs what type of access your App has to NFS, either `ro` (read-only), or `rw` (read and write).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
