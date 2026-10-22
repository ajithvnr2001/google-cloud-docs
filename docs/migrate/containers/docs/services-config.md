---
url: https://docs.cloud.google.com/migrate/containers/docs/services-config/
title: Using services-config.yaml \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:25.994620+00:00
---

# Using services-config.yaml  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/services-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using services-config.yaml

When you use the simplified Linux service manager to perform a migration, Migrate to Containers creates a new artifact file, `services-config.yaml`. Use this file to control application initialization on a deployed container. 

**Note:** The `services-config.yaml` is only created when you perform a **new** migration using Migrate to Containers version 1.15.0. It is not created when you convert an existing migration from a previous version to version 1.15.0.

For example, after you migrate the container, edit the `services-config.yaml` file to control application initialization to:

  * Remove applications from the file
  * Add applications to the file
  * Edit the initialization properties of an application



Shown below is an example `services-config.yaml` file:
    
    
    version: v1beta1
    env:
      - name: KEY1
        value: VALUE1
      - name: KEY2
        value: VALUE2
    applications:
        - name: nginx
          type: forking
          envfile: /path/to/file.txt
          env:
            - name: KEY3
              value: VALUE3
          start:
          - cmd: /usr/sbin/nginx -g 'daemon on; master_process on;'
          pidfile: /run/nginx.pid
        - name: ssh@
          type: simple
          start:
          - cmd: /usr/sbin/sshd -i $SSHD_OPTS
            ignore_errors: true
          runtime_directories:
            mode: "0755"
            paths:
              - /run/sshd
            preserve: true
        - name: suitecrm
          type: exec
          start:
          - cmd: /etc/init.d/suitecrm start
          status:
            cmd: /etc/init.d/suitecrm status
        - name: phpsessionclean
          type: oneshot
          start:
            - cmd: /usr/lib/php/sessionclean
          timers:
            - name: phpsessionclean.timer
              on_calendar:
                - cron: 09,39 * * * *
        - name: mariadb
          type: notify
          prestart:
            - cmd: /usr/bin/install -m 755 -o mysql -g root -d /var/run/mysqld
            - cmd: /bin/sh -c "systemctl unset-environment _WSREP_START_POSITION"
            - cmd: /bin/sh -c "[ ! -e /usr/bin/galera_recovery ] && VAR= || VAR=`cd /usr/bin/..; /usr/bin/galera_recovery`; [ $? -eq 0 ] && systemctl set-environment _WSREP_START_POSITION=$VAR || exit 1"
          start:
          - cmd: /usr/sbin/mysqld $MYSQLD_OPTS $_WSREP_NEW_CLUSTER $_WSREP_START_POSITION
          poststart:
            - cmd: /bin/sh -c "systemctl unset-environment _WSREP_START_POSITION"
            - cmd: /etc/mysql/debian-start
          user: mysql
          group: mysql

In this file:

  * `env`: Specifies environment variables at the global level or at the application level. If you specify the same environment variable at both the global and application levels, then the environment variable at the application level takes precedence.

    * For environment variables set at the global level, use `env` to specify a `name`/`value` pair. Names can contain ASCII letters, digits, and the underscore character. Names cannot start with a digit.

    * For environment variables set at the application level, use `env` to specify a `name`/`value` pair. Or, use `envfile` to specify the path to a text file containing lines in the form:
          
          # Comments allowed
          KEY=VALUE

If the text file contains an environment variable definition that duplicates one specified by `env`, then the one specified by `env` takes precedence.

  * `applications`: Specifies the list of applications to be started when you deploy the container and sets the application's initialization properties. 

    * `name`: Specifies the name of the application. 

    * `type` specifies the type of the application, as one of the following: 

      * `forking`: Run the file specified by `start` without forking. The service executable is expected to fork. We recommend that you also set `pidfile`. 

      * `exec`: Fork to run the service. The service is considered started after `exec` has been called on the executable. 

      * `simple` \- Same as `exec`. A `simple` service behaves differently from the `systemd` definition because it waits for both `fork` and `exec` instead of for `fork`.

      * `notify`: Same as `exec` except that for `systemd` the `NOTIFY_SOCKET` environment variable is not set so `sd_notify systemd` calls do not work.

      * `oneshot`: The service is considered started after `exec` is called on the executable. The status is `error` if the service exits with an error code not equal to 0.

    * `prestart`, `start`, `poststart`, and `status` commands for the service.

To start a service, Migrate to Containers executes the `prestart` commands (if any), then the `start` command, and finally the `poststart` commands (if any). If a command fails, and you have not configured the command to use `ignore_errors`, then the service is stopped and you see an error message in the service's status.

The commands used to perform specific operations on the application have the form:
          
          command-type: 
              cmd: command
              shell: /bin/sh
              ignore_errors: false
              ignore_environment_variables: false

Where: 

      * command-type: Specifies the command type as either `prestart`, `start`, `poststart`, or `status`.

For `start`, you can have a single command unless the `type` is `oneshot`.

If `type=forking` or `type=oneshot`, the `poststart` commands are executed after the `start` command forks. Otherwise, they are executed immediately after executing the `start` command.

      * command: Specifies the command to run to perform the operation. 

**Note:** Not everything supported by `/bin/sh` is supported. Only basic environment substitution is supported. 
      * `shell` (Optional): By default, all commands are executed in the `/bin/sh` shell. You can optionally set `shell` to `/bin/bash`. 

      * `ignore_errors` (Optional): If `true`, an exit code from the command normally considered a failure is recorded, but the command is considered to have succeeded. The default value is `false`. 

By default, Migrate to Containers sets `ignore_errors` to `true` for any `systemd` executable that includes the "-" prefix.

      * `ignore_environment_variables` (Optional): If `true`, environment variable substitution is not applied. The default value is `false`.

By default, Migrate to Containers sets `ignore_environment_variables` to `true` for any `systemd` executable that includes the ":" prefix.

    * `pidfile`: Specifies the pid file containing the process ID of the service which is used to check if the process is still running. 

    * `chdir`: Specifies the working directory of the started process. 

    * `user`: Specifies the user name under which the new process is started. 

    * `group`: Specifies the group name under which the new process is started.

    * `timers`: Specifies the list of timers of the application. The application will be activated whenever any of the specified timers elapse.
          
          version: v1beta1
          env: []
          Applications:
          - name: service_name
            type: service_type
            start:
              - cmd: service_exec_command
            timers:
              - name: timer_name
                on_calendar:
                  - cron: realtime_time
                on_startup:
                  - duration: monotonic_time
                on_service_start:
                  - duration: monotonic_time
                on_service_stop:
                  - duration: monotonic_time
          

      * `name`: Specifies the name of the timer.

      * `on_calendar`: Specifies the list of calendar events for the timer.

        * `cron`: A specified time using cron format. For example:
              
              cron: 0 0 * * *
              cron: @daily
              

      * `on_startup`: Specifies a list of durations (relative to when you deploy your container).

        * `duration`: A specified time using duration format. For example:
    
    duration: 30m
    duration: 1sec
    

      * `on_service_start`: Specifies a list of durations, relative to when your application's status changes to active.

        * `duration`: A specified time using duration format.
      * `on_service_stop`: Specifies a list of durations, relative to when your application's status changes to inactive.

        * `duration`: A specified time using duration format.
    * Use the following properties to specify `paths` to directories that are created before starting the service:

      * `runtime_directories`: Specifies the list of `paths` to directories created in `/run/`.

      * `state_directories`: Specifies the list of `paths` to directories created in `/var/lib/`.

      * `cache_directories`: Specifies the list of `paths` to directories created in `/var/cache/`.

      * `logs_directories`: Specifies the list of `paths` to directories created in `/var/log/`.

      * `configuration_directories`: Specifies the list of `paths` to directories created in `/etc/`.

Each of these properties takes the following options:

      * `mode`: Specifies the file mode. The default is 0755, corresponding to read and execute access for everyone, and write access for the owner.
      * `preserve`: If `false` the directory is cleaned up when the service is stopped. The default is `true`.



## Add or remove a service to your services.yaml file

You can add or remove a service from your `services.yaml` file by manually editing it. Whenever you add a new service, you must populate the following fields:

  * `name`
  * `type`
  * `start`



For more information about the mandatory and optional fields for a service, see the `services.yaml` definition above.

**Note:** When working with `.yaml` documents, you should be mindful about your indentation and spacing as they can cause warnings and errors.

### Add a service

To add a service to your `services.yaml` file, follow these steps:

  1. Open your `services.yaml` file in a text editor for modification.

  2. In `services.yaml`, navigate to the **`applications`** attribute:
         
         version: v1beta1
         env:
          - name: KEY1
          ...
         **applications :**
         

  3. Add your desired service on the line below the `applications` attribute starting with the `name` field, followed by the other mandatory and optional fields appropriate to your application:
         
         version: v1beta1
         env:
          - name: KEY1
          ...
         applications:
         **- name:**
           **type :**
           **start :**
             **- cmd:**
           ...
         

If your `services.yaml` file already has service definitions under the `applications` attribute, you can add a new service starting with the `name` field on the line below the last entry of the previous service:
         
         version: v1beta1
         env:
          - name: KEY1
          ...
         applications:
         - name:
           type:
           start:
         **- name:**
           **type :**
           **start :**
             ...
         

  4. Save your `services.yaml` file.




### Remove a service

To remove a service from your `services.yaml` file, follow these steps:

  1. Open your `services.yaml` file in a text editor for modification.

  2. In `services.yaml`, navigate to the **`applications`** attribute:
         
         version: v1beta1
         env:
          - name: KEY1
          ...
         **applications :**
         ...
         

  3. Remove your desired service starting with the `name` field, followed by the other mandatory and optional fields appropriate to your application. For example:

Before the service has been removed:
         
         version: v1beta1
         env:
         - name: KEY1
           ...
         applications:
         **- name:**
           **type :**
           **start :**
             **- cmd:**
         - name:
           ...
         
         

After the service has been removed:
         
         version: v1beta1
         env:
         - name: KEY1
           ...
         applications:
         **- name:**
           ...
         

  4. Save your `services.yaml` file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
