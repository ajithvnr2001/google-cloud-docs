---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.5.0/sidecar/
title: Sidecar v1.5.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:00.517250+00:00
---

# Sidecar v1.5.0 custom resource definition  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.5.0/sidecar/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Sidecar v1.5.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.5.0/sidecar)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.5.0/sidecar)



## Spec schema

SidecarSpec specifies the desired state of Sidecar.
    
    
    additionalVolumes:
    - awsElasticBlockStore:
        fsType: string
        partition: integer
        readOnly: boolean
        volumeID: string
      azureDisk:
        cachingMode: string
        diskName: string
        diskURI: string
        fsType: string
        kind: string
        readOnly: boolean
      azureFile:
        readOnly: boolean
        secretName: string
        shareName: string
      cephfs:
        monitors:
        - string
        path: string
        readOnly: boolean
        secretFile: string
        secretRef:
          name: string
        user: string
      cinder:
        fsType: string
        readOnly: boolean
        secretRef:
          name: string
        volumeID: string
      configMap:
        defaultMode: integer
        items:
        - key: string
          mode: integer
          path: string
        name: string
        optional: boolean
      csi:
        driver: string
        fsType: string
        nodePublishSecretRef:
          name: string
        readOnly: boolean
        volumeAttributes:
      downwardAPI:
        defaultMode: integer
        items:
        - fieldRef:
            apiVersion: string
            fieldPath: string
          mode: integer
          path: string
          resourceFieldRef:
            containerName: string
            divisor: integer or string
            resources: string
      emptyDir:
        medium: string
        sizeLimit: integer or string
      ephemeral:
        volumeClaimTemplate:
          metadata:
          spec:
            accessModes:
            - string
            dataSource:
              apiGroup: string
              kind: string
              name: string
            dataSourceRef:
              apiGroup: string
              kind: string
              name: string
              namespace: string
            resources:
              claims:
              - name: string
              limits: integer or string
              requests: integer or string
            selector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels:
            storageClassName: string
            volumeAttributesClassName: string
            volumeMode: string
            volumeName: string
      fc:
        fsType: string
        lun: integer
        readOnly: boolean
        targetWWNs:
        - string
        wwids:
        - string
      flexVolume:
        driver: string
        fsType: string
        options:
        readOnly: boolean
        secretRef:
          name: string
      flocker:
        datasetName: string
        datasetUUID: string
      gcePersistentDisk:
        fsType: string
        partition: integer
        pdName: string
        readOnly: boolean
      gitRepo:
        directory: string
        repository: string
        revision: string
      glusterfs:
        endpoints: string
        path: string
        readOnly: boolean
      hostPath:
        path: string
        type: string
      iscsi:
        chapAuthDiscovery: boolean
        chapAuthSession: boolean
        fsType: string
        initiatorName: string
        iqn: string
        iscsiInterface: string
        lun: integer
        portals:
        - string
        readOnly: boolean
        secretRef:
          name: string
      name: string
      nfs:
        path: string
        readOnly: boolean
        server: string
      persistentVolumeClaim:
        claimName: string
        readOnly: boolean
      photonPersistentDisk:
        fsType: string
        pdID: string
      portworxVolume:
        fsType: string
        readOnly: boolean
        volumeID: string
      projected:
        defaultMode: integer
        sources:
          clusterTrustBundle:
            labelSelector:
                matchExpressions:
                  key: string
                  operator: string
                  type: string
                matchLabels: object
              namespaceSelector:
                matchExpressions:
                  key: string
                  operator: string
                  values: string
                matchLabels: object
            name: string
            optional: boolean
            paht: string
            signerName: string
        - configMap:
            items:
            - key: string
              mode: integer
              path: string
            name: string
            optional: boolean
          downwardAPI:
            items:
            - fieldRef:
                apiVersion: string
                fieldPath: string
              mode: integer
              path: string
              resourceFieldRef:
                containerName: string
                divisor: integer or string
                resource: string
          secret:
            items:
            - key: string
              mode: integer
              path: string
            name: string
            optional: boolean
          serviceAccountToken:
            audience: string
            expirationSeconds: integer
            path: string
      quobyte:
        group: string
        readOnly: boolean
        registry: string
        tenant: string
        user: string
        volume: string
      rbd:
        fsType: string
        image: string
        keyring: string
        monitors:
        - string
        pool: string
        readOnly: boolean
        secretRef:
          name: string
        user: string
      scaleIO:
        fsType: string
        gateway: string
        protectionDomain: string
        readonly: boolean
        secretRef:
          name: string
        sslEnabled: boolean
        storageMode: string
        storagePool: string
        system: string
        volumeName: string
      secret:
        defaultMode: integer
        items:
        - key: string
          mode: integer
          path: string
        optional: boolean
        secretName: string
      storageos:
        fsType: string
        readOnly: boolean
        secretRef:
          name: string
        volumeName: string
        volumeNamespace: string
      vsphereVolume:
        fsType: string
        storagePolicyID: string
        storagePolicyName: string
        volumePath: string
    sidecars:
    - args:
      - string
      command:
      - string
      env:
      - name: string
        value: string
        valueFrom:
          configMapKeyRef:
            key: string
            name: string
            optional: boolean
          fieldRef:
            apiVersion: string
            fieldPath: string
          resourceFieldRef:
            containerName: string
            divisor: integer or string
            resource: string
          secretKeyRef:
            key: string
            name: string
            optional: boolean
      envFrom:
      - configMapRef:
          name: string
          optional: boolean
        prefix: string
        secretRef:
          name: string
          optional: boolean
      image: string
      imagePullPolicy: string
      lifecycle:
        postStart:
          exec:
            command:
            - string
          httpGet:
            host: string
            httpHeaders:
            - name: string
              value: string
            path: string
            port: integer or string
            scheme: string
          sleep:
            seconds: integer64
          tcpSocket:
            host: string
            port: integer or string
        preStop:
          exec:
            command:
            - string
          httpGet:
            host: string
            httpHeaders:
            - name: string
              value: string
            path: string
            port: integer or string
            scheme: string
          sleep:
            seconds: integer64
          tcpSocket:
            host: string
            port: integer or string
      livenessProbe:
        exec:
          command:
          - string
        failureThreshold: integer
        grpc:
          port: integer
          service: string
        httpGet:
          host: string
          httpHeaders:
          - name: string
            value: string
          path: string
          port: integer or string
          scheme: string
        initialDelaySeconds: integer
        periodSeconds: integer
        successThreshold: integer
        tcpSocket:
          host: string
          port: integer or string
        terminationGracePeriodSeconds: integer
        timeoutSeconds: integer
      name: string
      ports:
      - containerPort: integer
        hostIP: string
        hostPort: integer
        name: string
        protocol: string
      readinessProbe:
        exec:
          command:
          - string
        failureThreshold: integer
        grpc:
          port: integer
          service: string
        httpGet:
          host: string
          httpHeaders:
          - name: string
            value: string
          path: string
          port: integer or string
          scheme: string
        initialDelaySeconds: integer
        periodSeconds: integer
        successThreshold: integer
        tcpSocket:
          host: string
          port: integer or string
        terminationGracePeriodSeconds: integer
        timeoutSeconds: integer
      resizePolicy:
      - resourceName: string
        restartPolicy: string
      resources:
        claims:
        - name: string
        limits: integer or string
        requests: integer or string
      restartPolicy: string
      securityContext:
        allowPrivilegeEscalation: boolean
        capabilities:
          add:
          - string
          drop:
          - string
        privileged: boolean
        procMount: string
        readOnlyRootFilesystem: boolean
        runAsGroup: integer
        runAsNonRoot: boolean
        runAsUser: integer
        seLinuxOptions:
          level: string
          role: string
          type: string
          user: string
        seccompProfile:
          localhostProfile: string
          type: string
        windowsOptions:
          gmsaCredentialSpec: string
          gmsaCredentialSpecName: string
          hostProcess: boolean
          runAsUserName: string
      startupProbe:
        exec:
          command:
          - string
        failureThreshold: integer
        grpc:
          port: integer
          service: string
        httpGet:
          host: string
          httpHeaders:
          - name: string
            value: string
          path: string
          port: integer or string
          scheme: string
        initialDelaySeconds: integer
        periodSeconds: integer
        successThreshold: integer
        tcpSocket:
          host: string
          port: integer or string
        terminationGracePeriodSeconds: integer
        timeoutSeconds: integer
      stdin: boolean
      stdinOnce: boolean
      terminationMessagePath: string
      terminationMessagePolicy: string
      tty: boolean
      volumeDevices:
      - devicePath: string
        name: string
      volumeMounts:
      - mountPath: string
        mountPropagation: string
        name: string
        readOnly: boolean
        subPath: string
        subPathExpr: string
      workingDir: string
    

FieldType  
Required or optional |  Description  
---|---  
`additionalVolumes`  
`list (object)`  
_Optional_ |  AdditionalVolumes specifies a list of existing volumes to mount into the sidecar containers. Refer to https://kubernetes.io/docs/concepts/storage/volumes/ for more information.   
`additionalVolumes[]`  
`object`  
 _Optional_ |  Volume represents a named volume in a pod that may be accessed by any container in the pod.   
`additionalVolumes[].awsElasticBlockStore`  
`object`  
 _Optional_ |  awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore   
`additionalVolumes[].awsElasticBlockStore.fsType`  
`string`  
 _Optional_ |  fsType is the file system type of the volume that you want to mount. Tip: Ensure that the file system type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore   
`additionalVolumes[].awsElasticBlockStore.partition`  
`integer`  
 _Optional_ |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).   
`additionalVolumes[].awsElasticBlockStore.readOnly`  
`boolean`  
 _Optional_ |  readOnly value true will force the readOnly setting in VolumeMounts. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore   
`additionalVolumes[].awsElasticBlockStore.volumeID`  
`string`  
 _Required_ |  volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore   
`additionalVolumes[].azureDisk`  
`object`  
 _Optional_ |  azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.   
`additionalVolumes[].azureDisk.cachingMode`  
`string`  
 _Optional_ |  cachingMode is the Host Caching mode: None, Read-only, Read Write.   
`additionalVolumes[].azureDisk.diskName`  
`string`  
 _Required_ |  diskName is the Name of the data disk in the blob storage   
`additionalVolumes[].azureDisk.diskURI`  
`string`  
 _Required_ |  diskURI is the URI of data disk in the blob storage   
`additionalVolumes[].azureDisk.fsType`  
`string`  
 _Optional_ |  fsType is File system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].azureDisk.kind`  
`string`  
 _Optional_ |  kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared   
`additionalVolumes[].azureDisk.readOnly`  
`boolean`  
 _Optional_ |  readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].azureFile`  
`object`  
 _Optional_ |  azureFile represents an Azure File Service mount on the host and bind mount to the pod.   
`additionalVolumes[].azureFile.readOnly`  
`boolean`  
 _Optional_ |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].azureFile.secretName`  
`string`  
 _Required_ |  secretName is the name of secret that contains Azure Storage Account Name and Key   
`additionalVolumes[].azureFile.shareName`  
`string`  
 _Required_ |  shareName is the azure share Name   
`additionalVolumes[].cephfs`  
`object`  
 _Optional_ |  cephFS represents a Ceph FS mount on the host that shares a pod's lifetime   
`additionalVolumes[].cephfs.monitors`  
`list (string)`  
_Required_ |  monitors is Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it   
`additionalVolumes[].cephfs.path`  
`string`  
 _Optional_ |  path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /   
`additionalVolumes[].cephfs.readOnly`  
`boolean`  
 _Optional_ |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it   
`additionalVolumes[].cephfs.secretFile`  
`string`  
 _Optional_ |  secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it   
`additionalVolumes[].cephfs.secretRef`  
`object`  
 _Optional_ |  secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it   
`additionalVolumes[].cephfs.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].cephfs.user`  
`string`  
 _Optional_ |  user is optional: User is the rados username, default is administrator More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it   
`additionalVolumes[].cinder`  
`object`  
 _Optional_ |  cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md   
`additionalVolumes[].cinder.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md   
`additionalVolumes[].cinder.readOnly`  
`boolean`  
 _Optional_ |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md   
`additionalVolumes[].cinder.secretRef`  
`object`  
 _Optional_ |  secretRef is optional: points to a secret object containing parameters used to connect to OpenStack   
`additionalVolumes[].cinder.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].cinder.volumeID`  
`string`  
 _Required_ |  volumeID used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md   
`additionalVolumes[].configMap`  
`object`  
 _Optional_ |  configMap represents a configMap that should populate this volume   
`additionalVolumes[].configMap.defaultMode`  
`integer`  
 _Optional_ |  defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644\. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].configMap.items`  
`list (object)`  
_Optional_ |  items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys won't be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`additionalVolumes[].configMap.items[]`  
`object`  
 _Optional_ |  Maps a string key to a path within a volume.   
`additionalVolumes[].configMap.items[].key`  
`string`  
 _Required_ |  key is the key to project.   
`additionalVolumes[].configMap.items[].mode`  
`integer`  
 _Optional_ |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].configMap.items[].path`  
`string`  
 _Required_ |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
`additionalVolumes[].csi`  
`object`  
 _Optional_ |  csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature).   
`additionalVolumes[].csi.driver`  
`string`  
 _Required_ |  driver is the name of the CSI driver that handles this volume. Consult with your administrator for the correct name as registered in the cluster.   
`additionalVolumes[].csi.fsType`  
`string`  
 _Optional_ |  fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default file system to apply.   
`additionalVolumes[].csi.nodePublishSecretRef`  
`object`  
 _optional_ |  nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.   
`additionalVolumes[].csi.nodePublishSecretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].csi.readOnly`  
`boolean`  
 _Optional_ |  readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).   
`additionalVolumes[].csi.volumeAttributes`  
`object (string)`  
_Optional_ |  volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.   
`additionalVolumes[].downwardAPI`  
`object`  
 _Optional_ |  downwardAPI represents downward API about the pod that should populate this volume   
`additionalVolumes[].downwardAPI.defaultMode`  
`integer`  
 _Optional_ |  Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644\. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].downwardAPI.items`  
`list (object)`  
_Optional_ |  Items is a list of downward API volume file   
`additionalVolumes[].downwardAPI.items[]`  
`object`  
 _Optional_ |  DownwardAPIVolumeFile represents information to create the file containing the pod field   
`additionalVolumes[].downwardAPI.items[].fieldRef`  
`object`  
 _Optional_ |  Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.   
`additionalVolumes[].downwardAPI.items[].fieldRef.apiVersion`  
`string`  
 _Optional_ |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`additionalVolumes[].downwardAPI.items[].fieldRef.fieldPath`  
`string`  
 _Required_ |  Path of the field to select in the specified API version.   
`additionalVolumes[].downwardAPI.items[].mode`  
`integer`  
 _Optional_ |  Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].downwardAPI.items[].path`  
`string`  
 _Required_ |  Required: Path is the relative path of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'.   
`additionalVolumes[].downwardAPI.items[].resourceFieldRef`  
`object`  
 _Optional_ |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are supported.   
`additionalVolumes[].downwardAPI.items[].resourceFieldRef.containerName`  
`string`  
 _Optional_ |  Container name: required for volumes, optional for env vars   
`additionalVolumes[].downwardAPI.items[].resourceFieldRef.divisor`  
`integer or string`  
 _Optional_ |  Specifies the output format of the exposed resources, defaults to "1"   
`additionalVolumes[].downwardAPI.items[].resourceFieldRef.resource`  
`string`  
 _Required_ |  Required: resource to select   
`additionalVolumes[].emptyDir`  
`object`  
 _Optional_ |  emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir   
`additionalVolumes[].emptyDir.medium`  
`string`  
 _Optional_ |  medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir   
`additionalVolumes[].emptyDir.sizeLimit`  
`integer or string`  
 _Optional_ |  sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir   
`additionalVolumes[].ephemeral`  
`object`  
 _Optional_ |  ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed. \n Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim). \n Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod. \n Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information. \n A pod can use both types of ephemeral volumes and persistent volumes at the same time.   
`additionalVolumes[].ephemeral.volumeClaimTemplate`  
`object`  
 _Optional_ |  Will be used to create a standalone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, or the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long). \n An existing PVC with that name that is not owned by the pod won't* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this isn't necessary, but it may be useful when manually reconstructing a broken cluster. \n This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created. \n Required, must not be nil.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.metadata`  
`object`  
 _Optional_ |  May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec`  
`object`  
 _Required_ |  The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.accessModes`  
`list (string)`  
_Optional_ |  accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.accessModes[]`  
`string`  
 _Optional_ |   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSource`  
`object`  
 _Optional_ |  dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef won't be copied to dataSource.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSource.apiGroup`  
`string`  
 _Optional_ |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSource.kind`  
`string`  
 _Required_ |  Kind is the type of resource being referenced   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSource.name`  
`string`  
 _Required_ |  Name is the name of resource being referenced   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef`  
`object`  
 _Optional_ |  dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn't specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn't set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef.apiGroup`  
`string`  
 _Optional_ |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef.kind`  
`string`  
 _Required_ |  Kind is the type of resource being referenced   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef.name`  
`string`  
 _Required_ |  Name is the name of resource being referenced   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace's owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources`  
`object`  
 _Optional_ |  resources represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources.claims`  
`list (object)`  
_Optional_ |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. \n This is an alpha field and requires enabling the DynamicResourceAllocation feature gate. \n This field is immutable. It can only be set for containers.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources.claims[]`  
`object`  
 _Optional_ |  ResourceClaim references one entry in PodSpec.ResourceClaims.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources.claims[].name`  
`string`  
 _Required_ |  Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources.limits`  
`integer or string`  
 _Optional_ |  Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.resources.requests`  
`integer or string`  
 _Optional_ |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector`  
`object`  
 _Optional_ |  selector is a label query over volumes to consider for binding.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions`  
`list (object)`  
_Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[]`  
`object`  
 _Optional_ |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[].key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[].operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[].values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.selector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.storageClassName`  
`string`  
 _Optional_ |  storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.volumeAttributesClassName`  
`string`  
 _Optional_ |  volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it's not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: [ Persistent Volumes - VolumeAttributesClass (Alpha)](https://kubernetes.io/docs/concepts/storage/persistent-volumes#volumeattributesclass). Using this field requires the VolumeAttributesClass feature gate to be enabled.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.volumeMode`  
`string`  
 _Optional_ |  volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.   
`additionalVolumes[].ephemeral.volumeClaimTemplate.spec.volumeName`  
`string`  
 _Optional_ |  volumeName is the binding reference to the PersistentVolume backing this claim.   
`additionalVolumes[].fc`  
`object`  
 _Optional_ |  fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.   
`additionalVolumes[].fc.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].fc.lun`  
`integer`  
 _Optional_ |  lun is Optional: FC target lun number   
`additionalVolumes[].fc.readOnly`  
`boolean`  
 _Optional_ |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].fc.targetWWNs`  
`list (string)`  
_Optional_ |  targetWWNs is Optional: FC target worldwide names (WWNs)   
`additionalVolumes[].fc.targetWWNs[]`  
`string`  
 _Optional_ |   
`additionalVolumes[].fc.wwids`  
`list (string)`  
_Optional_ |  wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.   
`additionalVolumes[].fc.wwids[]`  
`string`  
 _Optional_ |   
`additionalVolumes[].flexVolume`  
`object`  
 _Optional_ |  flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.   
`additionalVolumes[].flexVolume.driver`  
`string`  
 _Required_ |  driver is the name of the driver to use for this volume.   
`additionalVolumes[].flexVolume.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default file system depends on FlexVolume script.   
`additionalVolumes[].flexVolume.options`  
`object`  
 _Optional_ |  options is Optional: this field holds extra command options if any.   
`additionalVolumes[].flexVolume.readOnly`  
`boolean`  
 _Optional_ |  readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].flexVolume.secretRef`  
`object`  
 _Optional_ |  secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.   
`additionalVolumes[].flexVolume.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].flocker`  
`object`  
 _Optional_ |  flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running   
`additionalVolumes[].flocker.datasetName`  
`string`  
 _Optional_ |  datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated   
`additionalVolumes[].flocker.datasetUUID`  
`string`  
 _Optional_ |  datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset   
`additionalVolumes[].gcePersistentDisk`  
`object`  
 _Optional_ |  gcePersistentDisk represents a Compute Engine Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk   
`additionalVolumes[].gcePersistentDisk.fsType`  
`string`  
 _Optional_ |  fsType is file system type of the volume that you want to mount. Tip: Ensure that the file system type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk   
`additionalVolumes[].gcePersistentDisk.partition`  
`integer`  
 _Optional_ |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk   
`additionalVolumes[].gcePersistentDisk.pdName`  
`string`  
 _Required_ |  pdName is unique name of the persistent disk resource in Compute Engine. Used to identify the disk in Compute Engine. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk   
`additionalVolumes[].gcePersistentDisk.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk   
`additionalVolumes[].gitRepo`  
`object`  
 _Optional_ |  gitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repository, mount an EmptyDir into an InitContainer that clones the repository using git, then mount the EmptyDir into the Pod's container.   
`additionalVolumes[].gitRepo.directory`  
`string`  
 _Optional_ |  directory is the target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.   
`additionalVolumes[].gitRepo.repository`  
`string`  
 _Required_ |  repository is the URL   
`additionalVolumes[].gitRepo.revision`  
`string`  
 _Optional_ |  revision is the commit hash for the specified revision.   
`additionalVolumes[].glusterfs`  
`object`  
 _Optional_ |  glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md   
`additionalVolumes[].glusterfs.endpoints`  
`string`  
 _Required_ |  endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod   
`additionalVolumes[].glusterfs.path`  
`string`  
 _Required_ |  path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod   
`additionalVolumes[].glusterfs.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod   
`additionalVolumes[].hostPath`  
`object`  
 _Optional_ |  hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath   
`additionalVolumes[].hostPath.path`  
`string`  
 _Required_ |  path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath   
`additionalVolumes[].hostPath.type`  
`string`  
 _Optional_ |  type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath   
`additionalVolumes[].iscsi`  
`object`  
 _Optional_ |  iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md   
`additionalVolumes[].iscsi.chapAuthDiscovery`  
`boolean`  
 _Optional_ |  chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication   
`additionalVolumes[].iscsi.chapAuthSession`  
`boolean`  
 _Optional_ |  chapAuthSession defines whether support iSCSI Session CHAP authentication   
`additionalVolumes[].iscsi.fsType`  
`string`  
 _Optional_ |  fsType is the file system type of the volume that you want to mount. Tip: Ensure that the file system type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi   
`additionalVolumes[].iscsi.initiatorName`  
`string`  
 _Optional_ |  initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.   
`additionalVolumes[].iscsi.iqn`  
`string`  
 _Required_ |  iqn is the target iSCSI Qualified Name.   
`additionalVolumes[].iscsi.iscsiInterface`  
`string`  
 _Optional_ |  iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).   
`additionalVolumes[].iscsi.lun`  
`integer`  
 _Required_ |  lun represents iSCSI Target Lun number.   
`additionalVolumes[].iscsi.portals`  
`list (string)`  
_Optional_ |  portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
`additionalVolumes[].iscsi.portals[]`  
`string`  
 _Optional_ |   
`additionalVolumes[].iscsi.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.   
`additionalVolumes[].iscsi.secretRef`  
`object`  
 _Optional_ |  secretRef is the CHAP Secret for iSCSI target and initiator authentication   
`additionalVolumes[].iscsi.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].iscsi.targetPortal`  
`string`  
 _Required_ |  targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
`additionalVolumes[].name`  
`string`  
 _Required_ |  name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].nfs`  
`object`  
 _Optional_ |  nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs   
`additionalVolumes[].nfs.path`  
`string`  
 _Required_ |  path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs   
`additionalVolumes[].nfs.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs   
`additionalVolumes[].nfs.server`  
`string`  
 _Required_ |  server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs   
`additionalVolumes[].persistentVolumeClaim`  
`object`  
 _Optional_ |  persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims   
`additionalVolumes[].persistentVolumeClaim.claimName`  
`string`  
 _Required_ |  claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims   
`additionalVolumes[].persistentVolumeClaim.readOnly`  
`boolean`  
 _Optional_ |  readOnly Will force the ReadOnly setting in VolumeMounts. Default false.   
`additionalVolumes[].photonPersistentDisk`  
`object`  
 _Optional_ |  photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine   
`additionalVolumes[].photonPersistentDisk.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].photonPersistentDisk.pdID`  
`string`  
 _Required_ |  pdID is the ID that identifies Photon Controller persistent disk   
`additionalVolumes[].portworxVolume`  
`object`  
 _Optional_ |  portworxVolume represents a portworx volume attached and mounted on kubelets host machine   
`additionalVolumes[].portworxVolume.fsType`  
`string`  
 _Optional_ |  fSType represents the file system type to mount Must be a file system type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].portworxVolume.readOnly`  
`boolean`  
 _Optional_ |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].portworxVolume.volumeID`  
`string`  
 _Required_ |  volumeID uniquely identifies a Portworx volume   
`additionalVolumes[].projected`  
`object`  
 _Optional_ |  projected items for all in one resources secrets, configmaps, and downward API   
`additionalVolumes[].projected.defaultMode`  
`integer`  
 _Optional_ |  defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].projected.sources`  
`list (object)`  
_Optional_ |  sources is the list of volume projections   
`additionalVolumes[].projected.sources[]`  
`object`  
 _Optional_ |  Projection that may be projected along with other supported volume types.   
`additionalVolumes[].projected.sources[].clusterTrustBundle`  
`object`  
 _Optional_ |  ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.   
Alpha, gated by the ClusterTrustBundleProjection feature gate.   
ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.   
Kubelet performs aggressive normalization of the PEM contents written into the pod file system. Esoteric PEM features such as inter-block comments and block headers are stripped. Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector`  
`object`  
 _Optional_ |  Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything".   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`additionalVolumes[].projected.sources[].clusterTrustBundle.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`additionalVolumes[].projected.sources[].configMap`  
`object`  
 _Optional_ |  configMap information about the configMap data to project   
`additionalVolumes[].projected.sources[].configMap.items`  
`list (object)`  
_Optional_ |  items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys won't be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`additionalVolumes[].projected.sources[].configMap.items[]`  
`object`  
 _Optional_ |  Maps a string key to a path within a volume.   
`additionalVolumes[].projected.sources[].configMap.items[].key`  
`string`  
 _Required_ |  key is the key to project.   
`additionalVolumes[].projected.sources[].configMap.items[].mode`  
`integer`  
 _Optional_ |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511\. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].projected.sources[].configMap.items[].path`  
`string`  
 _Required_ |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
`additionalVolumes[].projected.sources[].configMap.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].projected.sources[].configMap.optional`  
`boolean`  
 _Optional_ |  optional specify whether the ConfigMap or its keys must be defined   
`additionalVolumes[].projected.sources[].downwardAPI`  
`object`  
 _Optional_ |  downwardAPI information about the downwardAPI data to project   
`additionalVolumes[].projected.sources[].downwardAPI.items`  
`list (object)`  
_Optional_ |  Items is a list of DownwardAPIVolume file   
`additionalVolumes[].projected.sources[].downwardAPI.items[]`  
`object`  
 _Optional_ |  DownwardAPIVolumeFile represents information to create the file containing the pod field   
`additionalVolumes[].projected.sources[].downwardAPI.items[].fieldRef`  
`object`  
 _Optional_ |  Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.   
`additionalVolumes[].projected.sources[].downwardAPI.items[].fieldRef.apiVersion`  
`string`  
 _Optional_ |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`additionalVolumes[].projected.sources[].downwardAPI.items[].fieldRef.fieldPath`  
`string`  
 _Required_ |  Path of the field to select in the specified API version.   
`additionalVolumes[].projected.sources[].downwardAPI.items[].mode`  
`integer`  
 _Optional_ |  Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].projected.sources[].downwardAPI.items[].path`  
`string`  
 _Required_ |  Required: Path is the relative path of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'   
`additionalVolumes[].projected.sources[].downwardAPI.items[].resourceFieldRef`  
`object`  
 _Optional_ |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are supported.   
`additionalVolumes[].projected.sources[].downwardAPI.items[].resourceFieldRef.containerName`  
`string`  
 _Optional_ |  Container name: required for volumes, optional for env vars   
`additionalVolumes[].projected.sources[].downwardAPI.items[].resourceFieldRef.divisor`  
`integer or string`  
 _Optional_ |  Specifies the output format of the exposed resources, defaults to "1"   
`additionalVolumes[].projected.sources[].downwardAPI.items[].resourceFieldRef.resource`  
`string`  
 _Required_ |  Required: resource to select   
`additionalVolumes[].projected.sources[].secret`  
`object`  
 _Optional_ |  secret information about the secret data to project   
`additionalVolumes[].projected.sources[].secret.items`  
`list (object)`  
_Optional_ |  items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys won't be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`additionalVolumes[].projected.sources[].secret.items[]`  
`object`  
 _Optional_ |  Maps a string key to a path within a volume.   
`additionalVolumes[].projected.sources[].secret.items[].key`  
`string`  
 _Required_ |  key is the key to project.   
`additionalVolumes[].projected.sources[].secret.items[].mode`  
`integer`  
 _Optional_ |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511\. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].projected.sources[].secret.items[].path`  
`string`  
 _Required_ |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
`additionalVolumes[].projected.sources[].secret.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].projected.sources[].secret.optional`  
`boolean`  
 _Optional_ |  optional field specify whether the Secret or its key must be defined   
`additionalVolumes[].projected.sources[].serviceAccountToken`  
`object`  
 _Optional_ |  serviceAccountToken is information about the serviceAccountToken data to project   
`additionalVolumes[].projected.sources[].serviceAccountToken.audience`  
`string`  
 _Optional_ |  audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.   
`additionalVolumes[].projected.sources[].serviceAccountToken.expirationSeconds`  
`integer`  
 _Optional_ |  expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.   
`additionalVolumes[].projected.sources[].serviceAccountToken.path`  
`string`  
 _Required_ |  path is the path relative to the mount point of the file to project the token into.   
`additionalVolumes[].quobyte`  
`object`  
 _Optional_ |  quobyte represents a Quobyte mount on the host that shares a pod's lifetime   
`additionalVolumes[].quobyte.group`  
`string`  
 _Optional_ |  group to map volume access to Default is no group   
`additionalVolumes[].quobyte.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.   
`additionalVolumes[].quobyte.registry`  
`string`  
 _Required_ |  registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes   
`additionalVolumes[].quobyte.tenant`  
`string`  
 _Optional_ |  tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin   
`additionalVolumes[].quobyte.user`  
`string`  
 _Optional_ |  user to map volume access to Defaults to serivceaccount user   
`additionalVolumes[].quobyte.volume`  
`string`  
 _Required_ |  volume is a string that references an already created Quobyte volume by name.   
`additionalVolumes[].rbd`  
`object`  
 _Optional_ |  rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md   
`additionalVolumes[].rbd.fsType`  
`string`  
 _Optional_ |  fsType is the file system type of the volume that you want to mount. Tip: Ensure that the file system type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd   
`additionalVolumes[].rbd.image`  
`string`  
 _Required_ |  image is the rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.keyring`  
`string`  
 _Optional_ |  keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.monitors`  
`list (string)`  
_Required_ |  monitors is a collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.monitors[]`  
`string`  
 _Optional_ |   
`additionalVolumes[].rbd.pool`  
`string`  
 _Optional_ |  pool is the rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.readOnly`  
`boolean`  
 _Optional_ |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.secretRef`  
`object`  
 _Optional_ |  secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].rbd.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].rbd.user`  
`string`  
 _Optional_ |  user is the rados username. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it   
`additionalVolumes[].scaleIO`  
`object`  
 _Optional_ |  scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.   
`additionalVolumes[].scaleIO.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".   
`additionalVolumes[].scaleIO.gateway`  
`string`  
 _Required_ |  gateway is the host address of the ScaleIO API Gateway.   
`additionalVolumes[].scaleIO.protectionDomain`  
`string`  
 _Optional_ |  protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.   
`additionalVolumes[].scaleIO.readOnly`  
`boolean`  
 _Optional_ |  readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].scaleIO.secretRef`  
`object`  
 _Required_ |  secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.   
`additionalVolumes[].scaleIO.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].scaleIO.sslEnabled`  
`boolean`  
 _Optional_ |  sslEnabled Flag enable/disable SSL communication with Gateway, default false   
`additionalVolumes[].scaleIO.storageMode`  
`string`  
 _Optional_ |  storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.   
`additionalVolumes[].scaleIO.storagePool`  
`string`  
 _Optional_ |  storagePool is the ScaleIO Storage Pool associated with the protection domain.   
`additionalVolumes[].scaleIO.system`  
`string`  
 _Required_ |  system is the name of the storage system as configured in ScaleIO.   
`additionalVolumes[].scaleIO.volumeName`  
`TYPE`  
 _Optional_ |  volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.   
`additionalVolumes[].secret`  
`object`  
 _Optional_ |  secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret   
`additionalVolumes[].secret.defaultMode`  
`integer`  
 _Optional_ |  defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644\. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].secret.items`  
`list (object)`  
_Optional_ |  items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys won't be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`additionalVolumes[].secret.items[]`  
`object`  
 _Optional_ |  Maps a string key to a path within a volume.   
`additionalVolumes[].secret.items[].key`  
`string`  
 _Required_ |  key is the key to project.   
`additionalVolumes[].secret.items[].mode`  
`integer`  
 _Optional_ |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`additionalVolumes[].secret.items[].path`  
`string`  
 _Required_ |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
`additionalVolumes[].secret.optional`  
`boolean`  
 _Optional_ |  optional field specify whether the Secret or its keys must be defined   
`additionalVolumes[].secret.secretName`  
`string`  
 _Optional_ |  secretName is the name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret   
`additionalVolumes[].storageos`  
`object`  
 _Optional_ |  storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.   
`additionalVolumes[].storageos.fsType`  
`string`  
 _Optional_ |  fsType is the file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].storageos.readOnly`  
`boolean`  
 _Optional_ |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`additionalVolumes[].storageos.secretRef`  
`object`  
 _Optional_ |  secretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted.   
`additionalVolumes[].storageos.secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`additionalVolumes[].storageos.volumeName`  
`string`  
 _Optional_ |  volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace.   
`additionalVolumes[].storageos.volumeNamespace`  
`string`  
 _Optional_ |  volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod's namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that don't pre-exist within StorageOS will be created.   
`additionalVolumes[].vsphereVolume`  
`object`  
 _Optional_ |  vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine   
`additionalVolumes[].vsphereVolume.fsType`  
`string`  
 _Optional_ |  fsType is file system type to mount. Must be a file system type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`additionalVolumes[].vsphereVolume.storagePolicyID`  
`string`  
 _Optional_ |  storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.   
`additionalVolumes[].vsphereVolume.storagePolicyName`  
`string`  
 _Optional_ |  storagePolicyName is the storage Policy Based Management (SPBM) profile name.   
`additionalVolumes[].vsphereVolume.volumePath`  
`string`  
 _Required_ |  volumePath is the path that identifies vSphere volume vmdk   
`sidecars`  
`list (object)`  
_Optional_ |  Sidecar specifies a list of sidecar containers to inject into the database pod. Refer to https://kubernetes.io/docs/concepts/containers/ for more information.   
`sidecars[]`  
`object`  
 _Optional_ |  A single application container that you want to run within a pod.   
`sidecars[].args`  
`list (string)`  
_Optional_ |  Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax:; on other words, "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references are never expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell   
`sidecars[].args[]`  
`string`  
 _Optional_ |   
`sidecars[].command`  
`list (string)`  
_Optional_ |  Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax; in other words, "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell   
`sidecars[].command[]`  
`string`  
 _Optional_ |   
`sidecars[].env`  
`list (object)`  
_Optional_ |  List of environment variables to set in the container. Cannot be updated.   
`sidecars[].env[]`  
`object`  
 _Optional_ |  EnvVar represents an environment variable present in a Container.   
`sidecars[].env[].name`  
`string`  
 _Required_ |  Name of the environment variable. Must be a C_IDENTIFIER.   
`sidecars[].env[].value`  
`string`  
 _Optional_ |  Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax; in other words, "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".   
`sidecars[].env[].valueFrom`  
`object`  
 _Optional_ |  Source for the environment variable's value. Cannot be used if value is not empty.   
`sidecars[].env[].valueFrom.configMapKeyRef`  
`object`  
 _Optional_ |  Selects a key of a ConfigMap.   
`sidecars[].env[].valueFrom.configMapKeyRef.key`  
`string`  
 _Required_ |  The key to select.   
`sidecars[].env[].valueFrom.configMapKeyRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`sidecars[].env[].valueFrom.configMapKeyRef.optional`  
`boolean`  
 _Optional_ |  Specify whether the ConfigMap or its key must be defined   
`sidecars[].env[].valueFrom.fieldRef`  
`object`  
 _Optional_ |  Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels['<KEY>'], metadata.annotations['<KEY>'], spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.   
`sidecars[].env[].valueFrom.fieldRef.apiVersion`  
`string`  
 _Optional_ |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`sidecars[].env[].valueFrom.fieldRef.fieldPath`  
`string`  
 _Required_ |  Path of the field to select in the specified API version.   
`sidecars[].env[].valueFrom.resourceFieldRef`  
`object`  
 _Optional_ |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are supported.   
`sidecars[].env[].valueFrom.resourceFieldRef.containerName`  
`string`  
 _Optional_ |  Container name: required for volumes, optional for env vars   
`sidecars[].env[].valueFrom.resourceFieldRef.divisor`  
`integer or string`  
 _Optional_ |  Specifies the output format of the exposed resources, defaults to "1"   
`sidecars[].env[].valueFrom.resourceFieldRef.resource`  
`string`  
 _Required_ |  Required: resource to select   
`sidecars[].env[].valueFrom.secretKeyRef`  
`object`  
 _Optional_ |  Selects a key of a secret in the pod's namespace   
`sidecars[].env[].valueFrom.secretKeyRef.key`  
`string`  
 _Required_ |  The key of the secret to select from. Must be a valid secret key.   
`sidecars[].env[].valueFrom.secretKeyRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`sidecars[].env[].valueFrom.secretKeyRef.optional`  
`boolean`  
 _Optional_ |  Specify whether the Secret or its key must be defined   
`sidecars[].envFrom`  
`list (object)`  
_Optional_ |  List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.   
`sidecars[].envFrom[]`  
`object`  
 _Optional_ |  EnvFromSource represents the source of a set of ConfigMaps   
`sidecars[].envFrom[].configMapRef`  
`object`  
 _Optional_ |  The ConfigMap to select from   
`sidecars[].envFrom[].configMapRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`sidecars[].envFrom[].configMapRef.optional`  
`boolean`  
 _Optional_ |  Specify whether the ConfigMap must be defined   
`sidecars[].envFrom[].prefix`  
`string`  
 _Optional_ |  An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.   
`sidecars[].envFrom[].secretRef`  
`object`  
 _Optional_ |  The Secret to select from   
`sidecars[].envFrom[].secretRef.name`  
`string`  
 _Optional_ |  Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names   
`sidecars[].envFrom[].secretRef.optional`  
`boolean`  
 _Optional_ |  Specify whether the Secret must be defined   
`sidecars[].image`  
`string`  
 _Optional_ |  Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.   
`sidecars[].imagePullPolicy`  
`string`  
 _Optional_ |  Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :{{ .Chart.Version }} tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images   
`sidecars[].lifecycle`  
`object`  
 _Optional_ |  Actions that the management system should take in response to container lifecycle events. Cannot be updated.   
`sidecars[].lifecycle.postStart`  
`object`  
 _Optional_ |  PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks   
`sidecars[].lifecycle.postStart.exec`  
`object`  
 _Optional_ |  Exec specifies the action to take.   
`sidecars[].lifecycle.postStart.exec.command`  
`list (string)`  
_Optional_ |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's file system. The command is exec'd, it is not run inside a shell, so standard shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
`sidecars[].lifecycle.postStart.exec.command[]`  
`string`  
 _Optional_ |   
`sidecars[].lifecycle.postStart.httpGet`  
`object`  
 _Optional_ |  HTTPGet specifies the http request to perform.   
`sidecars[].lifecycle.postStart.httpGet.host`  
`string`  
 _Optional_ |  Hostname to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`sidecars[].lifecycle.postStart.httpGet.httpHeaders`  
`list (object)`  
_Optional_ |  Custom headers to set in the request. HTTP allows repeated headers.   
`sidecars[].lifecycle.postStart.httpGet.httpHeaders[]`  
`object`  
 _Optional_ |  HTTPHeader describes a custom header to be used in HTTP probes   
`sidecars[].lifecycle.postStart.httpGet.httpHeaders[].name`  
`string`  
 _Required_ |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`sidecars[].lifecycle.postStart.httpGet.httpHeaders[].value`  
`string`  
 _Required_ |  The header field value   
`sidecars[].lifecycle.postStart.httpGet.path`  
`string`  
 _Optional_ |  Path to access on the HTTP server.   
`sidecars[].lifecycle.postStart.httpGet.port`  
`integer or string`  
 _Required_ |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].lifecycle.postStart.httpGet.scheme`  
`string`  
 _Optional_ |  Scheme to use for connecting to the host. Defaults to HTTP.   
`sidecars[].lifecycle.postStart.sleep`  
`object`  
 _Optional_ |  Sleep represents the duration that the container must sleep before being terminated.   
`sidecars[].lifecycle.postStart.sleep.seconds`  
`object`  
 _Required_ |  Seconds is the number of seconds to sleep in `int64` format.   
`sidecars[].lifecycle.postStart.tcpSocket`  
`object`  
 _Optional_ |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified.   
`sidecars[].lifecycle.postStart.tcpSocket.host`  
`string`  
 _Optional_ |  Optional: Hostname to connect to, defaults to the pod IP.   
`sidecars[].lifecycle.postStart.tcpSocket.port`  
`integer or string`  
 _Required_ |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].lifecycle.preStop`  
`object`  
 _Optional_ |  PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, and resource contention. The handler is not called if the container crashes or exits. The Pod's termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks   
`sidecars[].lifecycle.preStop.exec`  
`object`  
 _Optional_ |  Exec specifies the action to take.   
`sidecars[].lifecycle.preStop.exec.command`  
`list (string)`  
_Optional_ |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's file system. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
`sidecars[].lifecycle.preStop.exec.command[]`  
`string`  
 _Optional_ |   
`sidecars[].lifecycle.preStop.httpGet`  
`object`  
 _Optional_ |  HTTPGet specifies the http request to perform.   
`sidecars[].lifecycle.preStop.httpGet.host`  
`string`  
 _Optional_ |  Hostname to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`sidecars[].lifecycle.preStop.httpGet.httpHeaders`  
`list (object)`  
_Optional_ |  Custom headers to set in the request. HTTP allows repeated headers.   
`sidecars[].lifecycle.preStop.httpGet.httpHeaders[]`  
`object`  
 _Optional_ |  HTTPHeader describes a custom header to be used in HTTP probes   
`sidecars[].lifecycle.preStop.httpGet.httpHeaders[].name`  
`string`  
 _Required_ |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`sidecars[].lifecycle.preStop.httpGet.httpHeaders[].value`  
`string`  
 _Required_ |  The header field value   
`sidecars[].lifecycle.preStop.httpGet.path`  
`string`  
 _Optional_ |  Path to access on the HTTP server.   
`sidecars[].lifecycle.preStop.httpGet.port`  
`integer or string`  
 _Required_ |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].lifecycle.preStop.httpGet.scheme`  
`string`  
 _Optional_ |  Scheme to use for connecting to the host. Defaults to HTTP.   
`sidecars[].lifecycle.preStop.sleep`  
`object`  
 _Optional_ |  Sleep represents the duration that the container should sleep before being terminated.   
`sidecars[].lifecycle.preStop.sleep.seconds`  
`object`  
 _Required_ |  Seconds is the number of seconds to sleep in `int64` format.   
`sidecars[].lifecycle.preStop.tcpSocket`  
`object`  
 _Optional_ |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for the backward compatibility. There are no validation of this field and lifecycle hooks will fail in runtime when tcp handler is specified.   
`sidecars[].lifecycle.preStop.tcpSocket.host`  
`string`  
 _Optional_ |  Optional: Hostname to connect to, defaults to the pod IP.   
`sidecars[].lifecycle.preStop.tcpSocket.port`  
`integer or string`  
 _Required_ |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].livenessProbe`  
`object`  
 _Optional_ |  Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].livenessProbe.exec`  
`object`  
 _Optional_ |  Exec specifies the action to take.   
`sidecars[].livenessProbe.exec.command`  
`list (string)`  
_Optional_ |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's file system. The command is exec'd, it is not run inside a shell, so standard shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
`sidecars[].livenessProbe.exec.command[]`  
`string`  
 _Optional_ |   
`sidecars[].livenessProbe.failureThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`sidecars[].livenessProbe.grpc`  
`object`  
 _Optional_ |  GRPC specifies an action involving a GRPC port.   
`sidecars[].livenessProbe.grpc.port`  
`integer`  
 _Required_ |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`sidecars[].livenessProbe.grpc.service`  
`string`  
 _Optional_ |  Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md). \n If this is not specified, the default behavior is defined by gRPC.   
`sidecars[].livenessProbe.httpGet`  
`object`  
 _Optional_ |  HTTPGet specifies the http request to perform.   
`sidecars[].livenessProbe.httpGet.host`  
`string`  
 _Optional_ |  Hostname to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`sidecars[].livenessProbe.httpGet.httpHeaders`  
`list (object)`  
_Optional_ |  Custom headers to set in the request. HTTP allows repeated headers.   
`sidecars[].livenessProbe.httpGet.httpHeaders[]`  
`object`  
 _Optional_ |  HTTPHeader describes a custom header to be used in HTTP probes   
`sidecars[].livenessProbe.httpGet.httpHeaders[].name`  
`string`  
 _Required_ |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`sidecars[].livenessProbe.httpGet.httpHeaders[].value`  
`string`  
 _Required_ |  The header field value   
`sidecars[].livenessProbe.httpGet.path`  
`string`  
 _Optional_ |  Path to access on the HTTP server.   
`sidecars[].livenessProbe.httpGet.port`  
`integer or string`  
 _Required_ |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].livenessProbe.httpGet.scheme`  
`string`  
 _Optional_ |  Scheme to use for connecting to the host. Defaults to HTTP.   
`sidecars[].livenessProbe.initialDelaySeconds`  
`integer`  
 _Optional_ |  Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].livenessProbe.periodSeconds`  
`integer`  
 _Optional_ |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`sidecars[].livenessProbe.successThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`sidecars[].livenessProbe.tcpSocket`  
`object`  
 _Optional_ |  TCPSocket specifies an action involving a TCP port.   
`sidecars[].livenessProbe.tcpSocket.host`  
`string`  
 _Optional_ |  Optional: Hostname to connect to, defaults to the pod IP.   
`sidecars[].livenessProbe.tcpSocket.port`  
`integer or string`  
 _Required_ |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].livenessProbe.terminationGracePeriodSeconds`  
`integer`  
 _Optional_ |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately using the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`sidecars[].livenessProbe.timeoutSeconds`  
`integer`  
 _Optional_ |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].name`  
`string`  
 _Required_ |  Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.   
`sidecars[].ports`  
`list (object)`  
_Optional_ |  List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.   
`sidecars[].ports[]`  
`object`  
 _Optional_ |  ContainerPort represents a network port in a single container.   
`sidecars[].ports[].containerPort`  
`integer`  
 _Required_ |  Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536\.   
`sidecars[].ports[].hostIP`  
`string`  
 _Optional_ |  What host IP to bind the external port to.   
`sidecars[].ports[].hostPort`  
`integer`  
 _Optional_ |  Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536\. If HostNetwork is specified, this must match ContainerPort. Most containers don't need this.   
`sidecars[].ports[].name`  
`string`  
 _Optional_ |  If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.   
`sidecars[].ports[].protocol`  
`string`  
 _Optional_ |  Default value: TCP Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".   
`sidecars[].readinessProbe`  
`object`  
 _Optional_ |  Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].readinessProbe.exec`  
`object`  
 _Optional_ |  Exec specifies the action to take.   
`sidecars[].readinessProbe.exec.command`  
`list (string)`  
_Optional_ |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's file system. The command is is exec'd, it is not run inside a shell, so standard shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
`sidecars[].readinessProbe.exec.command[]`  
`string`  
 _Optional_ |   
`sidecars[].readinessProbe.failureThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`sidecars[].readinessProbe.grpc`  
`object`  
 _Optional_ |  GRPC specifies an action involving a GRPC port.   
`sidecars[].readinessProbe.grpc.port`  
`integer`  
 _Required_ |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`sidecars[].readinessProbe.grpc.service`  
`string`  
 _Optional_ |  Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md). \n If this is not specified, the default behavior is defined by gRPC.   
`sidecars[].readinessProbe.httpGet`  
`object`  
 _Optional_ |  HTTPGet specifies the http request to perform.   
`sidecars[].readinessProbe.httpGet.host`  
`string`  
 _Optional_ |  Hostname to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`sidecars[].readinessProbe.httpGet.httpHeaders`  
`list (object)`  
_Optional_ |  Custom headers to set in the request. HTTP allows repeated headers.   
`sidecars[].readinessProbe.httpGet.httpHeaders[]`  
`object`  
 _Optional_ |  HTTPHeader describes a custom header to be used in HTTP probes   
`sidecars[].readinessProbe.httpGet.httpHeaders[].name`  
`string`  
 _Required_ |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`sidecars[].readinessProbe.httpGet.httpHeaders[].value`  
`string`  
 _Required_ |  The header field value   
`sidecars[].readinessProbe.httpGet.path`  
`string`  
 _Optional_ |  Path to access on the HTTP server.   
`sidecars[].readinessProbe.httpGet.port`  
`integer or string`  
 _Required_ |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].readinessProbe.httpGet.scheme`  
`string`  
 _Optional_ |  Scheme to use for connecting to the host. Defaults to HTTP.   
`sidecars[].readinessProbe.initialDelaySeconds`  
`integer`  
 _Optional_ |  Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].readinessProbe.periodSeconds`  
`integer`  
 _Optional_ |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`sidecars[].readinessProbe.successThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`sidecars[].readinessProbe.tcpSocket`  
`object`  
 _Optional_ |  TCPSocket specifies an action involving a TCP port.   
`sidecars[].readinessProbe.tcpSocket.host`  
`string`  
 _Optional_ |  Optional: Hostname to connect to, defaults to the pod IP.   
`sidecars[].readinessProbe.tcpSocket.port`  
`integer or string`  
 _Required_ |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].readinessProbe.terminationGracePeriodSeconds`  
`integer`  
 _Optional_ |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately using the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`sidecars[].readinessProbe.timeoutSeconds`  
`integer`  
 _Optional_ |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].resizePolicy`  
`list (object)`  
_Optional_ |  Resources resize policy for the container.   
`sidecars[].resizePolicy[]`  
`object`  
 _Optional_ |  ContainerResizePolicy represents resource resize policy for the container.   
`sidecars[].resizePolicy[].resourceName`  
`string`  
 _Required_ |  Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.   
`sidecars[].resizePolicy[].restartPolicy`  
`string`  
 _Required_ |  Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.   
`sidecars[].resources`  
`object`  
 _Optional_ |  Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/   
`sidecars[].resources.claims`  
`list (object)`  
_Optional_ |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. \n This is an alpha field and requires enabling the DynamicResourceAllocation feature gate. \n This field is immutable. It can only be set for containers.   
`sidecars[].resources.claims[]`  
`object`  
 _Optional_ |  ResourceClaim references one entry in PodSpec.ResourceClaims.   
`sidecars[].resources.claims[].name`  
`string`  
 _Required_ |  Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.   
`sidecars[].resources.limits`  
`integer or string`  
 _Optional_ |  Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/   
`sidecars[].resources.requests`  
`integer or string`  
 _Optional_ |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/   
`sidecars[].restartPolicy`  
`string`  
 _Optional_ |  RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is "Always". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.   
`sidecars[].securityContext`  
`object`  
 _Optional_ |  SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/   
`sidecars[].securityContext.allowPrivilegeEscalation`  
`boolean`  
 _Optional_ |  AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.capabilities`  
`object`  
 _Optional_ |  The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.capabilities.add`  
`list (string)`  
_Optional_ |  Added capabilities   
`sidecars[].securityContext.capabilities.add[]`  
`string`  
 _Optional_ |  Capability represent POSIX capabilities type   
`sidecars[].securityContext.capabilities.drop`  
`list (string)`  
_Optional_ |  Removed capabilities   
`sidecars[].securityContext.capabilities.drop[]`  
`string`  
 _Optional_ |  Capability represent POSIX capabilities type   
`sidecars[].securityContext.privileged`  
`boolean`  
 _Optional_ |  Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.procMount`  
`string`  
 _Optional_ |  procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.readOnlyRootFilesystem`  
`boolean`  
 _Optional_ |  Whether this container has a read-only root file system. Default is false. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.runAsGroup`  
`integer`  
 _Optional_ |  The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.runAsNonRoot`  
`boolean`  
 _Optional_ |  Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
`sidecars[].securityContext.runAsUser`  
`integer`  
 _Optional_ |  The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.seLinuxOptions`  
`object`  
 _Optional_ |  The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.seLinuxOptions.level`  
`string`  
 _Optional_ |  Level is SELinux level label that applies to the container.   
`sidecars[].securityContext.seLinuxOptions.role`  
`string`  
 _Optional_ |  Role is a SELinux role label that applies to the container.   
`sidecars[].securityContext.seLinuxOptions.type`  
`string`  
 _Optional_ |  Type is a SELinux type label that applies to the container.   
`sidecars[].securityContext.seLinuxOptions.user`  
`string`  
 _Optional_ |  User is a SELinux user label that applies to the container.   
`sidecars[].securityContext.seccompProfile`  
`object`  
 _Optional_ |  The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.   
`sidecars[].securityContext.seccompProfile.localhostProfile`  
`string`  
 _Optional_ |  localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.   
`sidecars[].securityContext.seccompProfile.type`  
`string`  
 _Required_ |  type indicates which kind of seccomp profile will be applied. Valid options are: \n Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.   
`sidecars[].securityContext.windowsOptions`  
`object`  
 _Optional_ |  The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.   
`sidecars[].securityContext.windowsOptions.gmsaCredentialSpec`  
`string`  
 _Optional_ |  GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.   
`sidecars[].securityContext.windowsOptions.gmsaCredentialSpecName`  
`string`  
 _Optional_ |  GMSACredentialSpecName is the name of the GMSA credential spec to use.   
`sidecars[].securityContext.windowsOptions.hostProcess`  
`boolean`  
 _Optional_ |  HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.   
`sidecars[].securityContext.windowsOptions.runAsUserName`  
`string`  
 _Optional_ |  The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
`sidecars[].startupProbe`  
`object`  
 _Optional_ |  StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].startupProbe.exec`  
`object`  
 _Optional_ |  Exec specifies the action to take.   
`sidecars[].startupProbe.exec.command`  
`list (string)`  
_Optional_ |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's file system. The command is exec'd, it is not run inside a shell, so standard shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
`sidecars[].startupProbe.exec.command[]`  
`string`  
 _Optional_ |   
`sidecars[].startupProbe.failureThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`sidecars[].startupProbe.grpc`  
`object`  
 _Optional_ |  GRPC specifies an action involving a GRPC port.   
`sidecars[].startupProbe.grpc.port`  
`integer`  
 _Required_ |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`sidecars[].startupProbe.grpc.service`  
`string`  
 _Optional_ |  Service is the name of the service to place in the gRPC HealthCheckRequest (see https://github.com/grpc/grpc/blob/master/doc/health-checking.md). \n If this is not specified, the default behavior is defined by gRPC.   
`sidecars[].startupProbe.httpGet`  
`object`  
 _Optional_ |  HTTPGet specifies the http request to perform.   
`sidecars[].startupProbe.httpGet.host`  
`string`  
 _Optional_ |  Hostname to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`sidecars[].startupProbe.httpGet.httpHeaders`  
`list (object)`  
_Optional_ |  Custom headers to set in the request. HTTP allows repeated headers.   
`sidecars[].startupProbe.httpGet.httpHeaders[]`  
`object`  
 _Optional_ |  HTTPHeader describes a custom header to be used in HTTP probes   
`sidecars[].startupProbe.httpGet.httpHeaders[].name`  
`string`  
 _Required_ |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`sidecars[].startupProbe.httpGet.httpHeaders[].value`  
`string`  
 _Required_ |  The header field value   
`sidecars[].startupProbe.httpGet.path`  
`string`  
 _Optional_ |  Path to access on the HTTP server.   
`sidecars[].startupProbe.httpGet.port`  
`integer or string`  
 _Required_ |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].startupProbe.httpGet.scheme`  
`string`  
 _Optional_ |  Scheme to use for connecting to the host. Defaults to HTTP.   
`sidecars[].startupProbe.initialDelaySeconds`  
`integer`  
 _Optional_ |  Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].startupProbe.periodSeconds`  
`integer`  
 _Optional_ |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`sidecars[].startupProbe.successThreshold`  
`integer`  
 _Optional_ |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`sidecars[].startupProbe.tcpSocket`  
`object`  
 _Optional_ |  TCPSocket specifies an action involving a TCP port.   
`sidecars[].startupProbe.tcpSocket.host`  
`string`  
 _Optional_ |  Optional: Hostname to connect to, defaults to the pod IP.   
`sidecars[].startupProbe.tcpSocket.port`  
`integer or string`  
 _Required_ |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`sidecars[].startupProbe.terminationGracePeriodSeconds`  
`integer`  
 _Optional_ |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately using the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`sidecars[].startupProbe.timeoutSeconds`  
`integer`  
 _Optional_ |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes   
`sidecars[].stdin`  
`boolean`  
 _Optional_ |  Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.   
`sidecars[].stdinOnce`  
`boolean`  
 _Optional_ |  Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false   
`sidecars[].terminationMessagePath`  
`string`  
 _Optional_ |  Optional: Path at which the file to which the container's termination message will be written is mounted into the container's file system. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.   
`sidecars[].terminationMessagePolicy`  
`string`  
 _Optional_ |  Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.   
`sidecars[].tty`  
`boolean`  
 _Optional_ |  Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.   
`sidecars[].volumeDevices`  
`list (object)`  
_Optional_ |  volumeDevices is the list of block devices to be used by the container.   
`sidecars[].volumeDevices[]`  
`object`  
 _Optional_ |  volumeDevice describes a mapping of a raw block device within a container.   
`sidecars[].volumeDevices[].devicePath`  
`string`  
 _Required_ |  devicePath is the path inside of the container that the device will be mapped to.   
`sidecars[].volumeDevices[].name`  
`string`  
 _Required_ |  name must match the name of a persistentVolumeClaim in the pod   
`sidecars[].volumeMounts`  
`list (object)`  
_Optional_ |  Pod volumes to mount into the container's file system. Cannot be updated.   
`sidecars[].volumeMounts[]`  
`object`  
 _Optional_ |  VolumeMount describes a mounting of a Volume within a container.   
`sidecars[].volumeMounts[].mountPath`  
`string`  
 _Required_ |  Path within the container at which the volume should be mounted. Must not contain ':'.   
`sidecars[].volumeMounts[].mountPropagation`  
`string`  
 _Optional_ |  mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.   
`sidecars[].volumeMounts[].name`  
`string`  
 _Required_ |  This must match the Name of a Volume.   
`sidecars[].volumeMounts[].readOnly`  
`boolean`  
 _Optional_ |  Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.   
`sidecars[].volumeMounts[].subPath`  
`string`  
 _Optional_ |  Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).   
`sidecars[].volumeMounts[].subPathExpr`  
`string`  
 _Optional_ |  Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.   
`sidecars[].workingDir`  
`string`  
 _Optional_ |  Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.   
  
## Status schema

SidecarStatus specifies the observed state of Sidecar.
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    criticalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams:
      resource:
        component: string
        location:
          cluster: string
          group: string
          kind: string
          name: string
          namespace: string
          version: string
      stackTrace:
      - component: string
        message: string
      transientUntil: string
    observedGeneration: integer
    reconciled: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`conditions`  
`list (object)`  
_Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`conditions[]`  
`object`  
 _Optional_ |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, \n type FooStatus struct{ // Represents the observations of a foo's current state. // Known .status.conditions.type are: \"Available\", \"Progressing\", and \"Degraded\" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:\"conditions,omitempty\" patchStrategy:\"merge\" patchMergeKey:\"type\" protobuf:\"bytes,1,rep,name=conditions\"` \n // other fields }   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`conditions[].message`  
`string`  
 _Required_ |  Maximum length: 32768 message is a human readable message indicating details about the transition. This may be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  Minimum length: 1; Maximum length: 1024 reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Valid values: `"True"`, `"False"`, `Unknown` status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  Maximum length: 316 type of condition in CamelCase or in foo.example.com/CamelCase. \--- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)   
`criticalIncidents`  
`list (object)`  
_Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[]`  
`object`  
 _Optional_ |  CriticalIncident contains all information about an ongoing critical incident.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident/error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the UI.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident as well as about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  Version is the Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace`  
`list (object)`  
_Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace[]`  
`object`  
 _Optional_ |  CriticalIncidentStackTraceMessage contains stack trace information available for the incident.   
`criticalIncidents[].stackTrace[].component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace[].message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  TransientUntil if present indicates that the issue should be considered transient until the specified time.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
