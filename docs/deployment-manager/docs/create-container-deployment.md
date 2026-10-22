---
url: https://docs.cloud.google.com/deployment-manager/docs/create-container-deployment/
title: Creating a Container-Optimized Deployment \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:04.568588+00:00
---

# Creating a Container-Optimized Deployment  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/create-container-deployment/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating a Container-Optimized Deployment Stay organized with collections  Save and categorize content based on your preferences. 

This full example describes how to create a deployment with a virtual machine that uses a container-optimized image. For more information on using containers with Compute Engine, see [Container-Optimized Compute Engine Images](https://docs.cloud.google.com/container-optimized-os/docs).

This walk-through describes how to:

  1. Create a simple container manifest.
  2. Create a configuration and template that uses a container image.
  3. Deploy your resources and verify that the deployment was successful.



## Create a container manifest

To use containers, you must define a container manifest. The manifest describes properties such as the container image, containers to launch, commands to execute on boot, and ports to enable.

Create a file named `container_manifest.yaml` with the following contents:
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    # This is a container manifest, as described here:
    #   https://cloud.google.com/compute/docs/containers/container_vms
    apiVersion: v1
    kind: Pod
    metadata:
      name: simple-echo
    spec:
      containers:
        - name: simple-echo
          image: gcr.io/google-samples/hello-app:2.0
          imagePullPolicy: Always
          ports:
            - containerPort: 8080
              hostPort: 8080
    

This manifest creates a container named simple-echo that uses the [Hello Application](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app) container image and launches an echo server that listens on port 8080.

## Create a template and configuration

Next, create a template that launches a virtual machine instance with a container-optimized image. Create a file named `container_vm.[jinja|py]` with the following contents:

###  Jinja 
    
    
    
    {% set COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/' %}
    {% set BASE_NAME = env['deployment'] + '-' + env['name'] %}
    
    {% macro GlobalComputeUrl(project, collection, name) -%}
    {{ COMPUTE_URL_BASE }}projects/{{ project }}/global/{{ collection }}/{{ name }}
    {%- endmacro %}
    
    {% macro ZonalComputeUrl(project, zone, collection, name) -%}
    {{ COMPUTE_URL_BASE }}projects/{{ project }}/zones/{{ zone }}/{{ collection }}/{{ name }}
    {%- endmacro %}
    
    resources:
    - name: {{ BASE_NAME }}
      type: compute.v1.instance
      properties:
        zone: {{ properties['zone'] }}
        machineType: {{ ZonalComputeUrl(env['project'], properties['zone'], 'machineTypes', 'n1-standard-1') }}
        metadata:
          items:
            - key: gce-container-declaration
              value: |
                {{ imports[properties['containerManifest']]|indent(12) }}
        disks:
          - deviceName: boot
            type: PERSISTENT
            autoDelete: true
            boot: true
            initializeParams:
              diskName: {{ BASE_NAME }}-disk
              sourceImage: {{ GlobalComputeUrl('cos-cloud', 'images', properties['containerImage']) }}
        networkInterfaces:
          - accessConfigs:
              - name: external-nat
                type: ONE_TO_ONE_NAT
            network: {{ GlobalComputeUrl(env['project'],  'networks', 'default') }}
        serviceAccounts:
          - email: default
            scopes:
            - https://www.googleapis.com/auth/logging.write
            - https://www.googleapis.com/auth/monitoring.write
    
    

###  Python 
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Creates a Container VM with the provided Container manifest."""
    
    
    COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
    
    
    def GlobalComputeUrl(project, collection, name):
      return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                      '/global/', collection, '/', name])
    
    
    def ZonalComputeUrl(project, zone, collection, name):
      return ''.join([COMPUTE_URL_BASE, 'projects/', project,
                      '/zones/', zone, '/', collection, '/', name])
    
    
    def GenerateConfig(context):
      """Generate configuration."""
    
      res = []
      base_name = (context.env['deployment'] + '-' +
                   context.env['name'])
    
      # Properties for the container-based instance.
      instance = {
          'zone': context.properties['zone'],
          'machineType': ZonalComputeUrl(context.env['project'],
                                         context.properties['zone'],
                                         'machineTypes',
                                         'n1-standard-1'),
          'metadata': {
              'items': [{
                  'key': 'gce-container-declaration',
                  'value': context.imports[
                      context.properties['containerManifest']],
                  }]
          },
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'autoDelete': True,
              'boot': True,
              'initializeParams': {
                  'diskName': base_name + '-disk',
                  'sourceImage': GlobalComputeUrl('cos-cloud',
                                                  'images',
                                                  context.properties[
                                                      'containerImage'])
                  },
          }],
          'networkInterfaces': [{
              'accessConfigs': [{
                  'name': 'external-nat',
                  'type': 'ONE_TO_ONE_NAT'
                  }],
              'network': GlobalComputeUrl(context.env['project'],
                                          'networks',
                                          'default')
          }],
          'serviceAccounts': [{
              'email': 'default',
              'scopes': [
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring.write"
              ]
          }]
      }
      res.append({
          'name': base_name,
          'type': 'compute.v1.instance',
          'properties': instance
      })
      # Resources to return.
      resources = {
          'resources': res,
      }
    
      return resources
    

Create the corresponding [schema file](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas), which enforces the structure of the template:

###  Jinja 
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    info:
      title: Container VM
      author: Google Inc.
      description: Creates a Container VM with the provided Container manifest.
    
    required:
      - zone
      - containerImage
      - containerManifest
    
    properties:
      zone:
        description: Zone in which this VM will run
        type: string
      containerImage:
        description: Name of the Google Cloud Container VM Image
        type: string
      containerManifest:
        description: String containing the Container Manifest in YAML
        type: string
    

###  Python 
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    info:
      title: Container VM
      author: Google Inc.
      description: Creates a Container VM with the provided Container manifest.
    
    required:
      - zone
      - containerImage
      - containerManifest
    
    properties:
      zone:
        description: Zone in which this VM will run
        type: string
      containerImage:
        description: Name of the Google Cloud Container VM Image
        type: string
      containerManifest:
        description: String containing the Container Manifest in YAML
        type: string
    

Notice there are a number of parameters defined in this template including:

  * The `deployment`, `name`, and `project` environment variables. Deployment Manager automatically populates those variables without additional action from you.
  * The `zone`, `containerImage`, and `containerManifest` properties, which will be defined in the configuration.



Create a configuration file named `container_vm.yaml` that looks like the following:

###  Jinja 
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    imports:
    - path: ../../common/container_manifest.yaml
      name: container_manifest
    - path: container_vm.jinja
    
    resources:
      - name: my-container-vm
        type: container_vm.jinja
        properties:
          zone: ZONE_TO_RUN
          containerImage: family/cos-stable
          containerManifest: container_manifest
    

###  Python 
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    imports:
    - path: ../../common/container_manifest.yaml
      name: container_manifest
    - path: container_vm.py
    
    resources:
      - name: my-container-vm
        type: container_vm.py
        properties:
          zone: ZONE_TO_RUN
          containerImage: family/cos-stable
          containerManifest: container_manifest
    

Make sure to replace `ZONE_TO_RUN` with the desired zone for your virtual machine. Notice that the file has also defined the container image to use and the container manifest that you created earlier.

## Deploy your virtual machine instance

Finally, deploy your virtual machine instance using the Google Cloud CLI:
    
    
    gcloud deployment-manager deployments create my-container-deployment \
      --config container_vm.yaml
    

Once the deployment has been created, you can view the details of your deployment. For example:
    
    
    $ gcloud deployment-manager deployments describe my-container-deployment
    creationTimestamp: '2015-04-02T12:24:31.645-07:00'
    fingerprint: ''
    id: '8602410885927938432'
    manifest: https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/my-container-deployment/manifests/manifest-1428002671645
    name: my-container-deployment
    state: DEPLOYED
    resources:
    NAME                                     TYPE                 ID                   UPDATE_STATE  ERRORS
    my-container-deployment-my-container-vm  compute.v1.instance  3775082612632070557  COMPLETED     -
    

## Verify that your instance is running

To test that your container instance started up, visit the virtual machine's external IP address in your browser, which should print `hello world`:

  1. Add a Compute Engine firewall rule to allow you to query traffic on the virtual machine through port 8080:
         
         gcloud compute firewall-rules create allow-8080 --allow tcp:8080
         

  2. Get your instance's external IP address:
         
         $ gcloud compute instances describe my-container-deployment-my-container-vm
         ...
         name: my-container-vm-my-container-deployment
         networkInterfaces:
         - accessConfigs:
           - kind: compute#accessConfig
             name: external-nat
             natIP: 104.197.8.138
             type: ONE_TO_ONE_NAT
           name: nic0
           network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default
           networkIP: 10.240.97.220
         scheduling:
           automaticRestart: true
           onHostMaintenance: MIGRATE
         selfLink: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/my-container-deployment-my-container-vm
         status: RUNNING
         tags:
           fingerprint: 42WmSpB8rSM=
         zone: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a
         ...

In this case, the external IP is `104.197.8.138`.

  3. In a browser window, enter in the external IP and port 8080 in the browser bar. For example, `104.197.8.138:8080`.

If successful, you should see a `hello world` message.




## (Optional) Delete your deployment

If you want to save on costs and no longer want or need your deployment, delete your deployment.
    
    
    gcloud deployment-manager deployments delete my-container-deployment
    

## What's next

Explore more about Deployment Manager in the [Complete User Guides](https://docs.cloud.google.com/deployment-manager/docs/configuration) or through the [API](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).

Try out some other tutorials:

  * [Create a network load-balanced logbook application](https://docs.cloud.google.com/deployment-manager/docs/create-advanced-deployment).
  * [Create a HTTP load-balanced logbook application](https://docs.cloud.google.com/deployment-manager/docs/create-advanced-http-load-balanced-deployment). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
