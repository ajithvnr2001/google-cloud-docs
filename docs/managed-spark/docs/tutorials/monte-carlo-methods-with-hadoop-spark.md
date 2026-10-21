---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/monte-carlo-methods-with-hadoop-spark/
title: Monte Carlo methods using Apache Spark \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:17.090215+00:00
---

# Monte Carlo methods using Apache Spark  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/monte-carlo-methods-with-hadoop-spark/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Monte Carlo methods using Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) and [Apache Spark](https://spark.apache.org/) provide infrastructure and capacity that you can use to run Monte Carlo simulations written in Java, Python, or Scala.

Monte Carlo methods can help answer a wide range of questions in business, engineering, science, mathematics, and other fields. By using repeated random sampling to create a probability distribution for a variable, a Monte Carlo simulation can provide answers to questions that might otherwise be impossible to answer. In finance, for example, pricing an equity option requires analyzing the thousands of ways the price of the stock could change over time. Monte Carlo methods provide a way to simulate those stock price changes over a wide range of possible outcomes, while maintaining control over the domain of possible inputs to the problem.

In the past, running thousands of simulations could take a very long time and accrue high costs. Managed Service for Apache Spark enables you to provision capacity on demand and pay for it by the minute. Apache Spark lets you use clusters of tens, hundreds, or thousands of servers to run simulations in a way that is intuitive and scales to meet your needs. This means that you can run more simulations more quickly, which can help your business innovate faster and manage risk better.

Security is always important when working with financial data. Managed Service for Apache Spark runs on Google Cloud, which helps to keep your data [safe, secure, and private](https://cloud.google.com/security) in several ways. For example, all data is encrypted during transmission and when at rest, and Google Cloud is [ISO 27001, SOC3, and PCI compliant](https://cloud.google.com/compliance).

## Objectives

  * Create a managed Managed Service for Apache Spark cluster with [Apache Spark pre-installed](https://docs.cloud.google.com/managed-spark/docs/concepts/dataproc-versions#supported_cloud_dataproc_versions).
  * Run a Monte Carlo simulation using Python that estimates the growth of a stock portfolio over time.
  * Run a Monte Carlo simulation using Scala that simulates how a casino makes money.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/resources/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  * Set up a Google Cloud project 

    1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
    2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

       * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
       * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

    3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

    4. Enable the Dataproc and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component)

    5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
           
           gcloud init

    8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

       * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
       * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

    9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

    10. Enable the Dataproc and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component)

    11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
           
           gcloud init




## Create a Managed Service for Apache Spark cluster

Follow the steps to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster) from the Google Cloud console. The default cluster settings, which includes two-worker nodes, is sufficient for this tutorial.

## Disable logging for warnings

By default, Apache Spark prints verbose logging in the console window. For the purpose of this tutorial, change the logging level to log only errors. Follow these steps:

### Use `ssh` to connect to the Managed Service for Apache Spark cluster's primary node

The primary node of the Managed Service for Apache Spark cluster has the `-m` suffix on its VM name.

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)




An SSH window opens connected to the primary node.
    
    
    Connected, host fingerprint: ssh-rsa 2048 ...
    ...
    user@clusterName-m:~$
    

### Change the logging setting

  1. From the primary node's home directory, edit `/etc/spark/conf/log4j.properties`.
         
         sudo nano /etc/spark/conf/log4j.properties
         

  2. Set `log4j.rootCategory` equal to `ERROR`.
         
         # Set only errors to be logged to the console
         log4j.rootCategory=ERROR, console
         log4j.appender.console=org.apache.log4j.ConsoleAppender
         log4j.appender.console.target=System.err
         log4j.appender.console.layout=org.apache.log4j.PatternLayout
         log4j.appender.console.layout.ConversionPattern=%d{yy/MM/dd HH:mm:ss} %p %c{1}: %m%n
         

  3. Save the changes and exit the editor. If you want to enable verbose logging again, reverse the change by restoring the value for `.rootCategory` to its original (`INFO`) value.




## Spark programming languages

Spark supports Python, Scala, and Java as programming languages for standalone applications, and provides interactive interpreters for Python and Scala. The language you choose is a matter of personal preference. This tutorial uses the interactive interpreters because you can experiment by changing the code, trying different input values, and then viewing the results.

## Estimate portfolio growth

In finance, Monte Carlo methods are sometimes used to run simulations that try to predict how an investment might perform. By producing random samples of outcomes over a range of probable market conditions, a Monte Carlo simulation can answer questions about how a portfolio might perform on average or in worst-case scenarios.

Follow these steps to create a simulation that uses Monte Carlo methods to try to estimate the growth of a financial investment based on a few common market factors.

**Note:** This code is provided only as an example. Don't use this code to make investment decisions.

  1. Start the Python interpreter from the Managed Service for Apache Spark primary node.
         
         pyspark
         

Wait for the Spark prompt `>>>`.

  2. Enter the following code. Make sure you maintain the indentation in the function definition.
         
         import random
         import time
         from operator import add
         
         def grow(seed):
             random.seed(seed)
             portfolio_value = INVESTMENT_INIT
             for i in range(TERM):
                 growth = random.normalvariate(MKT_AVG_RETURN, MKT_STD_DEV)
                 portfolio_value += portfolio_value * growth + INVESTMENT_ANN
             return portfolio_value
         

  3. Press `return` until you see the Spark prompt again.

The preceding code defines a function that models what might happen when an investor has an existing retirement account that is invested in the stock market, to which they add additional money each year. The function generates a random return on the investment, as a percentage, every year for the duration of a specified term. The function takes a seed value as a parameter. This value is used to reseed the random number generator, which ensures that the function doesn't get the same list of random numbers each time it runs. The `random.normalvariate` function ensures that random values occur across a [normal distribution](https://wikipedia.org/wiki/Normal_distribution) for the specified mean and standard deviation. The function increases the value of the portfolio by the growth amount, which could be positive or negative, and adds a yearly sum that represents further investment.

You define the required constants in an upcoming step.

  4. Create many seeds to feed to the function. At the Spark prompt, enter the following code, which generates 10,000 seeds: 
         
         seeds = sc.parallelize([time.time() + i for i in range(10000)])
         

The result of the `parallelize` operation is a [resilient distributed dataset (RDD)](https://spark.apache.org/docs/latest/rdd-programming-guide.html), which is a collection of elements that are optimized for parallel processing. In this case, the RDD contains seeds that are based on the current system time.

When creating the RDD, Spark slices the data based on the number of workers and cores available. In this case, Spark chooses to use eight slices, one slice for each core. That's fine for this simulation, which has 10,000 items of data. For larger simulations, each slice might be larger than the default limit. In that case, specifying a second parameter to `parallelize` can increase the number slices, which can help to keep the size of each slice manageable, while Spark still takes advantage of all eight cores.

  5. Feed the RDD that contains the seeds to the growth function.
         
         results = seeds.map(grow)
         

The `map` method passes each seed in the RDD to the `grow` function and appends each result to a new RDD, which is stored in `results`. Note that this operation, which performs a _transformation_ , doesn't produce its results right away. Spark won't do this work until the results are needed. This _lazy evaluation_ is why you can enter code without the constants being defined.

  6. Specify some values for the function.
         
         INVESTMENT_INIT = 100000  # starting amount
         INVESTMENT_ANN = 10000  # yearly new investment
         TERM = 30  # number of years
         MKT_AVG_RETURN = 0.11 # percentage
         MKT_STD_DEV = 0.18  # standard deviation
         

  7. Call `reduce` to aggregate the values in the RDD. Enter the following code to sum the results in the RDD:
         
         sum = results.reduce(add)
         

  8. Estimate and display the average return:
         
         print (sum / 10000.)
         

Be sure to include the dot (`.`) character at the end. It signifies floating-point arithmetic.

  9. Now change an assumption and see how the results change. For example, you can enter a new value for the market's average return:
         
         MKT_AVG_RETURN = 0.07
         

  10. Run the simulation again.
         
         print (sc.parallelize([time.time() + i for i in range(10000)]) \
                 .map(grow).reduce(add)/10000.)
         

  11. When you're done experimenting, press `CTRL+D` to exit the Python interpreter.




## Program a Monte Carlo simulation in Scala

Monte Carlo, of course, is famous as a gambling destination. In this section, you use Scala to create a simulation that models the mathematical advantage that a casino enjoys in a game of chance. The "house edge" at a real casino varies widely from game to game; it can be over 20% in [keno](https://wikipedia.org/wiki/Keno), for example. This tutorial creates a simple game where the house has only a one-percent advantage. Here's how the game works:

  * The player places a bet, consisting of a number of chips from a bankroll fund.
  * The player rolls a 100-sided die (how cool would that be?).
  * If the result of the roll is a number from 1 to 49, the player wins.
  * For results 50 to 100, the player loses the bet.



You can see that this game creates a one-percent disadvantage for the player: in 51 of the 100 possible outcomes for each roll, the player loses.

Follow these steps to create and run the game:

  1. Start the Scala interpreter from the Managed Service for Apache Spark primary node.
         
         spark-shell
         

  2. Copy and paste the following code to create the game. Scala doesn't have the same requirements as Python when it comes to indentation, so you can simply copy and paste this code at the `scala>` prompt.
         
         val STARTING_FUND = 10
         val STAKE = 1   // the amount of the bet
         val NUMBER_OF_GAMES = 25
         
         def rollDie: Int = {
             val r = scala.util.Random
             r.nextInt(99) + 1
         }
         
         def playGame(stake: Int): (Int) = {
             val faceValue = rollDie
             if (faceValue < 50)
                 (2*stake)
             else
                 (0)
         }
         
         // Function to play the game multiple times
         // Returns the final fund amount
         def playSession(
            startingFund: Int = STARTING_FUND,
            stake: Int = STAKE,
            numberOfGames: Int = NUMBER_OF_GAMES):
            (Int) = {
         
             // Initialize values
             var (currentFund, currentStake, currentGame) = (startingFund, 0, 1)
         
             // Keep playing until number of games is reached or funds run out
             while (currentGame <= numberOfGames && currentFund > 0) {
         
                 // Set the current bet and deduct it from the fund
                 currentStake = math.min(stake, currentFund)
                 currentFund -= currentStake
         
                 // Play the game
                 val (winnings) = playGame(currentStake)
         
                 // Add any winnings
                 currentFund += winnings
         
                 // Increment the loop counter
                 currentGame += 1
             }
             (currentFund)
         }
         

  3. Press `return` until you see the `scala>` prompt.

  4. Enter the following code to play the game 25 times, which is the default value for `NUMBER_OF_GAMES`.
         
         playSession()
         

Your bankroll started with a value of 10 units. Is it higher or lower, now?

  5. Now simulate 10,000 players betting 100 chips per game. Play 10,000 games in a session. This Monte Carlo simulation calculates the probability of losing all your money before the end of the session. Enter the follow code:
         
         (sc.parallelize(1 to 10000, 500)
           .map(i => playSession(100000, 100, 250000))
           .map(i => if (i == 0) 1 else 0)
           .reduce(_+_)/10000.0)
         

Note that the syntax `.reduce(_+_)` is shorthand in Scala for aggregating by using a summing function. It is functionally equivalent to the `.reduce(add)` syntax that you saw in the Python example.

The preceding code performs the following steps:

     * Creates an RDD with the results of playing the session.
     * Replaces bankrupt players' results with the number `1` and nonzero results with the number `0`.
     * Sums the count of bankrupt players.
     * Divides the count by the number of players.

A typical result might be:
    
    0.998
    

Which represents a near guarantee of losing all your money, even though the casino had only a one-percent advantage.




## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * For more on submitting Spark jobs to Managed Service for Apache Spark without having to use `ssh` to connect to the cluster, read [Managed Service for Apache Spark—Submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
