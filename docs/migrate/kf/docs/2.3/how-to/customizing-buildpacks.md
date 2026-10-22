---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/customizing-buildpacks/
title: Customizing Stacks and Buildpacks \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:09.087374+00:00
---

# Customizing Stacks and Buildpacks  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/customizing-buildpacks/

Version 2.3

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
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Customizing Stacks and Buildpacks Stay organized with collections  Save and categorize content based on your preferences. 

Buildpacks are used by Kf to turn an application's source code into an executable image. Cloud Native Buildpacks use the latest [Buildpack API v3](https://github.com/buildpack/spec) and companies including VMware and Heroku are actively adding v3 support to existing buildpacks.

Kf supports Buildpacks conforming to both [V2](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html) and [V3](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html) of the Buildpack API specification.

## Comparison between V2 and V3 buildpacks

| V2 Buildpacks | V3 Buildpacks  
---|---|---  
Alternate names | Cloud Foundry Buildpacks | Cloud Native Buildpacks (CNB), Builder Images  
Status | Being Replaced | Current  
Ownership | Cloud Foundry | [Buildpacks.io](https://buildpacks.io)  
Stack | Shared by builder and runtime | Optionally different for builder and runtime  
Local development | Not possible | Yes, with the [`pack` CLI](https://buildpacks.io)  
Custom buildpacks | Available at runtime | Must be built into the builder  
  
## Buildpack lifecycle

Step | Cloud Foundry | Kf with Buildpacks V2 | Kf with Buildpacks V3  
---|---|---|---  
Source location | BITS service | Container registry | Container registry  
Buildpack location | BOSH/HTTP | HTTP | Container registry  
Stack location | BOSH | Container registry | Container registry  
Result | Droplet (App binary without stack) | Image (Droplet on a stack) | Image  
Runtime | Droplet glued on top of stack and run | Run produced image | Run produced image  
  
Kf _always_ produces a full, executable image as a result of its build process. Cloud Foundry, on the other hand, produces parts of an executable image at build time and the rest is added at runtime.

Kf chose to follow the model of always producing a full image for the following reasons:

  * Images can be exported, run locally, and inspected statically
  * Better security and auditing with tools like [binary authorization](https://docs.cloud.google.com/binary-authorization)
  * App deployments are reproducible



## Kf and Buildpacks

Kf stores its global list of buildpacks and stacks in the `config-defaults` ConfigMap in the `kf` Namespace. Each Space reflects these buildpacks in its status field. For a Space named `buildpack-docs` you could run the following to see the full Space configuration:
    
    
    $ kf space buildpack-docs
    
    Getting Space buildpack-docs
    API Version:  kf.dev/v1alpha1
    Kind:         Space
    Metadata:
      Creation Timestamp:  2020-02-14T15:09:52Z
      Name:                buildpack-docs
      Self Link:           /apis/kf.dev/v1alpha1/spaces/buildpack-docs
      UID:                 0cf1e196-4f3c-11ea-91a4-42010a80008d
    Status:
      Build Config:
        Buildpacks V2:
        - Name:      staticfile_buildpack
          URL:       https://github.com/cloudfoundry/staticfile-buildpack
          Disabled:  false
        - Name:      java_buildpack
          URL:       https://github.com/cloudfoundry/java-buildpack
          Disabled:  false
        Stacks V2:
        - Image:  cloudfoundry/cflinuxfs3
          Name:   cflinuxfs3
        Stacks V3:
        - Build Image:  cloudfoundry/cnb:cflinuxfs3
          Description:  A large Cloud Foundry stack based on Ubuntu 18.04
          Name:         org.cloudfoundry.stacks.cflinuxfs3
          Run Image:    cloudfoundry/run:full-cnb
    

Under the `Build Config` section there are three fields to look at:

  * Buildpacks V2 contains a list of V2 compatible buildpacks in the order they'll be run
  * Stacks V2 indicates the stacks that can be chosen to trigger a V2 buildpack build
  * Stacks V3 indicates the stacks that can be chosen to trigger a V3 buildpack build



You can also list the stacks with `kf stacks`:
    
    
    $ kf stacks
    
    Getting stacks in Space: buildpack-docs
    Version  Name                                Build Image                  Run Image                  Description
    V2       cflinuxfs3                          cloudfoundry/cflinuxfs3      cloudfoundry/cflinuxfs3
    V3       org.cloudfoundry.stacks.cflinuxfs3  cloudfoundry/cnb:cflinuxfs3  cloudfoundry/run:full-cnb  A large Cloud Foundry stack based on Ubuntu 18.04
    

Because V3 build images already have their buildpacks built-in, you must use `kf buildpacks` to get the list:
    
    
    $ kf buildpacks
    
    Getting buildpacks in Space: buildpack-docs
    Buildpacks for V2 stacks:
      Name                   Position  URL
      staticfile_buildpack   0         https://github.com/cloudfoundry/staticfile-buildpack
      java_buildpack         1         https://github.com/cloudfoundry/java-buildpack
    V3 Stack: org.cloudfoundry.stacks.cflinuxfs3:
      Name                                        Position  Version     Latest
      org.cloudfoundry.jdbc                       0         v1.0.179    true
      org.cloudfoundry.jmx                        1         v1.0.180    true
      org.cloudfoundry.go                         2         v0.0.2      true
      org.cloudfoundry.tomcat                     3         v1.1.102    true
      org.cloudfoundry.distzip                    4         v1.0.171    true
      org.cloudfoundry.springboot                 5         v1.1.2      true
      ...
    

## Customizing V3 Buildpacks

You can customize the buildpacks that are available to your developers by creating your own builder image with exactly the buildpacks they should have access to. You can also use builder images published by other authors.

### Use a third-party builder image

A list of published CNB stacks is available from the [Buildpack CLI `pack`](https://buildpacks.io/docs/install-pack/). As of this writing, `pack suggest-stacks` outputs:
    
    
    $ pack suggest-stacks
    
    Stacks maintained by the community:
    
        Stack ID: heroku-18
        Description: The official Heroku stack based on Ubuntu 18.04
        Maintainer: Heroku
        Build Image: heroku/pack:18-build
        Run Image: heroku/pack:18
    
        Stack ID: io.buildpacks.stacks.bionic
        Description: A minimal Cloud Foundry stack based on Ubuntu 18.04
        Maintainer: Cloud Foundry
        Build Image: cloudfoundry/build:base-cnb
        Run Image: cloudfoundry/run:base-cnb
    
        Stack ID: org.cloudfoundry.stacks.cflinuxfs3
        Description: A large Cloud Foundry stack based on Ubuntu 18.04
        Maintainer: Cloud Foundry
        Build Image: cloudfoundry/build:full-cnb
        Run Image: cloudfoundry/run:full-cnb
    
        Stack ID: org.cloudfoundry.stacks.tiny
        Description: A tiny Cloud Foundry stack based on Ubuntu 18.04, similar to distroless
        Maintainer: Cloud Foundry
        Build Image: cloudfoundry/build:tiny-cnb
        Run Image: cloudfoundry/run:tiny-cnb
    

To modify Kf to use the stack published by Heroku, edit the `config-defaults` ConfigMap in the `kf` Namespace. Add an entry to the `spaceStacksV3` key like the following:
    
    
    $ kubectl edit configmap config-defaults -n kf
    
    spaceStacksV3: |
      - name: org.cloudfoundry.stacks.cflinuxfs3
        description: A large Cloud Foundry stack based on Ubuntu 18.04
        buildImage: cloudfoundry/cnb:cflinuxfs3
        runImage: cloudfoundry/run:full-cnb
      - name: heroku-18
        description: The official Heroku stack based on Ubuntu 18.04
        buildImage: heroku/pack:18-build
        runImage: heroku/pack:18
    

Then, run `stacks` again:
    
    
    $ kf stacks
    
    Getting stacks in Space: buildpack-docs
    Version  Name                                Build Image                  Run Image                  Description
    V2       cflinuxfs3                          cloudfoundry/cflinuxfs3      cloudfoundry/cflinuxfs3
    V3       org.cloudfoundry.stacks.cflinuxfs3  cloudfoundry/cnb:cflinuxfs3  cloudfoundry/run:full-cnb  A large Cloud Foundry stack based on Ubuntu 18.04
    V3       heroku-18                           heroku/pack:18-build         heroku/pack:18             The official Heroku stack based on Ubuntu 18.04
    

### Create your own builder image

The [Buildpack CLI `pack`](https://buildpacks.io/docs/install-pack/) is used to create your own builder image. You can follow `pack`'s [Working with builders using `create-builder`](https://buildpacks.io/docs/using-pack/working-with-builders/) documentation to create your own builder image. Once created, push it to a container registry and use add it to the `config-defaults` ConfigMap.

## Setting a default stack

Apps will be assigned a default stack if one isn't supplied in their manifest. The default stack is the first in the V2 or V3 stacks list. Unless overridden, a V2 stack is chosen for compatibility with Cloud Foundry.

You can force Kf to use a V3 stack instead of a V2 by setting the `spaceDefaultToV3Stack` field in the `config-defaults` ConfigMap in the `kf` Namespace to be `"true"`:
    
    
    $ kubectl edit configmap config-defaults -n kf
    
    spaceDefaultToV3Stack: "true"
    

This option can also be modified on a per-Space basis by changing setting the `spec.buildConfig.defaultToV3Stack` field to be `true` or `false`. If unset, the value from the `config-defaults` ConfigMap is used.

`config-defaults` value for `spaceDefaultToV3Stack` | Space's `spec.buildConfig.defaultToV3Stack` | Default stack  
---|---|---  
_unset_ | _unset_ | V2  
`"false"` | _unset_ | V2  
`"true"` | _unset_ | V3  
_any_ | `false` | V2  
_any_ | `true` | V3  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
