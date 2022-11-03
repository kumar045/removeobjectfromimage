 <center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

## Exercise: Using AutoAI to predict outcomes!

Estimated time needed: 45 mins

Objective for Exercise:

- How to create a project in Watson Studio Service and add a Watson Machine Learning Service.
- Learn how to utilize Watson AutoAI to predict the likelihood of a particular outcome based on input data.
- Create and Train a model using sample data.

You\'re on the marketing team for a bank and your team is launching a
new campaign. In order to launch the most effective campaign, you need
to determine who to target in the campaign based on the likelihood that
your target audience will respond to the messaging.

**NOTE**: For learners working to get a certificate for this course (i.e.
not auditing), please go through this exercise carefully and thoroughly
it will be used for the graded assignment that follows.

## Pre-requisites

You will need an IBM Cloud account to do this lab. If you have not created one already, click on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CC0100EN-SkillsNetwork/labs/IBMCloud_accountCreation/CreateIBMCloudAccount.md.html) and follow the instructions to create an IBM Cloud account.

## Step 1: Add a Watson Machine Learning Service Instance

1. We need to add an instance of the Watson Machine Learning service to your account. This will be used later when you set up the rest of the assets for the project. From your Dashboard page, click or tap the **Create Resource** button at the top right of the page.

2. From the catalog page that loads, Click on the **services**, select the **AI** category and then select the **Watson Machine Learning** service from the list.

![](/images/2.png)


3. In the Watson Machine Learning setup page, select the *Region* as appropriate to your location. In this example, **DALLAS** has been chosen. Verify that the Lite plan is selected, and then click Create.
  

>Note: If you created a Watson Machine Learning instance in the past using the Lite plan, you won\'t be allowed to create a second instance. You can use the instance you already created for this exercise or you\'ll need to delete your previous instance and create a new one.

![](/images/3.png)
 

## Step 2: Create a Watson Studio Resource

In this step, you will be using Watson Studio to see AI in action. If you already have a Watson Studio resource set up, you can skip to step 4.

To manage all your projects, you will use IBM Watson Studio. In this exercise, you will add Watson Studio as a Resource.

1. In the IBM Cloud **Catalog** go to the Watson Studio listing - [cloud.ibm.com/catalog/services/watson-studio](https://cloud.ibm.com/catalog/services/watson-studio)

2. On the Watson Studio page, select DALLAS as the Region, verify that the **Lite** plan is selected, and then click **Create**.

<img src="./images/5-create_watson_studio_lite.jpg" style="border:1px solid grey;margin-left=30px; margin-top=30px;margin-bottom=30px"/>


3. Open the [IBM cloud resources page](https://cloud.ibm.com/resources?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-wwwcourseraorg-SkillsNetworkCoursesIBMDeveloperSkillsNetworkAI0101ENSkillsNetwork20718152-2022-01-01)

> 📷 Save a screenshot of this page in your account and save it as 'resourcepage' in .jpg or .png format. You will be asked to upload it for the final project grading. The screenshot of the resources page must show both the Waston Studio and the Machine Learning services active.

4. Once the Watson Studio instance is successfully created, click on **Launch in IBM Cloud Pak for Data**.

![](/images/5.png)

5. Once you get started, the first time, your IBM Cloud Pak for Data core services is provisioned.

<img src="./images/provisioning.png" style="border:1px solid grey;margin-left=30px; margin-top=30px;margin-bottom=30px"/>

6. You will a pop-up, click on **New Project** and click on **Next** to proceed.
![](/images/Screenshot%20(2954).png)

## Step 3: Create a Project

1. On the **New Project** page, enter a name for your project (we suggest using \"Auto AI Exercise\" or something similar) and, if you\'d like, a description.
![](/images/171.png)

2. You must define storage for your project before you can create it. If you already have an instance of Cloud Object Storage, you can select it, otherwise under Select storage service, click Add. Now on the Cloud Object Storage page, verify that Lite plan is selected, and then click Create.

![](/images/os2.png)

3. Now on the Create Project page, under Define storage, you may need to click Refresh to see the newly created instance of Cloud Object Storage (COS).

![](/images/os4.png)

4. Once an instance of Cloud Object Storage (COS) is listed, click Create to create the Project.

![](/images/77.png)


## Step 4: Add Auto AI Asset to Your Project

1. On the project page, go to the "Assets" and click on **New asset** button to add a new tool to your project.

![](/images/Screenshot%20(2972).png)
![](/images/Screenshot%20(2973).png)
2. Now, select the AutoAI tool to add this to your project.

![](/images/191.png)

3. On the Create an **AutoAI** experiment page, there are multiple samples provided under the Gallery sample,  please select the **Bank Marketing Sample Data** for this lab and click on **Next**.

![](/images/15.png)

4. In order to use AutoAI, you will need to associate a machine learning service with your project. If a machine learning service is not associated with your project, you can associate one under the **Define Configuration** section on this page. Click the link, **Associate a Machine Learning service instance** to start the association flow.

![](/images/Screenshot%20(2977).png)

5. Associate the Machine Learning service you created in an earlier step in this exercise. select a machine learning service and click **Associate**.

![](/images/Screenshot%20(2979).png)

6. After the service is associated, you will be taken back to the experiment details page. Click or tap the **Reload** button to refresh the machine learning association. Your machine learning instance should now show under the \"Define Configuration\" section.
![](/images/Screenshot%20(2980).png)
7. Now click the **Create** button and your AutoAI asset will be created in your project.
![](/images/Screenshot%20(2980)1.png)


## Step 5: Run the Experiment

1. When the \"Bank marketing sample data experiment\" page loads Now you\'re ready to analyze the sample data. Click the **Run experiment** button.

![](/images/Screenshot%20(2987).png)
</details>

Now, Let the classifier run until it\'s complete. You will see a visual representation of the work being done. You see a message on the right-hand side of the page when the experiment is complete. In the diagram on the left of the page, you\'ll see various pipelines that represent the experiments that were run. One pipeline will be starred. This shows the most effective experiment.

![](/images/Screenshot%20(2999).png)

> 📷 Save a screenshot of this page in your account and save it as 'experimentcompleted' in .jpg or .png format for the assignment.

## Step 6: Save the Model

1. On the experiment summary page, scroll down to the Pipeline leader board. Hover over the pipeline that has the first ranking in the list until the **Save as** button appears click it and then under **select asset type** select **Model** and click the Create button.

![](/images/Screenshot%20(3000).png)

>📷 Save a screenshot of this page in your account and save it as 'savedmodel' in .jpg or .png format for the assignment.

![](/images/Screenshot%20(3001).png)



## Step 7: Create a Deployment

1. In this step, you're going to deploy the model you just created to a web service so it can take input data. Under the model section, click on the model you saved:

![](/images/25.png)

2. Go to **Promote to deployment space**

![](/images/Screenshot%20(3003).png)

3. In the **Promoto to space page**, from the **Target space** dropdown select **Create a new deployment space** from you're going to deploy the model you just created to a web service so it can take input data.
![](/images/Screenshot%20(3004).png)
4. Give a name to the New deployment space and then click Create button
![](/images/Screenshot%20(3006).png)
5. When the pop up come **The space is ready** then close it and click on the **Promote** button
![](/images/Screenshot%20(3008).png)

![](/images/Screenshot%20(3009).png)

6. Go to the Watson Studio homepage, and click on **Deployments** and under the **Deployment Space** click on **Manage** and then click on **Associate instance** it will load **WatsonMachineLearning** instance and then select it from the drop down menu

![](/images/Screenshot%20(3011).png)
![](/images/Screenshot%20(3012).png)
![](/images/Screenshot%20(3013).png)



7. Under the **Deployment Space** click on **Assets** and then click on three dots and select **Deploy**

![](/images/Screenshot%20(3014).png)
![](/images/Screenshot%20(3015).png)
8. Under **Create a deployment** select Deployment type **Online** and give it a Name and click Create button
![](/images/Screenshot%20(3016).png)

9. Then click on **Deployments** and wait sometime it will deploy yopur model and finally it will be deployed

![](/images/Screenshot%20(3018).png)

1. 📷 Save a screenshot of this page in your account and save it as 'deploymentspace' in .jpg or .png format for the assignment.
![](/images/Screenshot%20(3019).png)

2. 📷 Save a screenshot of this page in your account and save it as 'deployedmodel' in .jpg or .png format for the assignment.

## Step 9: Test Your Deployment

1. Now that you have your model deployed, you\'re ready to test it with some data. On the deployment page you just opened, click the **Deploy**. Then click on **Test** tab and insert data in the first row of Text input table

input_data": 27,"unemployed", "married", "primary", "no",1787,"no", "no","cellular",19,"oct", 79, 1, -1, 0, "unknown"

![](/images/Screenshot%20(3021).png)
![](/images/Screenshot%20(3022).png)


2. To test the model, click **Predict** button it will show your output as a classification score and with label

![](/images/Screenshot%20(2998).png)

-   📷 Take a screenshot of your output result and save it to your local computer

-   For practice, you can change values two more times, run the model, and take and save screenshots after each run and save them to your computer.

We just used AI machine learning to predict how a customer is likely to respond to an effort by a bank to get their customers to enroll in a program using a marketing pitch! Can you think of ways a real bank could use this information to help them run their marketing campaigns?

> 📷 Save a screenshot of this page in your account and save it as 'result' in .jpg or .png format for the assignment.

[Follow Rav Ahuja](https://twitter.com/ravahuja)

## Author(s)

[Rav Ahuja](https://www.linkedin.com/in/ravahuja/)

## Contributor(s)

[Srishti Srivastava](linkedin.com/in/srishti-srivastava-343095a8)

## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2022-11-02 | 2.0 | Ratima | Added lab to the course |


## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
