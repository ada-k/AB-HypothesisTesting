## AB-HypothesisTesting
 Ad campaign performance evaluation using AB Testing
 
**Case Overview**:
SmartAd is a mobile first advertiser agency. It is running an online ad for a client with the intention of increasing brand awareness. 
The company provides an additional service called Brand Impact Optimizer (BIO), a lightweight questionnaire, served with every campaign to determine the impact of the ad they design. 

**Objectives**:
The task at hand is to design a reliable hypothesis testing algorithm for the BIO service and determine whether the recent advertising campaign resulted in significant lift in brand awareness.

**Methods**
* Sequential A/B testing.
* Classic A/B testing.
* A/B testing with Machine Learning.

**Conclusion**: 
The classical test shows a 1.2% lift in brand awareness which is higher than the minimum detectable change set. The Machine Learning approach indicates the experiment (exposed and control user groups)  feature is significant. All this implies there was a significant lift in brand awareness.

### Project Structure
The repository has a number of files that include notebooks, slides and setup files. They include:

`README.md` : Markdown text with a brief explanation of the project and the repository structure.

`LICENCE` : License template.

`requiremets.txt` : Dependancies file.

`slide(ada).pdf` : Project slide.

`kernels folder`: Has 4 jupyter notebooks:

 * ML_testing.ipynb - Machine Learn Approach to the AB test.

 * classic_testing.ipynb- Classic AB testing approach.

 * sequential_testing.ipynb- Sequential AB testing approach. 

 * eda.ipynb**- Notebook containing the explatory data analysis for the project
  
 
`scripts folder`: Has 4 python scripts:
     
 * ML_testing.py - python script for the ML notebook.

 * classic_testing.py- python script for the classic ab testing notebook.

 * sequential_testing.py- python script for the sequential ab testing notebook.

 * eda.py-python script for the eda notebook.

 * txt_file _merger.py- Requirements files merger.


`setup.py, AB-HypothesisTesting, dist, build/lib/AB-HypothesisTesting, AB_tests.egg-info` : Pip setup files.

**Installation**

`Install the dependenacies in requirements.txt`

`pip install -i https://test.pypi.org/simple/ AB-tests==0.0.1`



