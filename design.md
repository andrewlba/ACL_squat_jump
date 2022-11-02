# Design:

### User Type 1: Dr. Jane (Main User)

**User Need**: Jane is a physician who wants to visualize force data from the jumping force plates. She wants to be able to see the numerical differences between the two legs using graphs.

**Use Case**: She will be using this tool to analyze patient progress and relay medical information to the patients in a straightforward way.

0. Identify patient
1. Identifying the information required for care (i.e., which metrics are needed?)
2. Calculate the metrics
3. Perform visualization on the calculated metrics

**Skill Level**: Can understand the data but cannot program/code themselves.


### User Type 2: John Doe (Administrative Role)

**User Need**: John is the doctor's assistant. He uploads specific datasets for the softward to aid the physician in providing a more informed care for the patient.

**Use Case**: John will be using this tool to upload data for creating visualizations and curate relevant visualization to deliver to the physician.

1. Collect new patient data as csv
2. Upload collected data to the tool
3. (If any) If issues come up, ensure that data is clean and that tool outputs appropriate visualizations. 

**Skill Level**: Familiar with the datasets used. Not great at interpreting the results at a medical level.

### Components

#### High-level Tool Operating Process

1. Data Cleaning
    - Input: CSV from force plate (TBD: Specification of column types)
    - Output: Usable data for metric computation and visualization
2. Data Processing (i.e., Metrics Calculation)
    - Contains functions for generating metrics that are used for visualization 
3. Dashboard Visualization
    - Contains visualization display

#### List of Components

**1. Database:**:
Usage: Store the CSV data files that are retrieved from the force plates. [TO BE CHANGED]

**2. Raw Data:** 
Usage: The raw CSV data file containing numeric values (ordered by time, partitioned by user)

**2. Keyboard:**
Usage: To interact with the software.

**3. Git/GitHub:**
Usage: Version Control software for collaboration and hosting data/data-tools.

**5. Pandas/NumPy/Math:**
Usage: Scientific stack of Python Libraries to be used in data cleaning, and metric calculations.

**6. Utils Functions:**
Usage: Distinct python file containing utility functions to be used in data processing.

**7. Streamlit:**
Usage: Web Interface to display visualizations of our data.

**8. Screen:**
Usage: Used to see the visualizations

**9. Visualization Functions:**
Usage: Used to create the visualizations


### Use Cases:

#### 1: Data Cleaning and Pre-Processing:
Import and cleans the CSV data files that are retrieved from the force plates

**Input Components:**:
1. Raw Data: CSV file

Tools to be used:

1. Keyboard
2. Git/GitHub
3. Scientific Stack (Python Libraries)
4. Screen 

**Output Components:**:
1. Clean Dataset: NumPy Array
2. Status Report: Boolean value representing Success/Failure

#### 2: Data Processing:
Calculating biomechanical features from the Cleaned Data to create clinically interpretable metrics to be used in data visualization

**Input Components:**:
1. Clean Dataset

Tools to be used:

1. Utils Functions
2. Scientific Stack (Python Libraries)

**Output Components:**:
1. Processed Dataframe: Pandas DataFrame
2. Status Report: Boolean value representing Success/Failure

#### 3: Data Visualization:
Visualizing the calculated biomechanical metrics

**Input Components:**:
1. Processed Dataframe

Tools to be used:

1. Visualization Functions
2. Streamlit
3. Python Libraries (Seaborn, Plotly)
4. GitHub: to launch the Streamlit App

**Output Components:**:
1. Streamlit Dashboard
