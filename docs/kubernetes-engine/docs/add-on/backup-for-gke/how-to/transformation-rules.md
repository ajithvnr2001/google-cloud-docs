---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/transformation-rules/
title: Modify resources during restoration \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:02.656855+00:00
---

# Modify resources during restoration  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/transformation-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Modify resources during restoration Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to make modifications to Kubernetes resources during the restoration process using transformation rules. Transformation rules are intended as an improvement over a previous feature called substitution rules. Because they are not backward compatible with substitution rules, the deprecated substitution rules interface is still available.

To view the documentation for substitution rules, see [Modify resources during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/substitution-rules).

## Overview

There are several reasons why you might want to modify Kubernetes resources as part of the restore process:

  * You might want to create a PersistentVolumeClaim (PVC) using a different storage provisioner. For example, you want to move from the Kubernetes in-tree driver to the CSI driver.

  * You might want to restore a namespace under a different name.

  * You might want to add, change, or delete the value associated with a label or ConfigMap key.

  * You might want to change a replica count in a Deployment or StatefulSet.




Backup for GKE provides a mechanism for making these changes called _transformation rules_ , which you may optionally define as part of a [`RestorePlan`](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

In the restore process, transformation rules work as follows:

  1. Rules are organized into an ordered list.

  2. All the resources—except `CustomResourceDefinition` resources, for which transformations are not available—to be restored move sequentially through this list of rules.

  3. Each rule contains a short description, matching criteria, and resource edits.

  4. If a resource does not match a rule's criteria, then it moves to the next rule in the list without modification.

  5. If a resource matches a rule's criteria, then the rule's edits are applied to the resource before it moves to the next rule on the list.

  6. If multiple rules are defined, then each rule's matching criteria is evaluated against the version of the resource modified by previous rules.

  7. The final version of the resource, after any matching rule's edits are applied, is what is created in the cluster.




## Transformation rule parameters

You create a transformation rule by supplying the following information:

  * `description`: This is a short description of the transformation rule.

  * `resourceFilter`: This filter is used to match against resources. If no `resourceFilter` is provided, all resources match this rule.

  * `fieldActions`: This is a list of edits to make to the resources that match the `resourceFilter`. The edits are provided as an ordered list of actions. Order matters here because the outcome of one action can affect the next action in the list. If any action fails, the entire restore will fail.




### Resource filter (`resourceFilter`)

To define a resource filter, you provide the following parameters:

**Parameter** | **Required** | **Description**  
---|---|---  
`namespaces` | optional |  This is a list of namespaces. For a resource to match this rule, it must be a namespaced resource and have one of the given namespaces. If nothing is provided for this parameter, then all resources will match (all namespaced and cluster-scoped resources).   
`groupKinds` | optional |  This is a list of Kubernetes resource `Group/Kind` tuples:   


  * If nothing is provided for this parameter, then all resources will match with no restrictions based on `Group/Kind`. 
  * If one or more `Group/Kind` is supplied, then resources must match one of them in order to match the rule. 
To match against core resources, use an empty ("") group. 
  
`jsonPath` | optional |  This is a [JSONPath](https://github.com/json-path/JsonPath/blob/master/README.md) expression that is used to match against resources.   
  
#### JSONPath (`jsonPath`)

A [JSONPath](https://github.com/json-path/JsonPath/blob/master/README.md) expression is used to match against resources. If the result of the expression is not empty against a resource, then this resource is considered matched.

Given the following resource:

### YAML
    
    
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: mysql-cm
      labels:
        app: mysql
        app.kubernetes.io/name: mysql
    data:
      primary.cnf: |
        # Apply this config only on the primary.
        [mysqld]
        log-bin
      replica.cnf: |
        # Apply this config only on replicas.
        [mysqld]
        super-read-only
    

### JSON
    
    
    {
      "apiVersion": "v1",
      "kind": "ConfigMap",
      "metadata": {
        "name": "mysql-cm",
        "labels": {
          "app": "mysql",
          "app.kubernetes.io/name": "mysql"
        }
      },
      "data": {
        "primary.cnf": "# Apply this config only on the primary.\n[mysqld]\nlog-bin\n",
        "replica.cnf": "# Apply this config only on replicas.\n[mysqld]\nsuper-read-only\n"
      }
    }
    

Example of using JSONPath expressions:

**Expression** | **Description** | **Result**  
---|---|---  
`.metadata[?(@.name == 'mysql-cm')]` | The `metadata` object contains `name` key and its value is "mysql-cm" | ` [  
{  
"name": "mysql-cm",  
"labels": {  
"app": "mysql",  
"app.kubernetes.io/name": "mysql"  
}  
}  
]`  
`.metadata.labels['app.kubernetes.io/name']` | The string value of key "app.kubernetes.io/name" under `metadata.labels` | ` [  
"mysql"  
]`  
`.data['primary.cnf']` | The object value of key "primary.cnf" under `data` | ` [  
"# Apply this config only on the primary.\n[mysqld]\nlog-bin\n"  
]`  
`.metadata[?(@.name =~ /^mysql-.*/)]` | The `metadata` object contains `name` key and its value matches the regular expression "/^mysql-.*/i".  
The forward slashes `/` are used to delimit the regular expression pattern. The `i` at the end of the regular expression is the flag for case-insensitive matching. | ` [  
{  
"name": "mysql-cm",  
"labels": {  
"app": "mysql",  
"app.kubernetes.io/name": "mysql"  
}  
}  
]`  
  
As long as the output of the JSONPath expression is not empty, the corresponding resource will match this rule. Thus, `.metadata[?(@.name == 'mysql-cm')]` and `.metadata[?(@.name == 'mysql-cm')].name` result in the same matching result, which is matching the resource whose `.metadata.name` is `"mysql-cm"`.

If a map key in JSONPath contains a `.` (dot), use the bracket notation with single quotes (for example, `['app.kubernetes.io/name']` or `['primary.cnf']`). The `.` character does not need to be escaped within the single quotes.

We recommend using a JSONPath evaluator tool with regular expression support to test the expression before use. You can also use `kubectl` to verify the result of JSONPath expressions. See [JSONPath Support](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for more examples.

**Note:** `kubectl` does not support regular expression match and filters can be only targeted against an array and slice instead of a object.

### Field action (`fieldActions`)

Field actions are modeled based on [JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902), which defines a JSON document structure for expressing an operation to apply to a JSON document. To define a field action, the following parameters are required:

  * `path`: This is a [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) value that references the location in target resources where the operation is performed. JSON pointers always start with a `/` (slash), and the property names (keys) descend into child elements are also separated by a `/` (slash).

**Note:** If a property name contains `~` (tilde), then inside the pointer it must be escaped using `~0`, or if contains `/` (forward slash), then it must be escaped using `~1`.
  * `op`: This is the type of the operation performed against resources, five operations are supported:

    * `add` inserts a new object or value to the specified `path`, depending upon what the `path` references.
    * `remove` removes the value from the specified `path`.
    * `replace` replaces the value at the specified `path` with a new value.
    * `move` removes the value from a location and adds it to the specified `path`.
    * `copy` copies the value from a location to the specified `path`.



You can find examples of each operation, using the following Pod definition:

### YAML
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### JSON
    
    
    {
      "apiVersion": "v1",
      "kind": "Pod",
      "metadata": {
        "name": "nginx",
        "namespace": "ns",
        "labels": {
          "app": "nginx"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:latest",
            "ports": [
              {
                "containerPort": 80
              }
            ],
            "env": [
              {
                "name": "PROTOCOL",
                "value": "https"
              }
            ],
            "resources": {
              "limits": {
                "cpu": "250m",
                "memory": "64Mi"
              }
            }
          }
        ],
        "initContainers": [
          {
            "name": "install",
            "image": "busybox:stable",
            "command": [
              "wget",
              "-O",
              "/tmp/index.html",
              "http://info.cern.ch"
            ]
          }
        ]
      }
    }
    

#### Add

`value` is always required for `add` operations, and must be a legal JSON element.

This following action adds a new environment variable `"PORT"` with value `"80"` to the `nginx` container.
    
    
    op: add
    path: "/spec/containers/0/env/0"
    value: >
      {
        "name": "PORT",
        "value": "80"
      }
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        - name: PORT  # newly added
          value: "80"  # newly added
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

The following action adds value to a new label `app.kubernetes.io/name: nginx` to the Pod.
    
    
    op: add
    path: "/metadata/labels/app.kubernetes.io~1name"
    value: "nginx"
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
        app.kubernetes.io/name: nginx  # newly added
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

The following action replaces the image of `nginx` container to change it from `"nginx:latest"` to `"nginx:stable"`.
    
    
    op: add
    path: "/spec/containers/0/image"
    value: nginx:stable
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:stable  # replaced
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

**Note:** An `add` operation is equivalent to `replace` operation if the `path` specifies an object member that already exists.

#### Remove

The following action removes the resource requirements for the `nginx` container.
    
    
    op: remove
    path: "/spec/containers/0/resources"
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        # resource requirements are removed
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

#### Replace

`value` is required for `replace` operation, and it has to be a JSON element.

The following action replaces the image of the `nginx` container from `nginx:latest` to `nginx:stable`.
    
    
    op: replace
    path: "/spec/containers/0/image"
    value: nginx:stable
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:stable  # replaced
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

#### Move

`fromPath` is required for `move` operation.

The following action removes environment variables from the `nginx` container and adds them to the `install` init container.
    
    
    op: move
    fromPath: "/spec/containers/0/env"
    path: "/spec/initContainers/0/env"
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        #  "env" is moved to "install" container
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
        env:  # moved "from" nginx container
        - name: PROTOCOL
          value: https
    

#### Copy

`fromPath` is required for `copy` operation.

The following action copies environment variables from the `nginx` container to the `install` init container.
    
    
    op: copy
    fromPath: "/spec/containers/0/env"
    path: "/spec/initContainers/0/env"
    

### Original
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
    

### Transformed
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      namespace: ns
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: PROTOCOL
          value: "https"
        resources:
          limits:
            cpu: "250m"
            memory: "64Mi"
      initContainers:
      - name: install
        image: busybox:stable
        command:
        - wget
        - "-O"
        - "/tmp/index.html"
        - http://info.cern.ch
        env:  # copy from "nginx" container
        - name: PROTOCOL
          value: https
    

To learn more about defining transformation rules in the Google Cloud console, see [Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

To define transformation rules through gcloud CLI, create a file containing a YAML array of `transformationRules` and include the `--transformation-rules-file=` parameter in the [`gcloud beta container backup-restore restore-plans create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/create) command.

## Transformation rule examples

The following examples are provided in the YAML format used by gcloud CLI or the Terraform Configuration Language.

### Change StorageClass of PVCs

This example changes the StorageClass in all restored PersistentVolumeClaim resources from `standard` to `premium-rwo`:

### YAML
    
    
    transformationRules:
    - description: Change StorageClass in PVC from standard to premium-rwo
      resourceFilter:
        namespaces: []
        jsonPath: ".spec[?(@.storageClassName == 'standard')]"
        groupKinds:
        - resourceGroup: ""
          resourceKind: PersistentVolumeClaim
      fieldActions:
      - op: REPLACE
        path: "/spec/storageClassName"
        value: "premium-rwo"
    

### Terraform
    
    
    transformation_rules {
      description = "Change StorageClass in PVC from standard to premium-rwo"
      resource_filter {
        json_path = ".spec[?(@.storageClassName == 'standard')]"
        group_kinds {
          resource_kind = "PersistentVolumeClaim"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/spec/storageClassName"
        value = "premium-rwo"
      }
    }
    

**Note:** To change the StorageClass of PVC templates defined in the StatefulSet, a separate transformation rule has to be configured.

### Clone a Namespace

This example clones a namespace from alpha to beta—creating a new namespace `"beta"` and restoring all of the resources from `"alpha"` into the new `"beta"` namespace. This example requires two transformation rules—one for the namespace itself, and one for the resources within the namespace.

### YAML
    
    
    transformationRules:
    - description: Rename namespace name from alpha to beta
      resourceFilter:
        namespaces: []
        jsonPath: ".metadata[?(@.name == 'alpha')]"
        groupKinds:
        - resourceGroup: ""
          resourceKind: Namespace
      fieldActions:
      - op: REPLACE
        path: "/metadata/name"
        value: "beta"
    - description: Clone all resources from namespace alpha to beta
      resourceFilter:
        namespaces: ["alpha"]
      fieldActions:
      - op: REPLACE
        path: "/metadata/namespace"
        value: "beta"
    

### Terraform
    
    
    transformation_rules {
      description = "Rename namespace name from alpha to beta"
      resource_filter {
        json_path = ".metadata[?(@.name == 'alpha')]"
        group_kinds {
          resource_kind = "Namespace"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/metadata/name"
        value = "beta"
      }
    }
    transformation_rules {
      description = "Clone all resources from namespace alpha to beta"
      resource_filter {
        namespaces = ["alpha"]
      }
      field_actions {
        op = "REPLACE"
        path = "/metadata/namespace"
        value = "beta"
      }
    }
    

### Change StorageClass of PVCs and replica count in a cloned namespace

This example clones a namespace, and then applies a set of changes to resources in the new namespace:

  * Change the StorageClass on PVCs from `standard` to `premium-rwo`

  * Change the replica count of the Deployment `nginx` to `3`




### YAML
    
    
    transformationRules:
    - description: Rename the namespace from alpha to beta
      resourceFilter:
        namespaces: []
        jsonPath: ".metadata[?(@.name == 'alpha')]"
        groupKinds:
        - resourceGroup: ""
          resourceKind: Namespace
      fieldActions:
      - op: REPLACE
        path: "/metadata/name"
        value: "beta"
    - description: Change all resources from namespace alpha to beta
      resourceFilter:
        namespaces: ["alpha"]
      fieldActions:
      - op: REPLACE
        path: "/metadata/namespace"
        value: "beta"
    - description: Change the StorageClass on PVCs from standard to premium-rwo
      resourceFilter:
        namespaces: ["beta"]
        jsonPath: ".spec[?(@.storageClassName == 'standard')]"
        groupKinds:
        - resourceGroup: ""
          resourceKind: PersistentVolumeClaim
      fieldActions:
      - op: REPLACE
        path: "/spec/storageClassName"
        value: "premium-rwo"
    - description: Change the replica count of the Deployment nginx from 7 to 3
      resourceFilter:
        namespaces: ["beta"]
        jsonPath: ".metadata[?(@.name == 'nginx')]"
        groupKinds:
        - resourceGroup: apps
          resourceKind: Deployment
      fieldActions:
      - op: REPLACE
        path: "/spec/replicas"
        value: "3"
    

### Terraform
    
    
    transformation_rules {
      description = "Rename the namespace from alpha to beta"
      resource_filter {
        json_path = ".metadata[?(@.name == 'alpha')]"
        group_kinds {
          resource_kind = "Namespace"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/metadata/name"
        value = "beta"
      }
    }
    transformation_rules {
      description = "Change all resources from namespace alpha to beta"
      resource_filter {
        namespaces = ["alpha"]
      }
      field_actions {
        op = "REPLACE"
        path = "/metadata/namespace"
        value = "beta"
      }
    }
    transformation_rules {
      description = "Change the StorageClass on PVCs from standard to premium-rwo"
      resource_filter {
        namespaces = ["beta"]
        json_path = ".spec[?(@.storageClassName == 'standard')]"
        group_kinds {
          resource_kind = "PersistentVolumeClaim"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/spec/storageClassName"
        value = "premium-rwo"
      }
    }
    transformation_rules {
      description = "Change the replica count of the Deployment nginx from 7 to 3"
      resource_filter {
        namespaces = ["beta"]
        json_path = ".metadata[?(@.name == 'nginx')]"
        group_kinds {
          resource_group = "apps"
          resource_kind = "Deployment"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/spec/replicas"
        value = "3"
      }
    }
    

### Change, insert, and remove ConfigMap entries

This example modifies the `ConfigMap` that contains the label key `"app.kubernetes.io/name"` in the namespace `"mysql"` to:

  * Change the value of the entry `"endpoint"` to `"192.0.2.127"`.

  * Insert a new entry `"connection-timeout"` with value `"30s"`.

  * Remove the entry with the key `"read-timeout"`.




### YAML
    
    
    transformationRules:
    - description: Change, insert, remove `ConfigMap` entries
      resourceFilter:
        namespaces: ["mysql"]
        jsonPath: ".metadata.labels['app.kubernetes.io/name']"
        groupKinds:
        - resourceGroup: ""
          resourceKind: ConfigMap
      fieldActions:
      - op: REPLACE
        path: "/data/endpoint"
        value: "192.0.2.127"
      - op: ADD
        path: "/data/connection-timeout"
        value: "30s"
      - op: REMOVE
        path: "/data/read-timeout"
    

### Terraform
    
    
    transformation_rules {
      description = "Change, insert, remove `ConfigMap` entries"
      resource_filter {
        namespaces = ["mysql"]
        json_path = ".metadata.labels['app.kubernetes.io/name']"
        group_kinds {
          resource_kind = "ConfigMap"
        }
      }
      field_actions {
        op = "REPLACE"
        path = "/data/endpoint"
        value = "192.0.2.127"
      }
      field_actions {
        op = "ADD"
        path = "/data/connection-timeout"
        value = "30s"
      }
      field_actions {
        op = "REMOVE"
        path = "/data/read-timeout"
      }
    }
    

### Add a label `app.kubernetes.io/name` to resources whose name starts with _mysql-_ ;

This example adds a label `app.kubernetes.io/name` with the value `mysql` to all resources whose name starts with _mysql-_ :

### YAML
    
    
    transformationRules:
    - description: Add a label to resources whose name starts with
      resourceFilter:
        namespaces: []
        jsonPath: ".metadata[?(@.name =~ /^mysql-.*/)]"
      fieldActions:
      - op: ADD
        path: "/metadata/labels/app.kubernetes.io~1name"
        value: "mysql"
    

### Terraform
    
    
    transformation_rules {
      description = "Add a label to resources whose name starts with"
      resource_filter {
        json_path = ".metadata[?(@.name =~ /^mysql-.*/)]"
      }
      field_actions {
        op = "ADD"
        path = "/metadata/labels/app.kubernetes.io~1name"
        value = "mysql"
      }
    }
    

### Assign a static IP address for a LoadBalancer type Service

This example assigns a static IP address for the Service `"nginx-svc"` in the namespace `"nginx"`:

### YAML
    
    
    transformationRules:
    - description: Assign a static IP to Service nginx-svc
      resourceFilter:
        namespaces: ["nginx"]
        jsonPath: ".metadata[?(@.name == 'nginx-svc')]"
        groupKinds:
        - resourceGroup: ""
          resourceKind: Service
      fieldActions:
      - op: ADD
        path: "/spec/loadBalancerIP"
        value: "192.0.2.127"
    

### Terraform
    
    
    transformation_rules {
      description = "Assign a static IP to Service nginx-svc"
      resource_filter {
        namespaces = ["nginx"]
        json_path = ".metadata[?(@.name == 'nginx-svc')]"
        group_kinds {
          resource_kind = "Service"
        }
      }
      field_actions {
        op = "ADD"
        path = "/spec/loadBalancerIP"
        value = "192.0.2.127"
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
