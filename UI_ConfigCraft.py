import streamlit as st

# Title of the app
st.title("Firewall Configuration Generator Questionnaire")

# Firewall Type selection
firewall_type = st.selectbox("Please specify the type of firewall you want to configure",
                             ["Network-based Firewall", "Host-based Firewall", "Application Firewall", "Other"])
if firewall_type == "Other":
    firewall_type = st.text_input("Please specify the firewall type")

# Firewall Type Known selection
firewall_type_known = st.selectbox("Is the Firewall Type Known?", ["Yes", "No"])

# Firewall Vendor selection (if known)
if firewall_type_known == "Yes":
    firewall_vendor = st.selectbox("Please specify the firewall vendor",
                                   ["Cisco", "Juniper", "Palo Alto Networks", "Check Point", "Fortinet"])
else:
    firewall_vendor = "N/A"

# Configuration options selection
configuration_options = st.multiselect("Please specify the specific configuration options you require",
                                      ["Access Control Lists (ACLs)", "NAT (Network Address Translation)",
                                       "VPN (Virtual Private Network)", "Intrusion Detection/Prevention Systems (IDS/IPS)",
                                       "Port Forwarding", "Other"])
if "Other" in configuration_options:
    configuration_options.remove("Other")
    configuration_options.append(st.text_input("Please specify the configuration option"))

# Firewall Features requirement (if firewall type or vendor is not known)
firewall_features = st.multiselect("Please specify the features you require in the firewall configuration",
                                   ["Advanced Threat Protection", "Web Filtering", "Application Control",
                                    "Centralized Management", "High Availability"])

# Additional Information input
additional_info = st.text_area("Please provide any additional details or specifications for the firewall configuration")

# Generate Configuration Files button

if st.button("Generate Configuration Files"):

    # Call the function to generate the configuration files here

    generate_config(firewall_type, firewall_vendor, configuration_options, firewall_features, additional_info)

    st.success("Configuration files generated successfully!")

    #docker build

    # Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Streamlit and the required dependencies
RUN pip install --no-cache-dir streamlit==1.10.0

# Expose the Streamlit app port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]





    


    