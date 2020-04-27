
from functions import *

LOG_DIR_PATH = 'C:\Test_logs\\'  # Location where the log files should be copied

initial_wait_time = 0*60    # Amount of time it should wait before start running scripts
test_repeat_count = 1      # Number of times all the tests should be executed on same test system

# Include the list of features that has to be run with required option - Appliance IP, data variable file name, and the script to be executed

script_list = [
				{ 'ipv6_tests': r'--variable APPLIANCE_IP:[2001::21] --variablefile C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\data_variables_icm_ipv6.py  C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\ICM_IPV6_TestCases_ipv6_only_mode.txt'},
				{'Nitro_FC_License_test': r'--variable APPLIANCE_IP:192.168.145.51 --variablefile C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\FC_license_data_variables.py  C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\FC_License_TestCases.txt'},
				{'Nitro_50gb_downlink_License_test': r'--variable APPLIANCE_IP:192.168.145.52 --variablefile C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\50gb_downlink_License_data_variables.py  C:\Fusion_Code\4.10\10-Jan-2018\fusion\tests\wpst_crm\wpst-crm-india\OV_ICM_IPV6_Support\50gb_downlink_License_TestCases.txt'},
				]

				
RunRGTestScripts(initial_wait_time, script_list, LOG_DIR_PATH, test_repeat_count)

ExecutionTermination()


