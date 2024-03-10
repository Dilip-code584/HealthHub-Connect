Health-Care-Access-Platform

Health Hub Using AI And Machine Learning Libraries

By harnessing the power of artificial intelligence, our innovative project is dedicated to transforming the realm of healthcare. 

Through the utilization of advanced predictive models, we aim to forecast the probability of developing critical conditions such as stroke, liver disease, heart ailments, diabetes, and pneumonia.
Our system leverages the latest trends and comprehensive patient data to offer precise and reliable insights, enabling early identification and proactive management of potential health risks. 

In this busy world where people dont have much time to get their blood pressure or cholestral checked, they can directly accesss our highly accurate website and directly get in touch with doctors if they find the chance of risk somewhere for some disease, this is more efficient and saves the time and money of both doctor and patients,Since AI is the future.

With a focus on preventive care, our AI-driven solution endeavors to empower individuals and healthcare providers with valuable information, fostering a proactive approach to health maintenance and disease prevention. 
Embracing the potential of AI, we are committed to revolutionizing healthcare by delivering personalized and data-driven predictions, ultimately contributing to improved patient outcomes and a healthier society.

Machine learning (ML) in healthcare has emerged as a game-changing force, revolutionizing diagnosis, treatment, and patient care.
Its ability to analyze vast datasets has paved the way for personalized medicine and predictive analytics, enhancing treatment outcomes and patient satisfaction.

ML algorithms are being employed to interpret medical images, predict disease progression, and optimize treatment plans, driving precision medicine and tailored interventions.
The integration of ML with wearable devices and remote monitoring has facilitated continuous health tracking and early intervention, empowering individuals to actively manage their health.


Furthermore, the trend towards explainable AI and ethical considerations in healthcare ML is shaping a transparent and responsible approach to leveraging these technologies for the benefit of patients, healthcare providers, and society as a whole.

Video of implementation-https://drive.google.com/file/d/1dZ-YSYTd1eFcLPyw25NrAooaVVPDbLat/view?usp=drive_link


I have predicted here in the video only for one disease,but we can do the same for all...

All the necessary libraries such as tensorflow,xgboost,numpy scikit-learn etc.. I have referenced them directly in the requirements.txt file which can directly be installed just by referncing that-


How a typical Hospital Mangement implementation system looks like-


Usercase Diagram-

![image](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/40514b6a-d584-4ee4-a7eb-a67bb10c5b31)


Class Diagram-


![image](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/694cfe3c-527d-45bc-91a0-e0726bcaaed1)


How the system works like-

![image](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/015b5ce3-b624-401d-8547-2de72fda8972)


Sequence Project-

![image](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/31bfc8f4-6056-4207-a007-af9c2e8cea64)





Please note for the above ones I just referenced how hospital system works like,this has no link with my project..


In my application AltairCare i have used machine learning and deep learning algorithms to train highly accurate models and thus allowing users to check their chance of having one of the following diseases:

    Liver Disease
    Pneumonia Disease
    Kidney Disease
    Diabete Disease
    Stroke Disease
    Heart Disease


Prediction Page-


![Screenshot from 2024-03-10 00-22-48](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/d9860799-d502-40d7-9d84-280cc511df75)


Each Disease have it's own page with an overview and symptoms that patient may have, and also the prediction model information and required parameters that user must provide

Disease Page-

![Screenshot from 2024-03-10 00-19-21](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/3d95c653-ac83-4bd6-9fc0-b7f20041f49f)

![Screenshot from 2024-03-10 00-32-20](https://github.com/Dilip-code584/HealthHub-Connect/assets/128896508/856337dc-d099-421a-b645-7a350ab727f5)

All the datasets used to train the models can be found in the Kaggle website
Libraries Used :

    Flask: for backend web development
    Scikit-learn & tensorflow: for training the diseases prediction models
    sqlalchemy: library for handling sqlite database

    Here for frontend I have used html css and js

    Whereas for backend I have used much of python and libraries imported which i have referenced above-
    

 How to run this project :

 
Clone this repository:

git clone https://github.com/Dilip-code584/HealthHub-Connect


Install requirements (using a virtual environment is highly recommended):

Optional(but recommended)-

Creating virtual enviornment-

python3 -m venv myenv

 source myenv/bin/activate

Mandatory Steps-

pip install -r requirements.txt


Run this command to start local server:

python3 app.py


(Optional)

You can also try out go for implementing blockchain , done via hyperledger fabric chaincode make sure you have installed that,


 This provides basic functionality for patients to store their data and hospitals to access it, while ensuring data integrity and confidentiality.

 By Using Such Functionalities.., I have uploaded the go file also above.


import (
	"encoding/json"
	"errors"

	"github.com/hyperledger/fabric/core/chaincode/shim"
	"github.com/hyperledger/fabric/protos/peer"
)

// PatientChaincode represents the chaincode implementation
type PatientChaincode struct {
}

// PatientData represents the structure of patient data
type PatientData struct {
	PatientID string `json:"patientID"`
	Data      string `json:"data"`
}

// AccessControlContract represents the access control smart contract
type AccessControlContract struct {
}

// GrantAccess grants access to a hospital for a patient's data
func (ac *AccessControlContract) GrantAccess(patientID string, hospitalID string) error {
	// Implement access control logic here
	

// GetPatientData retrieves patient data for a hospital
func (ac *AccessControlContract) GetPatientData(patientID string, hospitalID string) (*PatientData, error) {
	// Implement logic to retrieve patient data
	// For simplicity, we return hardcoded patient data
	if patientID == "patient1" {
		return &PatientData{
			PatientID: "patient1",
			Data:      "Medical history: Lorem ipsum dolor sit amet...",
		}, nil
	} else {
		return nil, errors.New("patient not found")
	}
}

// Init initializes the chaincode
func (cc *PatientChaincode) Init(stub shim.ChaincodeStubInterface) peer.Response {
	return shim.Success(nil)
}

// Invoke handles invocations of the chaincode
func (cc *PatientChaincode) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
	function, args := stub.GetFunctionAndParameters()

	switch function {
	case "GrantAccess":
		return cc.GrantAccess(stub, args)
	case "GetPatientData":
		return cc.GetPatientData(stub, args)
	default:
		return shim.Error("Invalid function name")
	}
}

// GrantAccess grants access to a hospital for a patient's data
func (cc *PatientChaincode) GrantAccess(stub shim.ChaincodeStubInterface, args []string) peer.Response {
	if len(args) != 2 {
		return shim.Error("Incorrect number of arguments. Expecting 2: patient



 
Last but not the least-

Dear ACM NITK, Spider R&D NITT, and CSEA NITW,

Thank you for providing me this incredible opportunity to participate in the 36-hour hackathon.
It was an enriching experience to present my project on disease prediction using machine learning using helathcare acces platform.
Your support and encouragement mean the world to me, and I am grateful for the platform you provided to showcase my skills and innovation
