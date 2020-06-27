from django import forms
from .models import problems,patient,doctors,nurses,ambulances,hospital,file2links,chats
class ProblemsForm(forms.ModelForm):
    class Meta:
        model = problems
        fields = [
            "username",
            "patient_name",
            "age",
            "Address",    
            "fever",
            "dry_cough",
            "fatigue",
            "sputum_production",
            "shortness_of_breath",
            "mussle_or_joint_pain",
            "sore_throat",
            "headache",
            "chills",
            "nausea_or_vomiting",
            "nasal_congestion",
            "diarrhoea",
            "others",
            "File",
            "sendid",
            "Payment_Proof",

        ]
        widgets = {
            "username": forms.HiddenInput(),
            "patient_name": forms.TextInput(attrs={'class': 'form-control','placeholder':'Write Patient Name'}),
            "age": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. 20'}),
            "Address": forms.TextInput(attrs={'class': 'form-control','placeholder':'Type patient address'}),
            "sendid": forms.TextInput(attrs={'class': 'form-control','placeholder':'Write Doctor Id or Hospital Id'}), 
            "others": forms.Textarea(attrs={'class': 'form-control','placeholder':'Describe Your Problems......',"rows":"3"}), 
        }
        labels = {
        "File": "Upload a File",
        "sendid": "Send It To ",
        "Payment_Proof" : "Payment Proof (if any)"
    }
class Patients(forms.ModelForm):
    class Meta:
        model = patient
        fields = [
            "username",
            "sugar",
            "Sugar_Report",
            "pressure",
            "Presure_Report",
            "heart",
            "Heart_Report",
            "Any_Operation",
            "Report",
            "Any_Other_Report",


        ]
        widgets = {
            "username": forms.HiddenInput(),

        }
class Doctor(forms.ModelForm):
    class Meta:
        model = doctors
        fields = [
            "username",
            "collage",
            "university",
            "Passing_Year",
            "Experience",
            "Upload_Profile_Pic",
            "Degrees",
            "Supporting_Document",
            "Home_Address",
            "Your_Supporting_Document",
            "Hospital_or_Chamber_Address_1",
            "Hospital_or_Chamber_Address_2",
            "Hospital_or_Chamber_Address_3",
            "Hospital_or_Chamber_Address_4",
            "Hospital_or_Chamber_Address_5",
            "Specialist_of",
            "Fees",
            "Online_Banking_QR_Code_for_Online_Payment"
        ]
        
        widgets = {
            "username": forms.HiddenInput(), 
            "collage": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Calcutta Medical College (C.M.C.)'}), 
            "university": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. AIIMS Delhi'}), 
            "Passing_Year": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. 2012'}), 
            "Experience": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. 5 year'}), 
            #"Upload_Profile_Pic": forms.TextInput(attrs={'class': 'form-control-file','id':'exampleFormControlFile1'}), 
            "Degrees": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. MBBS,MD,PHD'}),
            "Home_Address": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
            "Hospital_or_Chamber_Address_1": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}), 
            "Hospital_or_Chamber_Address_2": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
            "Hospital_or_Chamber_Address_3": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
            "Hospital_or_Chamber_Address_4": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
            "Hospital_or_Chamber_Address_5": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
            "Specialist_of": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Child Specialist, ENT Specialist etc.'}),
        }


        
class Nurse(forms.ModelForm):
    class Meta:
        model = nurses
        fields = [
            "username",
            "collage",
            "university",
            "Passing_Year",
            "Experience",
            "Upload_Profile_Pic",
            "Degrees",
            "Supporting_Document",
            "Home_Address",
            "Your_Supporting_Document",
        ]
        
        widgets = {
            "username": forms.HiddenInput(), 
            "collage": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Calcutta Medical College (C.M.C.)'}), 
            "university": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. AIIMS Delhi'}), 
            "Passing_Year": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. 2012'}), 
            "Experience": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. 5 year'}), 
            #"Upload_Profile_Pic": forms.TextInput(attrs={'class': 'form-control-file','id':'exampleFormControlFile1'}), 
            "Degrees": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. MBBS,MD,PHD'}),
            "Home_Address": forms.TextInput(attrs={'class': 'form-control','placeholder':'Bantala,Science City,Kolkata,700150'}),
        }
class Ambulance(forms.ModelForm):
    class Meta:
        model = ambulances
        fields = [
            "username",
            "Driver_name",
            "Ambulances_Number",
            "Hospital_Belongs_to",
            "Upload_Ambulance_Pic",
            "Bed_to_Bed_Transfer_Facility",
            "emergency_online_support_team",
            "Special_care_teams_and_physicians",
            "Transfer_the_patient_under_doctors",
            "Both_side_road_ambulances",        
        ]
        widgets = {
            "username": forms.HiddenInput(), 
            "Driver_name": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Soumik Dutta'}), 
            "Ambulances_Number": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. WB126P63'}), 
            "Hospital_Belongs_to": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. CMC (calcutta)'}), 

        }
        labels = {
            "Driver_name":"Driver's_name",
            "Bed_to_Bed_Transfer_Facility": "Bed to Bed Transfer Facility at Affordable Rent",
            "emergency_online_support_team": "24X7 emergency online tech-support team",
            "Special_care_teams_and_physicians": "Special care teams and physicians with the patient as well as special care of patients with ICU",
            "Transfer_the_patient_under_doctors": "Transfer the patient under the supervision of specialized doctors and health care specialists",
            "Both_side_road_ambulances": "Both side road ambulances to pick up and drop off the patient",

    }
class Hospital(forms.ModelForm):
    class Meta:
        model = hospital
        fields = [
            "username",
            "Hospital_Name",
            "Address",
            "Pictures",
            "Depertment",
            "Microbiology",
            "Pathology",
            "Medicine",
            "Opthalmology",
            "Ostiology",
            "Sergery",
            "Features",
            "Bypass_surgery",
            "Eye_operation",
            "Delivery",
            "Dialysis",
            "Anjioplasty",
            "Chemotherapy",
            "Dengue",
            "Covid_19_treatment",
        ]
        widgets = {
            "username": forms.HiddenInput(), 
            "Hospital_Name": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Soumik Dutta'}), 
            "Address": forms.TextInput(attrs={'class': 'form-control','placeholder':'eg. Soumik Dutta'}), 
            "Depertment": forms.TextInput(attrs={'class': 'form-control','placeholder':'Write or pic a tick Depertment of Doctors available'}),
            "Features": forms.TextInput(attrs={'class': 'form-control','placeholder':'Write or pic a tick on the Feaatures Available in your Hospital'}),
        }

class file2link(forms.ModelForm):
    class Meta:
        model = file2links
        fields = [
            "username",
            "Upload_File",

        ] 
        widgets = {
            "username": forms.HiddenInput(), 
        }

class chat(forms.ModelForm):
    class Meta:
        model = chats
        fields = [
            "Send_To",
            "sender_Id",
            "msg",
            "Attatch_File",

        ] 
        widgets = {
            "sender_Id": forms.HiddenInput(), 
            "Send_To": forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Sending Id...'}), 
            "msg": forms.TextInput(attrs={'class': 'form-control','placeholder':'Write Your Message.............'}),

        }
        labels = {
            "msg":"Message",
        }