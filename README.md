## AppiumTest

### Develop Platform
- Android Studio
- PyCharm

### Project Structure

```
kooTest
├── Common
│     ├── Public
│     │     ├── __init__.py
│     │     ├── AXMLParser.py       # resolve binary xml
│     │     ├── HTMLTestRunner.py
│     │     ├── Keycode.py
│     │     ├── String.py
│     │     └── System.py
│     ├── __init__.py
│     ├── Command.py
│     ├── DeviceInfo.py
│     ├── Logger.py           # code layer log    
│     ├── MyLog.py            # android layer log  
│     ├── ReadData.py
│     └── SendEmail.py
├── Data
│     ├── cap.xml
│     └── testcase.xlsx
├── Module
│     ├── __init__.py
│     ├── BasePage.py
│     ├── DashPage.py
│     ├── HomePage.py
│     └── SubPage.py
├── Result
│     ├── 2016-xx-xx
│     │     ├── Log_2016-xx-xx_xx.xx.xx.log
│     │     ├── OutPut.log
│     │     ├── Report_2016-xx-xx_xx.xx.xx.html
│     │     └── Image
│     │            ├── xx_2016-xx-xx_xx.xx.xx.png
│     │            └── xx_2016-xx-xx_xx.xx.xx.png
│     └── appium.log
├── Testcase
│     ├── Test_xxx.py
│     └── Test_xxx.py
├── Runner.py
└── AutoRun.bat
```