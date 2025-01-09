import requests

BASE_URL = "http://localhost:8000/api"

class CCDServices:

    def register_patient(self, patient_info):
        # Headers for the POST request
        headers = {
            "Content-Type": "application/json"
        }

        # Sending the POST request
        response = requests.post(BASE_URL+'/patient/registration/', json=patient_info, headers=headers)

        # Printing the response
        print("Status Code:", response.status_code)
        print("Response Body:", response.json())


# Payload for the POST request
payload = {
    "username": "Aakash123",
    "email": "aaaaa@gmail.com",
    "first_name": "Aakash",
    "last_name": "Aggarwal",
    "password1": "aakash@123",
    "password2": "aakash@123",
    "dob": "1999-06-13T00:00:00Z",
    "gender": "male",
    "ehr_code": "",
    "user_profile": {
        "address": "78 Wall Street mexico city",
        "phone": "",
        "preferred_alert_mode": "Email",
        "secondary_alert_mode": "Email"
    }
}

CCDServices().register_patient(patient_info=payload)


