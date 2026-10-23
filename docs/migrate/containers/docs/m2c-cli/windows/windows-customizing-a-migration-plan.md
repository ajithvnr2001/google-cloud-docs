---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/windows/windows-customizing-a-migration-plan/
title: Customize migration plan for Windows IIS services \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:07.815263+00:00
---

# Customize migration plan for Windows IIS services  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/windows/windows-customizing-a-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize migration plan for Windows IIS services

Review the migration plan file that was populated during the creation of the migration. You can customize it before proceeding to execute the migration. The details of your migration plan are used to extract the workload container artifacts from the source VM.

This section describes the contents of the migration plan and the kinds of customizations that you might consider before you execute the migration, and generate deployment artifacts.

## Before you begin

This document assumes that you've already [created a migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the resulting migration plan file.

## Migration plan structure

Following is the full migration plan structure. The next sections discuss this structure, explain what each part is, and how to modify it.
    
    
    globalSettings:
        globalIis:
            enablegmsa: string
            apppools:
                - enable32bitapponwin64: bool
                  identitytype: string
                  managedruntimeversion: string
                  name: string
            connectionStrings:
                add:
                    - connectionstring: string
                      name: string
                      providername: string
            security:
                authentication:
                    windowsAuthentication:
                        enabled: bool
                        providers:
                            - value: string
                authorization:
                    add:
                        - access_type: string
                          roles: string
                          users: string
                          verbs: string
                    remove:
                        - roles: string
                          users: string
                          verbs: string
        image:
            extraFeatures:
                - string
        target:
            baseVersion: string
            requirements:
                - string
            warnings:
                - string
        msvcRuntimes:
                - string
        pathEnvVarAdditionalEntries:
                - string
    images:
        - name: string
          probes:
            enabled: bool
            livenessProbe:
                probehandler:
                    exec:
                        command:
                            - string
                            - string
                initialdelayseconds: int
                timeoutseconds: int
                periodseconds: int
                successthreshold: int
                failurethreshold: int
                terminationgraceperiodseconds: optional[int]
            readinessProbe:
                probehandler:
                    exec:
                        command:
                            - string
                            - string
                initialdelayseconds: int
                timeoutseconds: int
                periodseconds: int
                successthreshold: int
                failurethreshold: int
                terminationgraceperiodseconds: optional[int]
          useractions:
            files:
                - source: string
                  target: string
            registry:
                currentcontrolset:
                    - path: string
                software:
                    - path: string
          workloads:
            sites:
                site:
                    - applications:
                        - applicationpool: string
                          path: string
                          virtualdirectories:
                            - path: string
                              physicalpath: string
                      bindings:
                        - port: int
                          protocol: string
                          sslflags: int
                      connectionstrings:
                        - connectionstring: string
                          name: string
                          providername: string
                      name: string
                      security:
                        authentication:
                            windowsAuthentication:
                                enabled: bool
                                providers:
                                    - value: string
                        authorization:
                            add:
                                - access_type: string
                                  roles: string
                                  users: string
                                  verbs: string
                            remove:
                                - roles: string
                                  users: string
                                  verbs: string
                      serverautostart: bool
    version: string
    

## The `globalSettings` section

The `globalSettings` section describes basic requirements for pods running IIS sites from this VM. The discovery process searches for general configurations in the source VM, and uses them to populate this section. These configurations contain fields present in the specific image configurations as described in the following section, and affects all images at the same time.

### The `image` section

The `image` section following `globalSettings` describes the list of [Windows features](https://docs.microsoft.com/en-us/powershell/module/servermanager/?view=windowsserver2022-ps) to install on the pods. The discovery process populates this section with all Windows features which exist on the original VM, and can be installed on a Windows container.

**Note:**

Not all Windows features can be installed on Windows containers. Therefore, manually editing this section might cause build errors. 

### The `msvcRuntimes` section

When migrating an application, it might have a dependency on a specific version or versions of the Microsoft Visual C++ Runtime (MSVCRT). Migrate to Containers automatically detects the runtimes installed on the source VM and included them in the migration plan.

You can modify the list of runtimes in the migration plan by adding or removing members of `msvcRuntimes`:

The complete list of possible values are: (The 2015 runtime also includes support for 2017, 2019, and 2022)
    
    
        msvcRuntimes:
            - MSVC2012_x64
            - MSVC2013_x64
            - MSVC2015_x64
            - MSVC2012_x86
            - MSVC2013_x86
            - MSVC2015_x86
    

### The `pathEnvVarAdditionalEntries` section

Windows IIS applications might have non-default `PATH` environment variable entries, which are automatically detected on the source VM and included in the migration plan. You can modify the `PATH` environment variables by editing the members of `pathEnvVarAdditionalEntries`:
    
    
        pathEnvVarAdditionalEntries:
          - "C:\\myDllsFolder"
          - "C:\\ProgramData\\SomeSoftware"
    

#### Edit the image section

You might want to edit the `image` section in the following cases:

  1. Some suggested features are not be required by the migrated sites. This happens if the source VM has usages other than hosting IIS sites.

  2. You modified the IIS sections in the migration plan, and added configurations that depend on additional Windows features. (For example, Windows authentication depends on the Window authentication feature).




### The `target` section

The `target` section specifies which base Windows image you're using (for example 1909). You should rarely need to edit this field.

## The `images` section

Each subitem of the `images` section specifies a single output image.  
In the artifacts zip, each such image has a separate subdirectory, with its own `Dockerfile` and `deployment_spec.yaml` (see [Deploying the container image](https://docs.cloud.google.com/migrate/containers/docs/windows/deploying-to-target-cluster#deploy-pod)).

### The `name` field

The `name` field describes the image name. It affects the name of the image subdirectory and the `deployment_spec.yaml` file in the artifacts.

### The `probes` field

The `probes` field describes the health probe configuration of the image. To learn more about kubelet probes, see [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

#### Edit IIS health probes

Health probes can monitor the downtime and ready status of your managed containers. Health probe monitoring can help reduce the downtime of migrated containers and provide better monitoring.

Unknown health states can create availability degradation, false-positive availability monitoring, and potential data loss. Without a health probe, kubelet can only assume the health of a container and might send traffic to a container instance that is not ready. If the instance is not ready, it can cause traffic loss. Kubelet might also not detect containers that are in a frozen state and doesn't restart them.

A health probe functions by running a small scripted statement when the container starts. The script checks for successful conditions, which are defined by the type of probe used, every period. The period is defined in the migration plan by a `periodSeconds` field. You can define these probes manually when you customize the migration plan.

There are three types of probes available to configure. All probes are probe v1 core defined in [probe v1 core reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#probe-v1-core) and share the same function as the corresponding fields of [container v1 core](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#container-v1-core).

  * * **Liveness probe:** Liveness probes are used to know when to restart a container.

**Note:** If a process in your container is able to crash on its own when it encounters an issue, or is unhealthy, you don't necessarily need a liveness probe. The kubelet automatically performs the correct action in accordance with the `restartPolicy` of the Pod.
  * **Readiness probe:** Readiness probes are used to know when a container is ready to start accepting traffic. To start sending traffic to a pod only when a probe succeeds, specify a readiness probe. A readiness probe might act similarly to a liveness probe. However, a readiness probe indicates that a pod starts without receiving any traffic and only start receiving traffic after the probe succeeds.

  * **Startup probe:** The kubelet uses startup probes to know when a container application has started. If such a probe is configured, it disables liveness and readiness checks until it succeeds, making sure that those probes don't interfere with the application startup.




After discovery, the probe configuration is added to the migration plan. The probes can be used in their default configuration as shown in the following example. The default configuration uses `exec` command for the liveness and readiness probes. Both are using a PowerShell script called `probe.ps1` that calls IIS command-line tool [appcmd](https://docs.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe) to check the status of the IIS sites.

The probes are disabled by default, to enable the probes, set the `enabled` flag to `true`.
    
    
    images:
    name: IMAGE_NAME
          probes:
            enabled: false
            livenessProbe:
                probehandler:
                    exec:
                        command:
                            - powershell.exe
                            - C:\m4a\probe.ps1
                initialdelayseconds: 0
                timeoutseconds: 1
                periodseconds: 10
                successthreshold: 1
                failurethreshold: 3
                terminationgraceperiodseconds: null
            readinessProbe:
                probehandler:
                    exec:
                        command:
                            - powershell.exe
                            - C:\m4a\probe.ps1
                initialdelayseconds: 0
                timeoutseconds: 1
                periodseconds: 10
                successthreshold: 1
                failurethreshold: 3
                terminationgraceperiodseconds: null

### The `windowsServices` section

Windows containers created during a migration run and monitor a single Windows IIS service. However, some workloads might require running additional services (including a database, logging mechanism, proxy, and more) in order to function correctly.

To run additional services in the migrated container, add entries to the `windowsServices` section, and copy the necessary binaries in the `useractions` section.
    
    
    version: v1
    globalSettings:
        target:
           …
        globalIIS:
        …
    images:
      - name: migrated-image-zgwb2
        workloads:
        sites:
          site:
            - applications:
              ...
              bindings:
              - port: 80
                protocol: http
              name: Default Web Site
              …
        windowsServices:
        - MyService
        useractions:
          files:
            - source: C:\Program Files\MyService
              target: C:\Program Files\MyService
          registry:
            currentcontrolset:
              - key: services\MyService
    

### The `useractions` section

The `useractions` section specifies additional files and registry keys that you might want to migrate.

For example:
    
    
          useractions:
            files:
            - source: DRIVE:\FOLDER-OR-FILE-PATH
              target: DRIVE:\FOLDER-OR-FILE-PATH
            - source: C:\myfolder
              target: C:\myfolder
            - source: D:\myfile
              target: D:\myfile
            - source: D:\myfile
              target: C:\myfile
            ...
            registry:
              currentcontrolset:
              - path: KEY
              ...
              software:
              - path: KEY
              ...

The paths specified for `currentcontrolset` and `software` are to keys in the `HKEY_LOCAL_MACHINE\System\CurrentControlSet` [registry hive](https://docs.microsoft.com/en-us/windows/win32/sysinfo/registry-hives) or in the `HKEY_LOCAL_MACHINE\Software` registry hive.

#### Edit the `useractions` section

By default the only files copied to the image are the virtual directories of sites in the specified image.  
If your code or configurations import files from outside this directory, you should add them to the `useractions` section.  
Also, any registry values that your code depends on should be added by editing the `useractions` `registry` section.

## Settings related specifically to IIS

The IIS related settings are divided into settings related to specific sites, which are part of the image specification, and settings related to all sites, which are following the `gloabalIis` section.

**Note:**

The IIS sections in the migration plan are purposefully structured similarly to the IIS configuration files. They must be readable to people with IIS background.

### The `sites` section

The [sites](https://docs.microsoft.com/en-us/iis/get-started/planning-your-iis-architecture/understanding-sites-applications-and-virtual-directories-on-iis) section describes the sites that are migrated to a specific image. It's possible for several images to contain the same site.

If you want to use [Cloud Load Balancing, Ingress, or Cloud Service Mesh to handle the SSL configuration](https://docs.cloud.google.com/migrate/containers/docs/windows/prepare-windows-cluster#secure-access), then you need to set `protocol` to `http`:
    
    
    sites:
      site:
      - applications:
        - path: /
          virtualdirectories:
            - path: /
              physicalpath: '%SystemDrive%\inetpub\wwwroot'
              bindings:
              - port: 8080
                **protocol : http**
              name: Default Web Site

**Note:** Only HTTP and HTTPS protocols are allowed in the `protocol` setting. All protocols other than HTTP/HTTPS are skipped and not processed.

### The `apppools` section

The `apppools` section describes the [Application Pools](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/) created on the migrated pods.

The `identitytype` field specifies the IIS identity of an application pool as either `ApplicationPoolIdentity` (default), `NetworkService`, `LocalSystem`, or `LocalService`.

For more information, see [Understanding identities in IIS](https://support.microsoft.com/en-us/help/4466942/understanding-identities-in-iis) and [Application Pool Identities](https://docs.microsoft.com/en-us/iis/manage/configuring-security/application-pool-identities).

The following is an example migration plan containing `identitytype`:
    
    
    migrationPlan:
        applications:
          iis:
            applicationhost:
              apppools:
              - name: DefaultAppPool
                # Allowed values include: ApplicationPoolIdentity (default), NetworkService, LocalSystem, LocalService
                **identitytype="NetworkService"**
              - managedruntimeversion: v4.0
                name: .NET v4.5 Classic
              - managedruntimeversion: v4.0
                name: .NET v4.5

When you execute the migration plan to generate the container artifacts, Migrate to Containers automatically adds the necessary Dockerfile directives according to the `identitytype` field setting.

For example, if you set `identitytype` to `NetworkService` the directive is in the form:
    
    
    RUN c:\windows\system32\inetsrv\appcmd.exe set apppool \"DefaultAppPool\" \"/-processModel.identityType:NetworkService\";

Migrate to Containers automatically adds read ACL directives to the site's folders according to the target `identitytype`, and for the IUSR built-in user. This is automatically done for application file system items where the original application account was specified either by inheritance or explicitly.

For more information, see [Set ACLs](https://docs.cloud.google.com/migrate/containers/docs/windows/prepare-windows-cluster#set_acls).

### The `enablegmsa` field

The `enablegmsa` field is syntactic sugar in the migration plan. It's a shortcut for overwriting the [identity](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/add/processmodel) field of the application pool.

The supported values for `enablegmsa` field are:

  * `auto` (default): Convert the migrated container to use gMSA if Migrate to Containers determines that its current configuration is not allowed.
  * `all`: Always convert the migrated container to use gMSA and ignore the setting of `identitytype`. In this case, `identitytype` is always interpreted as being set to `NetworkService`.



The following is an example migration plan containing `enablegmsa`:
    
    
    migrationPlan:
        applications:
          iis:
            # Allowed values include: auto (default), all
            **enablegmsa : auto|all**

To learn more, see [Configure your app to use a gMSA](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/gmsa-configure-app).

### Connection strings

[Connection strings](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings) define a connection from the migrated container workload to a .NET Framework data provider.

Migrate to Containers supports connection strings at the site and global scope.

To add a connection string to a site, edit the `site` definition in the migration plan to set the `connectionstrings` property:
    
    
    sites:
      site:
        **# Add the site connection strings here.
        connectionstrings:
        - name: connectionname1
          providername: System.Data.SqlClient
          connectionstring: Database=connectedDB1;Password=Welcome1;User=admin;
        - name: connectionname2
          providername: System.Data.OleDb
          connectionstring: Database=connectedDB2;Password=Welcome2;User=admin;**
      - applications:
        - path: /
          virtualdirectories:
          ...

To add a connection string to the global scope (making it accessible to all sites), edit the connection strings directly following `globalIis`:
    
    
    globalIis:
      enablegmsa: auto
      connectionStrings:
      connectionstring:
        - name: connectionname3
          providername: System.Data.SqlClient
          connectionstring: Database=connectedDB3;Password=Welcome3;User=admin;
      applicationhost:
          ...

Where:

  * `name` specifies the connection name.
  * `providername` optionally specifies the data provider type. Migrate to Containers only supports a value of `System.Data.SqlClient`. supports the .NET Framework data provider: 
    * `System.Data.SqlClient`
    * `System.Data.OleDb`
    * `System.Data.Odbc`
    * `System.Data.OracleClient`
  * `connectionstring` specifies the [Connection Strings](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/connection-string-syntax#connection-string-builders) used to connect to the data provider.



#### Edit the connection strings sections

Migrate to Containers automatically copies connection strings detected in the migrated VM to the migration plan.

Some connection strings might not be detected and should be added by editing the migration plan as shown preceding. (For example, if the connection strings are in an encrypted section of the `applicationhost.config` file).

For guidance on determining which connection strings to add to your migration plan, see [Retrieving Connection Strings at Run Time](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings-and-configuration-files#retrieving-connection-strings-at-run-time) in the Microsoft documentation.

#### Connection string external dependencies

  * Connection strings can contain dependencies, such as a reference to a file at or to a Windows user associated with the site. You can add custom user actions to the migration plan to copy an extra file in the file system. Manually edit the Dockerfile to add a Windows user.
  * Connection strings can contain dependencies, such as a reference to an external data source. These dependencies must be migrated manually to ensure that the migrated container workload has access to the data source.



### The `security` section

The security sections contain the authentication and authorization subsections.

  * [Windows authentication](https://docs.microsoft.com/en-us/windows-server/security/windows-authentication/windows-authentication-overview) verifies Active Directory users.
  * [Windows authorization](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups) is the mechanism for specifying which users are allowed which types of access to an IIS website. The access types are the HTTP verbs (POST, GET, PUT, PATCH, DELETE).



Similar to connection strings, to set authorization or authentication for all sites, edit `globalIis` as in the following example. To set authorization or authentication for a specific site, edit the site element.
    
    
    globalIis:
        security:
          authentication:
            **windowsAuthentication :
              providers:
              - NTLM
          authorization:
            - add:
              user:John
              access:
              role:
             - remove:
                  user:Jane
                  access: GET
                  role: **
                ...

Where:

  * `providers` specifies the provider of your security protocols.
  * `user` species the username.
  * `access` species the permissions of the user. The access types are the HTTP verbs (POST, GET, PUT, PATCH, DELETE).
  * `role` species a specific permission role.



## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
