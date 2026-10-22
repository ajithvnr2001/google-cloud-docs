---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/restore-pgbackrest/
title: Restore an AlloyDB Omni cluster using pgBackRest \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:59.880310+00:00
---

# Restore an AlloyDB Omni cluster using pgBackRest  |  AlloyDB Omni for Kubernetes: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/restore-pgbackrest/

This page documents AlloyDB Omni version **15.7.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)



Send feedback 

#  Restore an AlloyDB Omni cluster using pgBackRest Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/restore-pgbackrest)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/restore-pgbackrest)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/restore-pgbackrest)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/restore-pgbackrest)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/restore-pgbackrest)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/restore-pgbackrest)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [pgBackRest](https://pgbackrest.org/), the open-source backup solution included with the AlloyDB Omni container. 

Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the pgBackRest manual](https://pgbackrest.org/user-guide-index.html) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.

For more information about configuring pgBackRest to work with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/set-up-pgbackrest).

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

For Kubernetes-based information, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/backup-kubernetes).

## Before you begin

Before restoring an AlloyDB Omni cluster, ensure that you have the following:

  * [Set up and configured pgBackRest](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/set-up-pgbackrest) for your AlloyDB Omni instance.

  * Sufficient disk space on destination file system to store the restored AlloyDB Omni database cluster.

  * Same major version of AlloyDB Omni used for the restoration container as the original source container.

To check your version of PostgreSQL, run the following command:

### Docker
        
        docker exec -u postgres CONTAINER_NAME psql -c "SELECT version();"
        

### Docker
        
        docker exec -u postgres CONTAINER_NAME psql -c "SELECT version();"
        

### Podman
        
        podman exec -u postgres CONTAINER_NAME psql -c "SELECT version();"
        

### Podman
        
        podman exec -u postgres CONTAINER_NAME psql -c "SELECT version();"
        

Replace the following variable:

    * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.

To check your version of pgBackRest, run the following command:

### Docker
    
    docker exec -u postgres CONTAINER_NAME pgbackrest version
    

### Docker
    
    docker exec -u postgres CONTAINER_NAME pgbackrest version
    

### Podman
    
    podman exec -u postgres CONTAINER_NAME pgbackrest version
    

### Podman
    
    podman exec -u postgres CONTAINER_NAME pgbackrest version
    

Replace the following variable:

    * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.

If your target container has a different version of PostgreSQL, pgBackRest, or both, then you need to create a new target container with a matching version. If this is not possible, then you need to use an alternative method, such as the PostgreSQL included `pg_dump` or `pg_dumpall` utilities to copy your databases across versions.




## Stop your AlloyDB Omni container

To simulate your AlloyDB Omni database cluster not being available, stop the container.

### Docker
    
    
    docker stop CONTAINER_NAME
    docker rm CONTAINER_NAME

### Docker
    
    
    docker stop CONTAINER_NAME
    docker rm CONTAINER_NAME

### Podman
    
    
    podman stop CONTAINER_NAME
    podman rm CONTAINER_NAME

### Podman
    
    
    podman stop CONTAINER_NAME
    podman rm CONTAINER_NAME

Replace the following variable:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.



## Create idle AlloyDB Omni container

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest sleep infinity
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest sleep infinity
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest sleep infinity
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest sleep infinity
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `BACKUP_DIR`: External directory path that your backups are stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.



## Remove your data directory

To clear your AlloyDB Omni database cluster, remove the data directory.

### Docker
    
    
    docker exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"
    

### Docker
    
    
    docker exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"
    

### Podman
    
    
    podman exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"
    

### Podman
    
    
    podman exec CONTAINER_NAME sh -c "rm -rf /var/lib/postgresql/data/*"
    

Replace the following variable:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.



## Validate that your backups are visible

### Docker
    
    
    docker exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    info
    

### Docker
    
    
    docker exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    info
    

### Podman
    
    
    podman exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    info
    

### Podman
    
    
    podman exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    info
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`.



## Restore your backup

### Docker
    
    
    docker exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    restore
    

### Docker
    
    
    docker exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    restore
    

### Podman
    
    
    podman exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    restore
    

### Podman
    
    
    podman exec -u postgres CONTAINER_NAME pgbackrest \
    --config-path=/var/lib/postgresql/backups \
    --stanza=STANZA_NAME \
    restore
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`.



## Remove idle AlloyDB Omni container

### Docker
    
    
    docker kill CONTAINER_NAME
    docker rm CONTAINER_NAME

### Docker
    
    
    docker kill CONTAINER_NAME
    docker rm CONTAINER_NAME

### Podman
    
    
    podman kill CONTAINER_NAME
    podman rm CONTAINER_NAME

### Podman
    
    
    podman kill CONTAINER_NAME
    podman rm CONTAINER_NAME

Replace the following variable:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.



## Create AlloyDB Omni container

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest
    

### Docker
    
    
    docker run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    google/alloydbomni:latest
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest
    

### Podman
    
    
    podman run -d --name CONTAINER_NAME \
    -v DATA_DIR:/var/lib/postgresql/data \
    -v BACKUP_DIR:/var/lib/postgresql/backups \
    -p HOST_PORT:5432 \
    --restart=always \
    docker.io/google/alloydbomni:latest
    

Replace the following variables:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.
  * `DATA_DIR`: Host directory path that your data is stored in.
  * `BACKUP_DIR`: External directory path that your backups are stored in.
  * `HOST_PORT`: TCP port on the host machine that the container should publish its own port `5432` to. To use the PostgreSQL default port on the host machine as well, specify `5432`.



## Validate that AlloyDB Omni started

### Docker
    
    
    docker logs -f CONTAINER_NAME
    

### Docker
    
    
    docker logs -f CONTAINER_NAME
    

### Podman
    
    
    podman logs -f CONTAINER_NAME
    

### Podman
    
    
    podman logs -f CONTAINER_NAME
    

Replace the following variable:

  * `CONTAINER_NAME`: Name you used for your container. For example, `my-omni-1`.



## Other options

The pgBackRest `restore` command is very flexible, with an array of options and features that you can control through passing in different command-line options. For a complete guide to performing restores, see [Restore](https://pgbackrest.org/user-guide.html#restore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
