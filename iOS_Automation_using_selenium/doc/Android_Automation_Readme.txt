to RUN Android test FW:

runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_ --testsrc C:\P4\depot\Enterprise_Mobile_Engineering\Projects\Nukona\qa\trunk\Appcenter_Automation\src\com\EnterpriseMobilityEngineering\qa\android\testSet --password=[password] --tenant=[AppCenter adress] --framework=android

	example: [python runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_ --testsrc C:\P4\depot\Enterprise_Mobile_Engineering\Projects\Nukona\qa\trunk\Appcenter_Automation\src\com\EnterpriseMobilityEngineering\qa\android\testSet --password=@Altiris3 --tenant=jlrhel.tales.sen.symantec.com --framework=android]

Currently we have:
test_set_AppCenterApp_Root_P1_Smoke_a_First_Run
test_set_AppCenterApp_Root_P1_Smoke_b_MDM_Policies

Following are system settings before you run android automation of appcenter automation suite.

1Jave settings:
	Install JDK 1.6
	Add syatem Varibale "JAVA_HOME" with value "c:\java\jdk160". the value depends on your java installation folder.
	Add "%JAVA_HOME%\bin" into System Variable PATH
	Add "%JAVA_HOME%\lib" into Syatem Variable CLASSPATH

2 Android SDK settings:
	Add Android home and point plaform-tools and tools into system PATH
	Add "ANDROID_HOME" as System Variable with value "c:\Joshua\Android-sdk"
	Add "%ANDROID_HOME%\tools" into System Variable PATH
	Add "%ANDROID_HOME%\platform-tools" into System Variable PATH

3 Python settings:
	Install python2.7.x( python-2.7.3.msi on windows)
	Add syatem Varibale "python_home" with value "E:\programs\Python273"
	Add "%python_home%" into System Variable PATH
	Add "%python_home%\lib" into System Variable PATH
	Add syatem Varibale "PYTHONPATH" and set Appcenter automation folder location as it`s value, such as "E:\Appcenter_Automation"

4 7z settings( 7z will be used to zip and unzip apk files on windows platform and it is open source software. On linux, zip and unzip will be used)
	Instatall 7z (7z922.msi)
	Add its location in to System Variable PATH, such as "C:\Program Files (x86)\7-Zip"
	
5 ANT settings:
	Download and unzip ANT.
	Add its location in to System Variable PATH, such as "apache-ant-1.8.4\bin;"

6 Create a custom Firefox profile 
	http://intranet.emm.symantec.com/display/QA/AppCenter
	
7 Copy debug.keystore from this folder to %USER%/.android/debug.keystore 

8 Install PSUtil
	easy_install psutil


Outside resources(WIKI/Guide):
1 WIKI of env setting on win and linux: http://socialtext.ges.symantec.com/ent-mobile-eng/android_testing_environment_configuration
2 7zip: http://www.7-zip.org/ (x64 does not work with our setup)
3 Install selenium within python on MAC
	3.1 Download setuptool from http://pypi.python.org/pypi/setuptools/#cygwin-mac-os-x-linux-other
	3.2 Install it on MAC as the WIKI above.
	3.3 Download and install pip "sudo python setup.py install" http://pypi.python.org/pypi/pip/1.2.1
	3.4 Install selenium through pip "sudo pip install -U selenium"

	
8. For the Android_Wrap_Test for encryption, we need to have installed OINotepad before running the test. as we need to open the installed - Expenses app doc in OINotepad.
Note, the test does not check on in which software we need to open

9. Android webdriver setup Instructions:- 
Install the WebDriver APK

Every device or emulator has a serial ID. Run this command to get the serial ID of the device or emulator you want to use:

$~/android_sdk/platform-tools/adb devices

Download the Android server from our downloads page. To install the application do:

$./adb -s <serialId> -e install -r  android-server.apk

Make sure you are allowing installation of application not coming from Android Market. Go to Settings -> Applications, and check "Unknown Sources".

Start the Android WebDriver application through the UI of the device or by running this command:

$./adb -s <serialId> shell am start -a android.intent.action.MAIN -n org.openqa.selenium.android.app/.MainActivity

You can start the application in debug mode, which has more verbose logs by doing:

$./adb -s <serialId> shell am start -a android.intent.action.MAIN -n org.openqa.selenium.android.app/.MainActivity -e debug true

Now we need to setup the port forwarding in order to forward traffic from the host machine to the emulator. In a terminal type:

$./adb -s <serialId> forward tcp:8080 tcp:8080

This will make the android server available at http://localhost:8080/wd/hub from the host machine. You're now ready to run the tests. Let's take a look at some code. 


Using API for Android Testing (in case �RunPythonTest API password reset flow�(test_NewTenant_PasswordResetFlow) ):

1 pip install BeautifulSoup
2 easy_install M2Crypto


Outside resources(WIKI/Guide):
1 WIKI of env setting on win and linux: http://socialtext.ges.symantec.com/ent-mobile-eng/android_testing_environment_configuration
2 7zip: http://www.7-zip.org/ (x64 does not work with our setup)
3 Install selenium within python on MAC
	3.1 Download setuptool from http://pypi.python.org/pypi/setuptools/#cygwin-mac-os-x-linux-other
	3.2 Install it on MAC as the WIKI above.
	3.3 Download and install pip "sudo python setup.py install" http://pypi.python.org/pypi/pip/1.2.1
	3.4 Install selenium through pip "sudo pip install -U selenium"

App Wrap Test Cases Preconditions: 

1. Download AndroidViewClient - https://github.com/dtmilano/AndroidViewClient and Install AndroidViewClient and setup env variable �ANDROID_VIEW_CLIENT_HOME . This is being used here - sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
2. patch chimpchat to support all of the properties in the different Views.[ use attach one] . This is under ANDROID_HOME/tools/lib
3. For the Android_Wrap_Test for encryption, we need to have installed OINotepad before running the test. as we need to open the installed - Expenses app doc in OINotepad.Note, the test does not check on in which software we need to open


Automated test suite list:

1.1 Acceptance ENT
 python -B runall.py --prefix=test_set_Acceptance_Trunk_ENTERPRISE --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant test7.isv.nuk9.com --password @Altiris2
 python -B runall.py -p test_set_AppCenterApp_Regression_P1_MDMIntegration.py --prefix test_set_AppCenterApp_Root_P1_AE003_NewDeviceTargetPolicyMDMEnabled --testsrc=src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android

1.2 Acceptance ISV
 python -B runall.py --prefix=test_set_Acceptance_Trunk_ISV --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant test10.isv.nuk9.com --password @Altiris2


2.1 Regression ENT
 Python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_a_First_Run_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2
 python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_c_WrapPartA_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2
 python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_c_WrapPartB_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2

 MDM Integration Regression [ Nexus Device ]
 python -B runall.py -p test_set_AppCenterApp_Regression_P1_MDMIntegration.py --prefix test_set_AppCenterApp_Root_P1_ --testsrc=src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --tenant=nuk8auto16.nuk8.com --username=nitin_kagale --password=@Altiris2 --framework=android

  2.1.1 Backup commands
   Python -B runall.py -p test_set_AppCenterApp_Regression_P1_MDMIntegration.py --prefix test_set_AppCenterApp_Root_P1_AE027_AndroidEnrollmentWizard_CancelAgentInstall --testsrc=src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --tenant=nuk8auto16.nuk8.com --username=nitin_kagale --password=@Altiris2 --framework=android
   Python -B runall.py -p test_set_AppCenterApp_Regression_P1_MDMIntegration.py --prefix test_set_AppCenterApp_Root_P1_AE025_test_DisagreeEula --testsrc=src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --tenant=nuk8auto16.nuk8.com --username=nitin_kagale --password=@Altiris2 --framework=android
   Python -B runall.py -p test_set_AppCenterApp_Regression_P1_MDMIntegration.py --prefix test_set_AppCenterApp_Root_P1_AE026_AndroidEnrollmentWizard_CancelDeviceAdmin --testsrc=src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --tenant=nuk8auto16.nuk8.com --username=nitin_kagale --password=@Altiris2 --framework=android


2.2 Regression ISV
 Python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_a_First_Run_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2
 Python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_SymantecSealed_PartA_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2
 Python -B runall.py --prefix test_set_AppCenterApp_Root_P1_Smoke_SymantecSealed_PartB_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant acaucostest02.mtvus.sen.symantec.com --password @Altiris2

3.1 Upgrade ENT
 python -B runall.py --prefix test_set_AppCenterApp_Upg_Pre_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant autoisv7.ssp.nuk8.com --password @Altiris2a
 python -B runall.py --prefix test_set_AppCenterApp_Upg_Post_UIAutomator --testsrc src/com/EnterpriseMobilityEngineering/qa/android/testset_uiautomator --framework=android --tenant autoisv7.ssp.nuk8.com --password @Altiris2a