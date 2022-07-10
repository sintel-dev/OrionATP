# OrionATP
Acquirer, Transformer, and Publisher for Data Analysis and Visualization using the Orion library in Python

Take time series data straight from API, detect anomalies using Orion library, and visualize using Streamlit. Scripts will run once a day as scheduled by the workflow for consistent analysis and progress tracking.

Key Instructions:
Step 1: Inpuut API Key and name of time and value metric in api.txt, in that precise order. This is the file that the acquisition script will read from in order to collect and aggregate the data successfully. Note: You will need to know the labels of the columns for your time and value metric in order for this workflow to run successfully.

Step 2: Input desired Pipeline and Hyperparameters into pipeline.json and hyperparameters.json respectively. This can simply be copy/pasted from Orion library's list of pipelines. These files exist so the pipeline and hyperparameters can be changed easily without having to edit the scripts themselves.

Step 3: When you fork this repo, deploy this app using https://streamlit.io/ and Python 3.7. We're currently trying to figure out if it is possible to omit this step.

Step 4: Go into your repository settings and enable GitHub pages. This is so you don't have to use the streamlit link when trying to view the visualization results.

Step 5: Manually trigger the workflow or wait for it to trigger on schedule. You should be all set!
