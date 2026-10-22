---
url: https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database/
title: Clean up the Airflow database \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:47.986164+00:00
---

# Clean up the Airflow database  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Clean up the Airflow database Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/cleanup-airflow-database "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to maintain the Airflow database in your environment.

## Limits for database size

As the time goes, the Airflow database of your environment stores more and more data. This data includes information and logs related to past DAG runs, tasks, and other Airflow operations.

  * If the Airflow database size is more than 16 GB, then you can't upgrade your environment to a later version.

  * If the Airflow database size is more than 20 GB, it is not possible to create snapshots.




## Run the DB maintenance DAG on a schedule

You can use the maintenance DAG to prune the content of your environment's Airflow database:

  * Run the maintenance DAG periodically to keep the database size within limits. We recommend to run this DAG daily for most environments.

  * Choose a retention period (`DEFAULT_MAX_DB_ENTRY_AGE_IN_DAYS`) that allows keeping the database size within limits. We recommend a period of 30 days as a starting point for most environments.

**Note:** The maintenance DAG prunes the content using an [`execution_date` identifier in Airflow](https://airflow.apache.org/docs/apache-airflow/stable/faq.html#what-does-execution-date-mean). Depending on your scheduling settings, there might be a significant difference between an `execution_date` and the actual time of execution. If you have DAGs with monthly schedule, we recommend to increase the retention period beyond 30 days.
  * If you observe that the [Airflow metadata database size metric](https://docs.cloud.google.com/composer/docs/composer-2/use-monitoring-dashboard#db-statistics) increases significantly between runs of the maintenance DAG, consider running this DAG more often.




By default, this DAG removes old entries from `job`, `dag_run`, `task_instance`, `log`, `xcom`, `sla_miss`, `dags`, `task_reschedule`, `task_fail` and `import_error` tables. In the DAG, review the list of tables and decide whether old entries must be removed from them. In general, most space savings are provided by cleaning `log`, `task_instance`, `dag_run` and `xcom` tables. To exclude a table from cleanup, modify the DAG and comment corresponding items in the `DATABASE_OBJECTS` list.
    
    
    """A maintenance workflow that you can deploy into Airflow to periodically clean
    out the DagRun, TaskInstance, Log, XCom, Job DB and SlaMiss entries to avoid
    having too much data in your Airflow MetaStore.
    
    ## Authors
    
    The DAG is a fork of [teamclairvoyant repository.](
    https://github.com/teamclairvoyant/airflow-maintenance-dags/tree/master/db-cleanup
    )
    
    ## Usage
    
    1. Update the global variables (SCHEDULE_INTERVAL, DAG_OWNER_NAME,
      ALERT_EMAIL_ADDRESSES and ENABLE_DELETE) in the DAG with the desired values
    
    2. Modify the DATABASE_OBJECTS list to add/remove objects as needed. Each
       dictionary in the list features the following parameters:
        - airflow_db_model: Model imported from airflow.models corresponding to
          a table in the airflow metadata database
        - age_check_column: Column in the model/table to use for calculating max
          date of data deletion
    
    3. Create and Set the following Variables in the Airflow Web Server
      (Admin -> Variables)
        - airflow_db_cleanup__max_db_entry_age_in_days - integer - Length to
          retain the log files if not already provided in the conf. If this is set
          to 30, the job will remove those files that are 30 days old or older.
    
    4. Put the DAG in your gcs bucket.
    """
    from datetime import timedelta
    import logging
    import os
    
    import airflow
    from airflow import settings
    from airflow.models import (
        DAG,
        DagModel,
        DagRun,
        Log,
        SlaMiss,
        TaskInstance,
        Variable,
        XCom,
    )
    from airflow.operators.python import PythonOperator
    from airflow.utils import timezone
    from airflow.version import version as airflow_version
    
    import dateutil.parser
    from sqlalchemy import desc, text
    from sqlalchemy.exc import ProgrammingError
    
    
    def parse_airflow_version(version: str) -> tuple[int]:
        # TODO(developer): Update this function if you are using a version
        # with non-numerical characters such as "2.9.3rc1".
        COMPOSER_SUFFIX = "+composer"
        if version.endswith(COMPOSER_SUFFIX):
            airflow_version_without_suffix = version[:-len(COMPOSER_SUFFIX)]
        else:
            airflow_version_without_suffix = version
        airflow_version_str = airflow_version_without_suffix.split(".")
    
        return tuple([int(s) for s in airflow_version_str])
    
    
    now = timezone.utcnow
    
    # airflow-db-cleanup
    DAG_ID = os.path.basename(__file__).replace(".pyc", "").replace(".py", "")
    
    START_DATE = airflow.utils.dates.days_ago(1)
    
    # How often to Run. @daily - Once a day at Midnight (UTC).
    SCHEDULE_INTERVAL = "@daily"
    
    # Who is listed as the owner of this DAG in the Airflow Web Server.
    DAG_OWNER_NAME = "operations"
    
    # List of email address to send email alerts to if this job fails.
    ALERT_EMAIL_ADDRESSES = []
    
    # Airflow version used by the environment as a tuple of integers.
    # For example: (2, 9, 2)
    #
    # Value in `airflow_version` is in format e.g. "2.9.2+composer"
    # It's converted to facilitate version comparison.
    AIRFLOW_VERSION = parse_airflow_version(airflow_version)
    
    # Length to retain the log files if not already provided in the configuration.
    # If this is set to 30, the job will remove those files
    # that are 30 days old or older.
    DEFAULT_MAX_DB_ENTRY_AGE_IN_DAYS = int(
        Variable.get("airflow_db_cleanup__max_db_entry_age_in_days", 30)
    )
    
    # Prints the database entries which will be getting deleted;
    # set to False to avoid printing large lists and slowdown the process.
    PRINT_DELETES = False
    
    # Whether the job should delete the DB entries or not.
    # Included if you want to temporarily avoid deleting the DB entries.
    ENABLE_DELETE = True
    
    # List of all the objects that will be deleted.
    # Comment out the DB objects you want to skip.
    DATABASE_OBJECTS = [
        {
            "airflow_db_model": DagRun,
            "age_check_column": DagRun.execution_date,
            "keep_last": True,
            "keep_last_filters": [DagRun.external_trigger.is_(False)],
            "keep_last_group_by": DagRun.dag_id,
        },
        {
            "airflow_db_model": TaskInstance,
            "age_check_column": TaskInstance.start_date,
            "keep_last": False,
            "keep_last_filters": None,
            "keep_last_group_by": None,
        },
        {
            "airflow_db_model": Log,
            "age_check_column": Log.dttm,
            "keep_last": False,
            "keep_last_filters": None,
            "keep_last_group_by": None,
        },
        {
            "airflow_db_model": XCom,
            "age_check_column": XCom.execution_date
            if AIRFLOW_VERSION < (2, 2, 5)
            else XCom.timestamp,
            "keep_last": False,
            "keep_last_filters": None,
            "keep_last_group_by": None,
        },
        {
            "airflow_db_model": SlaMiss,
            "age_check_column": SlaMiss.execution_date,
            "keep_last": False,
            "keep_last_filters": None,
            "keep_last_group_by": None,
        },
        {
            "airflow_db_model": DagModel,
            "age_check_column": DagModel.last_parsed_time,
            "keep_last": False,
            "keep_last_filters": None,
            "keep_last_group_by": None,
        },
    ]
    
    # Check for TaskReschedule model.
    try:
        from airflow.models import TaskReschedule
    
        DATABASE_OBJECTS.append(
            {
                "airflow_db_model": TaskReschedule,
                "age_check_column": TaskReschedule.execution_date
                if AIRFLOW_VERSION < (2, 2, 0)
                else TaskReschedule.start_date,
                "keep_last": False,
                "keep_last_filters": None,
                "keep_last_group_by": None,
            }
        )
    
    except Exception as e:
        logging.error(e)
    
    # Check for TaskFail model.
    try:
        from airflow.models import TaskFail
    
        DATABASE_OBJECTS.append(
            {
                "airflow_db_model": TaskFail,
                "age_check_column": TaskFail.start_date,
                "keep_last": False,
                "keep_last_filters": None,
                "keep_last_group_by": None,
            }
        )
    
    except Exception as e:
        logging.error(e)
    
    # Check for RenderedTaskInstanceFields model.
    if AIRFLOW_VERSION < (2, 4, 0):
        try:
            from airflow.models import RenderedTaskInstanceFields
    
            DATABASE_OBJECTS.append(
                {
                    "airflow_db_model": RenderedTaskInstanceFields,
                    "age_check_column": RenderedTaskInstanceFields.execution_date,
                    "keep_last": False,
                    "keep_last_filters": None,
                    "keep_last_group_by": None,
                }
            )
    
        except Exception as e:
            logging.error(e)
    
    # Check for ImportError model.
    try:
        from airflow.models import ImportError
    
        DATABASE_OBJECTS.append(
            {
                "airflow_db_model": ImportError,
                "age_check_column": ImportError.timestamp,
                "keep_last": False,
                "keep_last_filters": None,
                "keep_last_group_by": None,
                "do_not_delete_by_dag_id": True,
            }
        )
    
    except Exception as e:
        logging.error(e)
    
    if AIRFLOW_VERSION < (2, 6, 0):
        try:
            from airflow.jobs.base_job import BaseJob
    
            DATABASE_OBJECTS.append(
                {
                    "airflow_db_model": BaseJob,
                    "age_check_column": BaseJob.latest_heartbeat,
                    "keep_last": False,
                    "keep_last_filters": None,
                    "keep_last_group_by": None,
                }
            )
        except Exception as e:
            logging.error(e)
    else:
        try:
            from airflow.jobs.job import Job
    
            DATABASE_OBJECTS.append(
                {
                    "airflow_db_model": Job,
                    "age_check_column": Job.latest_heartbeat,
                    "keep_last": False,
                    "keep_last_filters": None,
                    "keep_last_group_by": None,
                }
            )
        except Exception as e:
            logging.error(e)
    
    default_args = {
        "owner": DAG_OWNER_NAME,
        "depends_on_past": False,
        "email": ALERT_EMAIL_ADDRESSES,
        "email_on_failure": True,
        "email_on_retry": False,
        "start_date": START_DATE,
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
    }
    
    dag = DAG(
        DAG_ID,
        default_args=default_args,
        schedule_interval=SCHEDULE_INTERVAL,
        start_date=START_DATE,
    )
    if hasattr(dag, "doc_md"):
        dag.doc_md = __doc__
    if hasattr(dag, "catchup"):
        dag.catchup = False
    
    
    def print_configuration_function(**context):
        logging.info("Loading Configurations...")
        dag_run_conf = context.get("dag_run").conf
        logging.info("dag_run.conf: " + str(dag_run_conf))
        max_db_entry_age_in_days = None
        if dag_run_conf:
            max_db_entry_age_in_days = dag_run_conf.get(
                "maxDBEntryAgeInDays", None
            )
        logging.info("maxDBEntryAgeInDays from dag_run.conf: " + str(dag_run_conf))
        if max_db_entry_age_in_days is None or max_db_entry_age_in_days < 1:
            logging.info(
                "maxDBEntryAgeInDays conf variable isn't included or Variable "
                + "value is less than 1. Using Default '"
                + str(DEFAULT_MAX_DB_ENTRY_AGE_IN_DAYS)
                + "'"
            )
            max_db_entry_age_in_days = DEFAULT_MAX_DB_ENTRY_AGE_IN_DAYS
        max_date = now() + timedelta(-max_db_entry_age_in_days)
        logging.info("Finished Loading Configurations")
        logging.info("")
    
        logging.info("Configurations:")
        logging.info("max_db_entry_age_in_days: " + str(max_db_entry_age_in_days))
        logging.info("max_date:                 " + str(max_date))
        logging.info("enable_delete:            " + str(ENABLE_DELETE))
        logging.info("")
    
        logging.info("Setting max_execution_date to XCom for Downstream Processes")
        context["ti"].xcom_push(key="max_date", value=max_date.isoformat())
    
    
    print_configuration = PythonOperator(
        task_id="print_configuration",
        python_callable=print_configuration_function,
        provide_context=True,
        dag=dag,
    )
    
    
    def build_query(
        session,
        airflow_db_model,
        age_check_column,
        max_date,
        dag_id=None
    ):
        """
        Build a database query to retrieve and filter Airflow data.
    
        Args:
            session: SQLAlchemy session object for database interaction.
            airflow_db_model: The Airflow model class to query (e.g., DagRun).
            age_check_column: The column representing the age of the data.
            max_date: The maximum allowed age for the data.
            dag_id (optional): The ID of the DAG to filter by. Defaults to None.
    
        Returns:
            SQLAlchemy query object: The constructed query.
        """
        query = session.query(airflow_db_model)
    
        logging.info("INITIAL QUERY : " + str(query))
    
        if hasattr(airflow_db_model, 'dag_id'):
            logging.info("Filtering by dag_id: " + str(dag_id))
            query = query.filter(airflow_db_model.dag_id == dag_id)
    
        if airflow_db_model == DagRun:
            newest_dagrun = (
                session
                .query(airflow_db_model)
                .filter(DagRun.external_trigger.is_(False))
                .filter(airflow_db_model.dag_id == dag_id)
                .order_by(desc(airflow_db_model.execution_date))
                .first()
            )
            logging.info("Newest dagrun: " + str(newest_dagrun))
    
            # For DagRuns we want to leave last *scheduled* DagRun
            # regardless of its age, otherwise Airflow will retrigger it
            if newest_dagrun is not None:
                query = (
                    query
                    .filter(airflow_db_model.id != newest_dagrun.id)
                )
    
        query = query.filter(age_check_column <= max_date)
        logging.info("FINAL QUERY: " + str(query))
    
        return query
    
    
    def print_query(query, airflow_db_model, age_check_column):
        entries_to_delete = query.all()
    
        logging.info("Query: " + str(query))
        logging.info(
            "Process will be Deleting the following "
            + str(airflow_db_model.__name__)
            + "(s):"
        )
        for entry in entries_to_delete:
            date = str(entry.__dict__[str(age_check_column).split(".")[1]])
            logging.info("\tEntry: " + str(entry) + ", Date: " + date)
    
        logging.info(
            "Process will be Deleting "
            + str(len(entries_to_delete))
            + " "
            + str(airflow_db_model.__name__)
            + "(s)"
        )
    
    
    def cleanup_function(**context):
        session = settings.Session()
    
        logging.info("Retrieving max_execution_date from XCom")
        max_date = context["ti"].xcom_pull(
            task_ids=print_configuration.task_id, key="max_date"
        )
        max_date = dateutil.parser.parse(max_date)  # stored as iso8601 str in xcom
    
        airflow_db_model = context["params"].get("airflow_db_model")
        state = context["params"].get("state")
        age_check_column = context["params"].get("age_check_column")
        keep_last = context["params"].get("keep_last")
        keep_last_filters = context["params"].get("keep_last_filters")
        keep_last_group_by = context["params"].get("keep_last_group_by")
    
        logging.info("Configurations:")
        logging.info("max_date:                 " + str(max_date))
        logging.info("enable_delete:            " + str(ENABLE_DELETE))
        logging.info("session:                  " + str(session))
        logging.info("airflow_db_model:         " + str(airflow_db_model))
        logging.info("state:                    " + str(state))
        logging.info("age_check_column:         " + str(age_check_column))
        logging.info("keep_last:                " + str(keep_last))
        logging.info("keep_last_filters:        " + str(keep_last_filters))
        logging.info("keep_last_group_by:       " + str(keep_last_group_by))
    
        logging.info("")
    
        logging.info("Running Cleanup Process...")
    
        try:
            if context["params"].get("do_not_delete_by_dag_id"):
                query = build_query(
                    session=session,
                    airflow_db_model=airflow_db_model,
                    age_check_column=age_check_column,
                    max_date=max_date,
                )
                if PRINT_DELETES:
                    print_query(query, airflow_db_model, age_check_column)
                if ENABLE_DELETE:
                    logging.info("Performing Delete...")
                    query.delete(synchronize_session=False)
                session.commit()
            else:
                dags = session.query(airflow_db_model.dag_id).distinct()
                session.commit()
    
                list_dags = [str(list(dag)[0]) for dag in dags] + [None]
                for dag_id in list_dags:
                    query = build_query(
                        session=session,
                        airflow_db_model=airflow_db_model,
                        age_check_column=age_check_column,
                        max_date=max_date,
                        dag_id=dag_id,
                    )
                    if PRINT_DELETES:
                        print_query(query, airflow_db_model, age_check_column)
                    if ENABLE_DELETE:
                        logging.info("Performing Delete...")
                        query.delete(synchronize_session=False)
                    session.commit()
    
            if not ENABLE_DELETE:
                logging.warning(
                    "You've opted to skip deleting the db entries. "
                    "Set ENABLE_DELETE to True to delete entries!!!"
                )
    
            logging.info("Finished Running Cleanup Process")
    
        except ProgrammingError as e:
            logging.error(e)
            logging.error(
                str(airflow_db_model) +
                " is not present in the metadata." +
                "Skipping..."
            )
    
        finally:
            session.close()
    
    
    def cleanup_sessions():
        session = settings.Session()
    
        try:
            logging.info("Deleting sessions...")
            count_statement = (
                "SELECT COUNT(*) AS cnt FROM session " +
                "WHERE expiry < now()::timestamp(0);"
            )
            before = session.execute(text(count_statement)).one_or_none()["cnt"]
            session.execute(
                text(
                    "DELETE FROM session WHERE expiry < now()::timestamp(0);"
                )
            )
            after = session.execute(text(count_statement)).one_or_none()["cnt"]
            logging.info("Deleted %s expired sessions.", (before - after))
        except Exception as err:
            logging.exception(err)
    
        session.commit()
        session.close()
    
    
    def analyze_db():
        session = settings.Session()
        session.execute("ANALYZE")
        session.commit()
        session.close()
    
    
    analyze_op = PythonOperator(
        task_id="analyze_query",
        python_callable=analyze_db,
        provide_context=True,
        dag=dag
    )
    
    cleanup_session_op = PythonOperator(
        task_id="cleanup_sessions",
        python_callable=cleanup_sessions,
        provide_context=True,
        dag=dag,
    )
    
    cleanup_session_op.set_downstream(analyze_op)
    
    for db_object in DATABASE_OBJECTS:
        cleanup_op = PythonOperator(
            task_id="cleanup_" + str(db_object["airflow_db_model"].__name__),
            python_callable=cleanup_function,
            params=db_object,
            provide_context=True,
            dag=dag,
        )
    
        print_configuration.set_downstream(cleanup_op)
        cleanup_op.set_downstream(analyze_op)

## Maintain database performance

  * Airflow database performance issues can lead to overall DAG execution issues. [Observe Database CPU and memory usage](https://docs.cloud.google.com/composer/docs/composer-2/use-monitoring-dashboard#db-statistics) statistics. If CPU and memory utilization approaches the limits, then the database is overloaded and requires scaling. The amount of resources available to the Airflow database is controlled by the environment size property of your environment. To scale the database up [change the environment size](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments) to a larger tier. Increasing the environment size increases the costs of your environment. 

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.




## Remove entries for unused DAGs

You can remove database entries for unused DAGs by [removing DAGs from the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#delete-md).

## What's next

  * [Configure database retention policy](https://docs.cloud.google.com/composer/docs/composer-3/configure-db-retention)
  * [Access Airflow command-line interface](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
