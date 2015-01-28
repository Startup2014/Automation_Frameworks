************
Setup for iOS Automation Framework :-
************

Preconditions:

	Device(Jailbreaken):
		1 Jailbreak your iPod 5.1.1
		2 Install Veency on iDevice and set connection password to 'symantec'
		3 Drag Settings from the first screen pan to the second. place it together with Cydia.
	
	Device(EggOn from Eggplant): To be added by Samrat.


MAC box system environment setting:
	1 Install JAVA 1.6
	2 Install Python 2.7
	3 Install Jython 2.7
	4 Install Sikuli (1.0 R930)
	5 Set system variables of software we used in profile( current user or root)
		SIKULIHOME, SIKULIJAR, PYTHONPATH, JYTHONHOME, JYTHONPATH
	6 Set JYTHONHOME and SIKULIHOME  into PATH
	7 Set SIKULIJAR into CLASSPATH
	8 Install Chrome Driver as UI_Automation_Readme.txt
	9 Example of system variable configuration. Following are the system variables on Joshua`s MAC box.
		9.1 Enable root user on MAC box first( only for configuration system variable purpose ).
		9.2 Add related system variables in to /etc/profile
			# Java
			export JAVA_HOME=/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
			
			# Android SDK
			export ANDROID_HOME=/Users/Joshua/adt-bundle-mac/sdk
			export ADTTOOLS=$ANDROID_HOME/tools
			export ADTPTOOLS=$ANDROID_HOME/platform-tools

			# AndroidViewClient
			export ANDROID_VIEW_CLIENT_HOME=/Users/Joshua/AndroidViewClient-master/AndroidViewClient
				
			# Sikuli (1.0 R930)
			export SIKULI_HOME=/Applications/Sikuli-IDE.app
			export SIKULI_JAR=$SIKULI_HOME/Contents/Resources/Java/sikuli-script.jar
			
			# SikuliX(1.0.0)
			#export SIKULI_HOME=/Users/Joshua/SikuliX
			#export Dsikuli.Home=${SIKULI_HOME}
			#export SIKULIX_HOME=${SIKULI_HOME}
			#export SIKULI_JAR=${SIKULI_HOME}/sikuli-script.jar
			#export SIKULIX_Libs=${SIKULI_HOME}/libs
			
			# Appcenter Automation workspace
			ACAW=/Users/Joshua/Perforce/jun_jiang_BeiJings-MacBook-Pro_4868/depot/Enterprise_Mobile_Engineering/Projects/Nukona/qa/trunk/Appcenter_Automation
			API=/Users/Joshua/Perforce/jun_jiang_BeiJings-MacBook-Pro_4868/depot/Enterprise_Mobile_Engineering/Source/Nukona/trunk/web-ui-test:/Users/Joshua/Perforce/jun_jiang_BeiJings-MacBook-Pro_4868/depot/Enterprise_Mobile_Engineering/Source/Nukona/trunk/web-ui-test/api_tests:/Users/Joshua/Perforce/jun_jiang_BeiJings-MacBook-Pro_4868/depot/Enterprise_Mobile_Engineering/Source/Nukona/trunk/web-ui-test/api_tests/api_infra:
		
			# Python
			export PYTHONPATH=/Library/Python/2.7/site-packages:$ACAW:$PYTHONPATH:${API}:${ANDROID_VIEW_CLIENT_HOME}/src
	
			# Jython
			export JYTHON_HOME=/Users/Joshua/jython2.7b1
			export JYTHONPATH=$ACAW:$PYTHONPATH
			
			# Selenium Driver(Chromedriver)
			export SCD=/Users/Joshua/driver/
			
			# Path and Classpath
			export PATH=$JAVA_HOME/bin:$SCD:$ADTTOOLS:$ADTPTOOLS:$JYTHON_HOME:$SIKULI_HOME:$SIKULIX_Libs:$PATH
			export CLASSPATH=.:$SIKULI_JAR
			
			# Jenkins
			export JENKINSHOME=/Users/Joshua/JENKINSHOME
			

Trigger test case using command like below.
	jython -B runall.py --testsrc /Users/snac/Documents/workspace/Kungfu/Appcenter_Automation/src/com/EnterpriseMobilityEngineering/qa/ios --tenant lqac6.nuk9.com


How to install Sikuli Script 1.0.0 
	1 Download related package form here https://launchpad.net/sikuli/+download
		Sikuli-API-1.0.0-Mac.zip (Sikuli API for Mac OS X 10.6+)
		Sikuli-IDE-1.0.0-App.zip (Sikuli IDE "lightweight" Automator App for Mac 10.6+)
		Sikuli-1.0.0-SupplementalStuff.zip (supplemental stuff)
	2 Install Sikuli IDE App into you application. you can use it edit image
	3 unzip Sikuli API to a folder such as "/Users/Joshua/SikuliX". it will be used in system variable configuration part.
	4 unzip Sikuli SupplementalStuff to a folder such as "/Users/Joshua/SikuliXSupplementalStuff"
		4.1This folder is an excerpt from the bundled Jython in sikuli-script.jar.copy the folder sikuli to your installed Jython folder into Lib/site-packages. This will make it available automatically at runtime.
		4.2At the same time, you cold copy the folder sikuli to our AppcenterAutomation folder to avoid missing Sikuli modul error.
	5 Configure Sikuli`s variable into you profile and add them into PATH and CLASSPATH( Please refer to example in 9.2)	
		# SikuliX(1.0.0)
		export SIKULI_HOME=/Users/Joshua/SikuliX
		export Dsikuli.Home=${SIKULI_HOME}
		export SIKULIX_HOME=${SIKULI_HOME}
		export SIKULI_JAR=${SIKULI_HOME}/sikuli-script.jar
		export SIKULIX_Libs=${SIKULI_HOME}/libs
		# Path and Classpath
		export PATH=$JAVA_HOME/bin:$SCD:$ADTTOOLS:$ADTPTOOLS:$JYTHON_HOME:$SIKULI_HOME:$SIKULIX_Libs:$PATH
		export CLASSPATH=.:$SIKULI_JAR

Outside resources(WIKI/Guide):
	1 Sikuli Script project`s address: http://www.sikuli.org
	2 Download: https://launchpad.net/sikuli/+download
	3 Usign Jython in eclipse: https://github.com/RaiMan/SikuliX-API/wiki/Usage-in-Java-programming#special-information-on-using-external-jython-in-ides-like-eclipse
	4 GitHub: https://github.com/RaiMan/SikuliX-API
	5 Sikuli Documentation: http://doc.sikuli.org
	6 Sikuli VS Eggplant: http://testwarriors.blogspot.com/2012/04/comparison-report-sikuli-vs-eggplant.html