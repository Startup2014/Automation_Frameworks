************
Setup for UI :-
************


1. install selenium-python bindings. download and follow the instructions from here - http://code.google.com/p/selenium/wiki/PythonBindings

2. Check your network settings. In order to run the gui test cases, we need to have "no proxy settings" on 127.0.0.1, localhost 

3. For Browser Specific Settings

Update the browser[Firefox, Chrome, IE, Safari) in the test_settings.py

Chrome:-
 - Download the ChromeDriver from Appcenter_Automation/lib directory and add it your PATH 

IE:-
 - Download the IEDriver.exe [32bit or 64bit as needed] from Appcenter_Automation/lib and add it to your PATH
 - Download the selenium-server-standalone-2.23.1.jar and add it to your PATH

Firefox 
 - Not any specific settings needed 
 
Safari 
- Download the SeleniumSafari-driver extension from link- https://docs.google.com/folder/d/0B5KGduKl6s6-c3dlMWVNcTJhLUk/edit?pli=1&docId=0B5KGduKl6s6-UEJ4Wjk3TGw1TUk
or here -  Appcenter_Automation/lib and drag/drop on safari browser. this will add the safari driver extension to the browser
- Start the selenium-server-standalone-2.23.1.jar by using command - java -jar selenium-server-standalone-2.23.1.jar

4. Update the settings file with tenant specific information

5. Run the test:
Run all Test Cases - python runall.py
Run Specific Test case - runall.py -p test_AppsPage* --prefix test_addNewApkAppUnpublished [ commands to run specific test cases]
Run the smoke test :- runall.py --prefix test_Smoke [dir] e.g python runall.py --prefix test_Smoke src/com/EnterpriseMobilityEngineering/qa/ui





*********
Optional for setup - Details on how downloads is working for different framework
*********

1. In the command line , we can provide the Ñframework parameter with values -> ui, ios android, ui_isv  
	Example - python runall.py Ñprefix=test_DownloadAndroidAppcenterApp Ñframework android
2. By default , if Ñframework not specified, download will be default Appcenter_Automation/downloads directory 
3. Based on framework specified on command line , download will be for the specific folder 
	UI -> ui/downloads [ setting for iOS download directory in ui_settings file]  
	UI_ISV -> ui_isv/downloads [ setting for iOS download directory in ui_isv_settings file]  
	ANDROID -> android/apks [ setting for iOS download directory in android_settings file]  
	IOS -> ios/downloads [ setting for iOS download directory in ui_settings file]  

4. Considering it is controlled by setting in respective framework setting file , you can update the setting to control which folder you download in ur test framework 


