---
url: https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest/
title: Viewing a Manifest \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:11.057087+00:00
---

# Viewing a Manifest  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Viewing a Manifest Stay organized with collections  Save and categorize content based on your preferences. 

Each deployment has a corresponding manifest. A manifest is a read-only property that describes all the resources in your deployment and is automatically created with each new deployment. Manifests are not modifiable after they have been created. A manifest is not the same as a configuration file, but is created based on the configuration file.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand [configurations](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * Understand [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates).
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file).



## Manifest structure

A manifest provides three views of a deployment:

  * The initial configuration
  * The fully-evaluated configuration after all templates and imports have been expanded
  * The _layout_ of the deployment, which describes all the resources for the deployment in a hierarchical structure.



### Original configuration

The original configuration is the configuration you provided to the deployment, before any template expansion. The initial configuration is indicated by the `config` property:
    
    
    config: |
      imports:
      - path: vm-template.jinja
      - path: network-template.jinja
      - path: firewall-template.jinja
      - path: compute-engine-template.jinja
    
      resources:
      - name: compute-engine-setup
        type: compute-engine-template.jinja
    

### Expanded configuration

The expanded configuration is a full description of your deployment, including all resources and their properties, after processing all your templates. This is the final state of your configuration.

The expanded configuration portion of your manifest is indicated by the `expandedConfig` property:
    
    
    expandedConfig: |
      resources:
      - name: datadisk-example-config-with-templates
        properties:
          sizeGb: 100
          type: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/diskTypes/pd-standard
          zone: us-central1-a
        type: compute.v1.disk
      - name: vm-example-config-with-templates
        properties:
          disks:
          - autoDelete: true
            boot: true
            deviceName: boot
            initializeParams:
              diskName: disk-example-config-with-templates
              sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619
            type: PERSISTENT
          - autoDelete: true
            deviceName: datadisk-example-config-with-templates
            source: $(ref.datadisk-example-config-with-templates.selfLink)
            type: PERSISTENT
          machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/f1-micro
          metadata:
            items:
            - key: startup-script
              value: |
                #!/bin/bash
                python -m http.server 8080
          networkInterfaces:
          - accessConfigs:
            - name: External NAT
              type: ONE_TO_ONE_NAT
            network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default
          zone: us-central1-a
        type: compute.v1.instance

### Imported templates

The `imports` property in your manifest shows the content of any templates you imported for this configuration. The imports section of your manifest is indicated by the `imports` section:
    
    
    imports:
    - content: |
        resources:
        - name: {{ env["name"] }}
          type: compute.v1.instance
          properties:
            disks:
            - autoDelete: true
              type: PERSISTENT
              boot: true
              deviceName: boot
              initializeParams:
                sourceImage:  https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619
            machineType: https://www.googleapis.com/compute/v1/projects/{{ env["project"] }}/zones/{{ properties["zone"] }}/machineTypes/{{ properties["machineType"] }}
            networkInterfaces:
            - network: $(ref.{{ properties["network"] }}.selfLink)
              accessConfigs:
              - name: External NAT
                type: ONE_TO_ONE_NAT
            zone: {{ properties["zone"] }}
            metadata:
              items:
              - key: startup-script
                value: |
                  #!/bin/bash
                  INSTANCE=$(curl http://metadata.google.internal/computeMetadata/v1/instance/hostname -H "Metadata-Flavor: Google")
                  echo "<html><header><title>Hello from Deployment Manager!</title></header>
                  <body><h2>Hello from $INSTANCE</h2>
                  <p>Deployment Manager bids you good day!</p>
                  </body>
                  </html>" > index.html
                  python -m http.server 80
      name: vm-template.jinja
    - content: |
        resources:
        - name: {{ env["name"] }}
          type: compute.v1.network
          properties:
            IPv4Range: 10.0.0.1/16
      name: network-template.jinja
    - content: |
        resources:
        - name: {{ env["name"]}}
          type: compute.v1.firewall
          properties:
            network: $(ref.{{ properties["network"] }}.selfLink)
            sourceRanges: ["0.0.0.0/0"]
            allowed:
            - IPProtocol: TCP
              ports: ["80"]
      name: firewall-template.jinja
    - content: |
        {% set  NETWORK_NAME = "a-new-network" %}
    
        resources:
        - name: the-first-vm
          type: vm-template.jinja
          properties:
            machineType: f1-micro
            zone: us-central1-f
            network: {{ NETWORK_NAME }}
        - name: the-second-vm
          type: vm-template.jinja
          properties:
            machineType: g1-small
            zone: us-central1-f
            network: {{ NETWORK_NAME }}
        - name: {{ NETWORK_NAME }}
          type: network-template.jinja
        - name: {{ NETWORK_NAME }}-firewall
          type: firewall-template.jinja
          properties:
            network: {{ NETWORK_NAME }}
      name: compute-engine-template.jinja

### Layout

The layout is an outline of your deployment and its resources, and shows the resource names and types.

Use the layout to visualize the structure of your deployment, view template properties that were set during the initial deployment, and other information about your configuration before it was expanded.

In your manifest, you can see the layout in the `layout` property:
    
    
    layout: |
      resources:
      - name: compute-engine-setup
        resources:
        - name: the-first-vm
          properties:
            machineType: f1-micro
            network: a-new-network
            zone: us-central1-f
          resources:
          - name: the-first-vm
            type: compute.v1.instance
          type: vm-template.jinja
        - name: the-second-vm
          properties:
            machineType: g1-small
            network: a-new-network
            zone: us-central1-f
          resources:
          - name: the-second-vm
            type: compute.v1.instance
          type: vm-template.jinja
        - name: a-new-network
          resources:
          - name: a-new-network
            type: compute.v1.network
          type: network-template.jinja
        - name: a-new-network-firewall
          properties:
            network: a-new-network
          resources:
          - name: a-new-network-firewall
            type: compute.v1.firewall
          type: firewall-template.jinja
        type: compute-engine-template.jinja
    

## Identify a manifest

You can identify a manifest by its unique ID, in the format `manifest-TIMESTAMP`. For example:
    
    
    manifest-1436393348324
    

Usually, you can get the manifest ID by getting information about the corresponding deployment, or by listing manifests for a deployment.

###  gcloud 

With the Google Cloud CLI, use the `deployments describe` sub-command:
    
    
    gcloud deployment-manager deployments describe example-deployment
    

`gcloud` returns a response similar to the following:
    
    
    id: '7428522736135856060'
    manifest: https://www.googleapis.com/deploymentmanager/v2beta1/projects/myproject/global/deployments/example-deployment/manifests/manifest-1436393348324
    name: example-deployment
    resources:
    NAME    TYPE      ID     STATE   ERRORS
    ...

###  API 

In the API, make a `GET` request, providing the deployment name in the request:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta1/projects/myproject/global/deployments/example-deployment-with-config
    

You should receive a response similar to the following:
    
    
    {
     "id": "5899501332770090517",
     "creationTimestamp": "2015-03-30T15:40:58.809-07:00",
     "name": "example-deployment-with-config",
     "fingerprint": "",
     "manifest": "https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-deployment-with-config/manifests/manifest-1427755258810-2b3498d9-530b-4f8e-b014-0342d3c9c66b",
     "state": "DEPLOYED"
    }

## View a manifest

You can view a manifest by making a [`get()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/manifests/get) request to a Manifest resource or through the [Google Cloud console](https://console.cloud.google.com/) or `gcloud`.

###  Console 

To view a manifest of a deployment in the [Google Cloud console](https://console.cloud.google.com/):

  1. Go to the [**Deployments**](https://console.cloud.google.com/project/_/deployments) page in the Google Cloud console.
  2. From the list, click the deployment that you want to view.
  3. In the deployment's details, click **Overview**.



###  gcloud 

With the Google Cloud CLI, view the full manifest using the `manifests describe` command. The command lists both the full manifest and the layout:
    
    
    gcloud deployment-manager manifests describe manifest-1436393348324 \
        --deployment example-config-with-templates
    

`gcloud` returns a response similar to the following:
    
    
     config: |
       imports: ["vm_template.jinja"]
    
    
    
    resources:
    
    
    
    

  * name: vm-instance type: vm_template.jinja properties: zone: us-central1-a project: myproject creationTimestamp: '2015-03-30T15:40:58.815-07:00' evaluatedConfig: | resources:
  * name: datadisk-example-config-with-templates properties: sizeGb: 100 type: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/diskTypes/pd-standard zone: us-central1-a type: compute.v1.disk
  * name: vm-example-config-with-templates properties: disks:
    * autoDelete: true boot: true deviceName: boot initializeParams: diskName: disk-example-config-with-templates sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619 type: PERSISTENT
    * autoDelete: true deviceName: datadisk-example-config-with-templates source: $(ref.datadisk-example-config-with-templates.selfLink) type: PERSISTENT machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/f1-micro metadata: items:
      * key: startup-script value: | #!/bin/bash python -m http.server 8080 networkInterfaces:
    * accessConfigs:
      * name: External NAT type: ONE_TO_ONE_NAT network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default zone: us-central1-a type: compute.v1.instance id: '7174699452487462421' layout: | resources:
  * name: vm-instance type: vm_template.jinja properties: project: myproject zone: us-central1-a resources:
    * name: datadisk-example-config-with-templates type: compute.v1.disk
    * name: vm-example-config-with-templates type: compute.v1.instance name: manifest-1427755258810-2b3498d9-530b-4f8e-b014-0342d3c9c66b selfLink: https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-config-with-templates/manifests/manifest-1436393348324



###  API 

In the API, provide the deployment name and the manifest name in a `GET` request:
    
    
     GET https://www.googleapis.com/deploymentmanager/v2beta1/projects/myproject/global/deployments/example-deployment/manifests/manifest-1436393348324
    

You should receive a response similar to the following:
    
    
    {
     "id": "7174699452487462421",
     "selfLink": "https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-config-with-templates/manifests/manifest-1436393348324",
     "creationTimestamp": "2015-03-30T15:40:58.815-07:00",
     "name": "manifest-1427755258810-2b3498d9-530b-4f8e-b014-0342d3c9c66b",
     "config": "imports: [\"vm_template.jinja\"]\n\nresources:\n- name: vm-instance\n  type: vm_template.jinja\n  properties:\n    zone: us-central1-a\n    project: myproject\n",
     "evaluatedConfig": "resources:\n- name: datadisk-example-config-with-templates\n  properties:\n    sizeGb: 100\n    type: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/diskTypes/pd-standard\n    zone: us-central1-a\n  type: compute.v1.disk\n- name: vm-example-config-with-templates\n  properties:\n    disks:\n    - autoDelete: true\n      boot: true\n      deviceName: boot\n      initializeParams:\n        diskName: disk-example-config-with-templates\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619\n      type: PERSISTENT\n    - autoDelete: true\n      deviceName: datadisk-example-config-with-templates\n      source: $(ref.datadisk-example-config-with-templates.selfLink)\n      type: PERSISTENT\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/f1-micro\n    metadata:\n      items:\n      - key: startup-script\n        value: |\n          #!/bin/bash\n          python -m http.server 8080\n    networkInterfaces:\n    - accessConfigs:\n      - name: External NAT\n        type: ONE_TO_ONE_NAT\n      network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default\n    zone: us-central1-a\n  type: compute.v1.instance\n",
     "layout": "resources:\n- name: vm-instance\n  properties:\n    project: myproject\n    zone: us-central1-a\n  resources:\n  - name: datadisk-example-config-with-templates\n    type: compute.v1.disk\n  - name: vm-example-config-with-templates\n    type: compute.v1.instance\n  type: vm_template.jinja\n"
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


