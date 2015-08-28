************
Run test_PLACR003_BuildWrapKitiOSApp test case in test_ProgramLibrary.py
************
Preconditions:
1. Install Xcode(V4.6.1) and Command Line Tools
2. Install related certs
1) NUk`s Dist Cert (installed in keychain Access)
2) Provisioning profile -> /Appcenter_Automation/resource/ioscerts/EME_Beijing_QA_team_Joshua_BJ_NUK_DP.mobileprovision(Double click to install it in to Organizer of Xcode)

Instruction:
1. cd ~/Appcenter_Automation/
2. python runall.py -p test_ProgramLibrary.py --prefix test_PLACR003_BuildWrapKitiOSApp